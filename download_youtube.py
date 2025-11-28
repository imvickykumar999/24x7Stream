#!/usr/bin/env python3
"""
YouTube Video Downloader using yt-dlp
Supports downloading videos, shorts, and playlists from YouTube
"""

import os
import sys
import argparse
from yt_dlp import YoutubeDL

def download_video(url, output_path='downloads', format_choice='best'):
    """
    Download a YouTube video using yt-dlp

    Args:
        url (str): YouTube URL to download
        output_path (str): Directory to save the video
        format_choice (str): Video format/quality ('best', 'worst', 'mp4', etc.)
    """

    # Create output directory if it doesn't exist
    if not os.path.exists(output_path):
        os.makedirs(output_path)
        print(f"📁 Created directory: {output_path}")

    # yt-dlp options
    ydl_opts = {
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'format': format_choice,
        'progress_hooks': [progress_hook],
        'noplaylist': True,  # Download single video, not playlist
        'quiet': False,
        'no_warnings': False,
    }

    # Add format-specific options
    if format_choice == 'audio':
        ydl_opts.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        })
    elif format_choice == 'mp4':
        ydl_opts['format'] = 'best[ext=mp4]/best'
    elif format_choice == 'webm':
        ydl_opts['format'] = 'best[ext=webm]/best'

    try:
        print(f"🎥 Downloading: {url}")
        print(f"📂 Saving to: {output_path}")
        print(f"🎬 Format: {format_choice}")
        print("-" * 50)

        with YoutubeDL(ydl_opts) as ydl:
            # Extract video info first
            info = ydl.extract_info(url, download=False)
            print(f"📹 Title: {info.get('title', 'Unknown')}")
            print(f"👤 Channel: {info.get('uploader', 'Unknown')}")
            print(f"⏱️  Duration: {info.get('duration_string', 'Unknown')}")

            # Download the video
            ydl.download([url])

        print("\n✅ Download completed successfully!")

    except Exception as e:
        print(f"\n❌ Error downloading video: {e}")
        return False

    return True

def progress_hook(d):
    """Progress hook for download status"""
    if d['status'] == 'downloading':
        # Show download progress
        percent = d.get('_percent_str', '0%')
        speed = d.get('_speed_str', 'N/A')
        eta = d.get('_eta_str', 'N/A')
        print(f"\r📥 Downloading... {percent} at {speed} ETA: {eta}", end='', flush=True)

    elif d['status'] == 'finished':
        print(f"\n📝 Download finished, now converting...")

def main():
    parser = argparse.ArgumentParser(description='Download YouTube videos using yt-dlp')
    parser.add_argument('url', help='YouTube URL to download')
    parser.add_argument('-o', '--output', default='downloads',
                        help='Output directory (default: downloads)')
    parser.add_argument('-f', '--format', default='best',
                        choices=['best', 'worst', 'mp4', 'webm', 'audio'],
                        help='Video format/quality (default: best)')

    # If no arguments provided, show usage for the Shorts URL
    if len(sys.argv) == 1:
        print("🎬 YouTube Video Downloader")
        print("=" * 40)
        print("Usage: python3 download_youtube.py [URL] [OPTIONS]")
        print("")
        print("Examples:")
        print("  python3 download_youtube.py https://www.youtube.com/shorts/lOPDr8C4z_A")
        print("  python3 download_youtube.py https://youtu.be/VIDEO_ID -f mp4")
        print("  python3 download_youtube.py https://youtube.com/watch?v=VIDEO_ID -o my_videos -f audio")
        print("")
        print("Format options:")
        print("  best   - Best available quality (default)")
        print("  worst  - Lowest available quality")
        print("  mp4    - Best MP4 format")
        print("  webm   - Best WebM format")
        print("  audio  - Extract audio only (MP3)")
        print("")
        print("💡 Tip: You can also run the script directly on the Shorts URL")
        return

    args = parser.parse_args()

    # Download the video
    success = download_video(args.url, args.output, args.format)

    if success:
        print("\n🎉 Video downloaded successfully!")
        print(f"📂 Check the '{args.output}' folder for your video")
    else:
        print("\n💥 Download failed. Please check the URL and try again.")
        sys.exit(1)

if __name__ == "__main__":
    main()
