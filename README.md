# Streaming API - Live Video Streaming Scripts

This repository contains shell scripts for streaming video content to YouTube Live and Instagram Live using FFmpeg.

<img width="1535" height="981" alt="image" src="https://github.com/user-attachments/assets/1296a1f4-9ece-4838-9611-a31091999d04" />
<img width="1535" height="982" alt="image" src="https://github.com/user-attachments/assets/5967b845-9c19-46f4-893e-141dfedf9c4d" />

## Prerequisites

- **FFmpeg** installed on your system
- **Python 3.6+** for video downloading scripts
- **LoopVideo.mp4** video file in the same directory as the scripts (or download one using the provided script)
- Valid stream keys for the platforms you want to use

## Video Download and Preparation

### Download YouTube Videos
Use the included Python script to download videos from YouTube for streaming:

```bash
# Install dependencies
pip install -r requirements.txt

# Download a YouTube video (replace with your URL)
python3 download_youtube.py "https://www.youtube.com/shorts/lOPDr8C4z_A"

# Download with specific format
python3 download_youtube.py "https://youtu.be/VIDEO_ID" -f mp4

# Download audio only
python3 download_youtube.py "https://youtu.be/VIDEO_ID" -f audio -o music
```

**Supported formats:**
- `best` - Best available quality (default)
- `mp4` - MP4 format
- `webm` - WebM format
- `audio` - Audio only (MP3)
- `worst` - Lowest quality

### Prepare Video for Streaming
Once downloaded, you can rename your video to `LoopVideo.mp4` or update the scripts to use your video filename.

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

## Environment Configuration

### Important: Secure Your Stream Keys
1. Copy the example configuration:
   ```bash
   cp config.env.example config.env
   ```
2. Edit `config.env` with your actual stream keys
3. **Never commit `config.env` to version control** (it's in `.gitignore`)
4. Keep your stream keys secure and private

### Configuration File Structure
```
# Video file to stream (download using download_youtube.py)
VIDEO_FILE=your_video_file.mp4

# YouTube Live Stream Key
YOUTUBE_STREAM_KEY=your_youtube_key

# Instagram Live Stream Key
INSTAGRAM_STREAM_KEY=your_instagram_key
```

## Setup

### YouTube Live Setup
1. Go to [YouTube Live](https://www.youtube.com/live) and start a new live stream
2. Copy the **Stream Key** from YouTube
3. Add it to your `config.env` file:
   ```bash
   YOUTUBE_STREAM_KEY=your_youtube_stream_key_here
   ```
4. The script will automatically use this key from the environment file

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
# Use the automated setup script (recommended)
./setup_streamlabs_key.sh
./stream_ig.sh
```

**Manual Setup**:
Edit `config.env` and add your video file and stream keys:
```bash
VIDEO_FILE=your_downloaded_video.mp4
INSTAGRAM_STREAM_KEY=your_stream_key_from_streamlabs
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
