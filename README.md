Discord YouTube Audio Streaming Bot
-----------------------------------
-----------------------------------

Overview:
A production-ready Discord bot that streams YouTube audio directly to user's voice channels in Discord servers without local file downloads. Built with Python, Discord.py, yt-dlp, Terraform and hosted on AWS.

Features:
- Direct YouTube Streaming: Streams audio directly from YouTube URLs
- No Downloads: No local storage required - streams in real-time
- oice Channel Management: Automatic connection/disconnection
- Error Resilient: Auto-reconnect on stream interruptions

Architecture Design
=================
Core Components:
- Python Application Layer: Discord.py bot with yt-dlp integration
- Audio Processing: FFmpeg audio transcoding and streaming
- AWS Infrastructure: EC2 deployment with SSM Parameter Store integration
- Security Layer: IAM role-based authentication and encrypted parameter storage
- Cookie Management: Automated cookie refresh system via cron jobs

Data Flow:
- User initiates playback via Discord command
- Bot retrieves YouTube content URL through yt-dlp with authentication cookies
- Audio stream processed through FFmpeg for Discord compatibility
- Secure voice transmission via Discord Voice Gateway
- Bot token managed through AWS SSM Parameter Store

Infrastructure Requirements
==========================
Cloud Services:
- Amazon EC2: Ubuntu 20.04+ instance for bot hosting
- AWS Systems Manager: Secure parameter storage for sensitive data
- IAM Roles: Instance profile with SSM read permissions

Software Dependencies:
- Python 3.8+ with virtual environment
- FFmpeg for audio processing
- yt-dlp for YouTube content extraction
- AWS CLI for parameter retrieval
- Discord.py for Discord API integration

Deployment Architecture
=====================
Instance Configuration:
- Ubuntu Server 20.04 LTS minimal installation
- Python virtual environment isolation
- Automated recovery and restart mechanisms


Discord Installation Prerequisites
=================================

Discord Bot with required intents:

- SERVER MEMBERS INTENT
- MESSAGE CONTENT INTENT
- VOICE STATES

Discord Apps permissions in server:
- Connect
- Speak
- Use Voice Activity
- Send Messages

Make sure to add Token in SSM as /Discord/Token.
 
For cookies managment, check pull-SSM.txt

How to Use
==========

Basic Commands:
--------------
!play <url>	-------> Stream YouTube audio

!leave	-----------> Disconnect from voice	

Example Session:
---------------
1-

User: !play https://youtube.com/watch?v=dQw4w9WgXcQ

Bot: 🎶 Now playing: https://youtube.com/watch?v=dQw4w9WgXcQ

2-


User: !leave

Bot: ✅ Left voice channel.


![drawio-diagram](https://i.postimg.cc/mZdptSYq/YT-audio-stream-discord-drawio.png)


Reference Documentation
======================
Discord Developer Portal: https://discord.com/developers/docs

yt-dlp GitHub Repository: https://github.com/yt-dlp/yt-dlp

AWS Systems Manager Parameter Store: https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html

AWS EC2 Documentation: https://docs.aws.amazon.com/ec2/

FFmpeg Official Documentation: https://ffmpeg.org/documentation.html
