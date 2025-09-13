import discord
from discord.ext import commands
import yt_dlp
import boto3
import json
from dotenv import load_dotenv




# Discord Bot Setup
intents = discord.Intents.default()  #permissions
intents.voice_states = True
intents.message_content = True  # Only needed if bot reads messages

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user.name} is ready to play!  ")

@bot.command()
async def play(ctx, url):
    """Joins your voice channel and streams YouTube audio.""" # This is used for !help
    # Check if user is in a voice channel
    if not ctx.author.voice:
        await ctx.send("❌   You are not in a voice channel. Please join one and try again!  ")
        return

    # Get the voice channel
    voice_channel = ctx.author.voice.channel

    # Connect to voice
    try:
        vc = await voice_channel.connect()
    except discord.ClientException:
        await ctx.send("❌   Bot is in use in another channel!")
        return

    # Get YouTube audio URL using yt-dlp
    try:
        ydl_opts = {
            'format': 'bestaudio/best', # Prioritizes audio-only
            'extract_flat': True,  # Extracts only metadata without downloading (faster)
            'cookiefile': '/home/ssm-user/discord_bot/yt_cookies.txt'
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl: # Ensures proper resource cleanup
            info = ydl.extract_info(url, download=False) # no file saved, only getting URL
            audio_url = info['url']  # Direct stream URL

    except Exception as e:
        await ctx.send(f"❌   Error fetching YouTube audio: {e}")
        await vc.disconnect()
        return

    # Stream audio using FFmpeg
    ffmpeg_options = {
        'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
        'options': '-vn -filter:a "volume=0.8"'
    }

    try:
        vc.play(discord.FFmpegPCMAudio(audio_url, **ffmpeg_options))
        await ctx.send(f"🎶   Now playing: {url}")
    except Exception as e: #suggested by DS
        await ctx.send(f"❌   Error playing audio: {e}")
        await vc.disconnect()

@bot.command()
async def leave(ctx):
    """Disconnects the bot from voice."""
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.send("✅   Bot left channel!")
    else:
        await ctx.send("❌   Bot is not in any voice channels")


# Run the bot
if __name__ == "__main__":
    SSMclient = boto3.client('ssm', region_name='eu-north-1')
    response = SSMclient.get_parameter(
        Name='/Discord/Token',
        WithDecryption=True,
    )
    bot.run(json.loads(response['Parameter']['Value'])['TOKEN'])
