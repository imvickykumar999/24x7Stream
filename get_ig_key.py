#!/usr/bin/env python3
"""
Instagram Live Stream Key Extractor
This script helps you extract Instagram Live RTMP stream keys from browser network logs.

Usage:
1. Start Instagram Live in your browser
2. Save browser network logs as HAR file
3. Run: python3 get_ig_key.py your_log_file.har
"""

import json
import sys
import re

def extract_instagram_stream_key(har_file_path):
    """Extract Instagram Live stream key from HAR file"""
    try:
        with open(har_file_path, 'r', encoding='utf-8') as f:
            har_data = json.load(f)

        stream_key = None

        # Look through all network requests
        for entry in har_data.get('log', {}).get('entries', []):
            url = entry.get('request', {}).get('url', '')

            # Look for Instagram Live RTMP URLs
            if 'live-api-s.facebook.com' in url and 'rtmp' in url:
                # Extract stream key from URL
                match = re.search(r'/rtmp/([^/?]+)', url)
                if match:
                    stream_key = match.group(1)
                    break

        return stream_key

    except FileNotFoundError:
        print(f"Error: File '{har_file_path}' not found")
        return None
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in '{har_file_path}'")
        return None
    except Exception as e:
        print(f"Error processing file: {e}")
        return None

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 get_ig_key.py <har_file>")
        print("\nTo get a HAR file:")
        print("1. Open Instagram in Chrome/Firefox")
        print("2. Press F12 → Network tab")
        print("3. Start Instagram Live")
        print("4. Right-click any request → Save as HAR")
        sys.exit(1)

    har_file = sys.argv[1]
    stream_key = extract_instagram_stream_key(har_file)

    if stream_key:
        print("Found Instagram Stream Key:")
        print(f"Stream Key: {stream_key}")
        print(f"Full RTMP URL: rtmp://live-api-s.facebook.com:80/rtmp/{stream_key}")
        print("\nCopy this stream key to your stream_ig.sh script")
    else:
        print("No Instagram Live stream key found in the HAR file.")
        print("Make sure you captured the network traffic while starting Instagram Live.")

if __name__ == "__main__":
    main()
