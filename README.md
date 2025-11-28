# Streaming API - Live Video Streaming Scripts

This repository contains shell scripts for streaming video content to YouTube Live and Instagram Live using FFmpeg.

## Prerequisites

- **FFmpeg** installed on your system
- **LoopVideo.mp4** video file in the same directory as the scripts
- Valid stream keys for the platforms you want to use

## Installation

### Install FFmpeg (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install ffmpeg
```

### Install FFmpeg (macOS)
```bash
brew install ffmpeg
```

### Install FFmpeg (Windows)
Download from the official FFmpeg website or use Chocolatey:
```bash
choco install ffmpeg
```

## Setup

### YouTube Live Setup
1. Go to [YouTube Live](https://www.youtube.com/live) and start a new live stream
2. Copy the **Stream URL** and **Stream Key**
3. Replace the RTMP URL in `stream_yt.sh` with your YouTube stream URL
4. Example: `rtmp://a.rtmp.youtube.com/live2/YOUR_STREAM_KEY`

### Instagram Live Setup
**Note**: Instagram doesn't provide RTMP keys directly. Here are the methods to get your stream key:

#### Method 1: Streamlabs OBS (Recommended - Easier than OBS Studio)
1. Download and install [Streamlabs OBS](https://streamlabs.com/) (free)
2. Create a Streamlabs account and connect your Instagram
3. In Streamlabs, go to Settings → Stream
4. Select "Instagram" as the service
5. Click "Go Live" to test and get your stream key
6. The RTMP URL and stream key will be automatically configured

#### Method 2: OBS Studio
1. Download and install [OBS Studio](https://obsproject.com/)
2. In OBS, go to Settings → Stream
3. Select "Instagram" as the service
4. Connect your Instagram account and start a live stream
5. OBS will automatically get the stream key for you

#### Streamlabs OBS Setup Guide

**Why Streamlabs?** Easier Instagram integration, built-in overlays, and simpler setup than OBS Studio.

**Step-by-Step Setup:**
1. **Download**: Get [Streamlabs OBS](https://streamlabs.com/) (free version available)
2. **Create Account**: Sign up and connect your Instagram account
3. **Configure Stream**:
   - Open Streamlabs → Settings (gear icon) → Stream tab
   - Select "Instagram" from the platform dropdown
   - Click "Connect Account" and authorize Instagram access
4. **Get Stream Key**:
   - In the Stream settings, you'll see "Stream Key" field
   - Copy this key (it will look like: `fb-live://...?stream_key=ABC123...`)
   - Use this key in your `stream_ig.sh` script

**Quick Start**:
```bash
# Option 1: Use the automated setup script
./setup_streamlabs_key.sh

# Option 2: Manual replacement
sed -i 's/YOUR_INSTAGRAM_STREAM_KEY/your_actual_key_here/' stream_ig.sh
./stream_ig.sh
```

#### Method 0: Meta Business Manager/Creator Studio
**Important Note**: Meta Business Manager and Creator Studio do NOT provide direct RTMP stream keys for custom streaming software. They offer:

- **Creator Studio**: Schedule and manage live streams, but uses Meta's own streaming interface
- **Meta Business Manager**: Business tools for live shopping and commerce, but no RTMP key access
- **Graph API**: Developer access for programmatic live streaming, but requires app approval and coding

**RTMP streaming to Instagram requires third-party tools or mobile apps.**

However, Meta does offer official alternatives:
- **Instagram Live Producer**: Web-based streaming dashboard (limited beta access)
- **Meta Live**: Professional streaming for verified creators/businesses
- **Facebook Gaming**: For gaming streams that can be shared to Instagram

For programmatic access, you can use Meta's Graph API with approved apps, but this requires developer setup and app review. See `meta_live_api_example.py` for a demonstration (advanced users only).

#### Method 2: Browser Developer Tools (Advanced)
1. Open Instagram in your web browser (instagram.com)
2. Press F12 to open Developer Tools
3. Go to the Network tab
4. Start an Instagram Live stream
5. Look for network requests containing "rtmp" or "live-api-s.facebook.com"
6. Extract the stream key from the request URL

#### Method 3: Third-party Services
Use services like:
- Yellow Duck (yellowduck.tv)
- Streamaxia
- Restream.io (supports Instagram integration)

#### Method 4: Mobile Streaming Apps
Apps like:
- Larix Broadcaster
- Streamlabs Mobile
- Switcher Studio

#### Method 5: Using the Included Python Script
1. Start Instagram Live in your browser
2. Press F12 to open Developer Tools
3. Go to Network tab and start recording
4. Start your Instagram Live stream
5. Export the network log as HAR file (Right-click → Save as HAR)
6. Run: `python3 get_ig_key.py your_file.har`
7. The script will extract your stream key automatically

**Once you have your stream key, replace `YOUR_INSTAGRAM_STREAM_KEY` in `stream_ig.sh` with your actual key.**

## Usage

### YouTube Live Streaming
```bash
./stream_yt.sh
```

### Instagram Live Streaming
```bash
./stream_ig.sh
```

## Script Details

Both scripts use the following FFmpeg parameters:
- **Input**: `LoopVideo.mp4` (loops indefinitely)
- **Video Codec**: H.264 (libx264)
- **Preset**: superfast (for low latency)
- **Video Bitrate**: 2000k (adjustable)
- **Audio Codec**: AAC
- **Audio Bitrate**: 128k
- **Keyframe Interval**: 60 frames
- **Output Format**: FLV (required for RTMP)

## Logs

- **YouTube logs**: `stream_log.txt`
- **Instagram logs**: `stream_ig_log.txt`

Check these files if you encounter any issues.

## Customization

You can modify the scripts to change:
- Video bitrate: `-b:v 2000k`
- Audio bitrate: `-b:a 128k`
- Resolution: Add `-s 1920x1080` for HD
- Frame rate: Add `-r 30` for 30fps

## Troubleshooting

### Common Issues:
1. **"No such file or directory"**: Ensure `LoopVideo.mp4` exists in the same directory
2. **Connection failed**: Check your internet connection and stream key validity
3. **Stream not visible**: Wait a few seconds after starting the script

### Checking FFmpeg Installation:
```bash
ffmpeg -version
```

### Testing Stream Without Broadcasting:
Remove the RTMP URL and use a local output for testing:
```bash
ffmpeg -re -stream_loop -1 -i LoopVideo.mp4 -c:v libx264 -preset superfast -f flv test_output.flv
```
