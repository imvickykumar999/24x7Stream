#!/bin/bash

# ==============================================================================
# FFmpeg 24/7 Stream Restarter
# This script continuously attempts to run the FFmpeg streaming command.
# If the command fails (e.g., due to RTMP server disconnect), the script
# will wait for a short period and then automatically restart the stream.
# ==============================================================================

# --- Configuration ---
INPUT_FILE="NCS.mp4"
RTMP_URL="rtmp://a.rtmp.youtube.com/live2/YOUR_YOUTUBE_STREAM_KEY"
RETRY_DELAY=5 # Time in seconds to wait before attempting a restart
# ---------------------

# The while true loop runs indefinitely, restarting the command whenever it fails.
while true; do
    echo "--- $(date) ---"
    echo "Attempting to start/restart FFmpeg stream..."

    # The original FFmpeg command. The quotes around $INPUT_FILE and $RTMP_URL
    # ensure paths with spaces are handled correctly (though not an issue here).
    ffmpeg -re -stream_loop -1 -i "$INPUT_FILE" \
        -vf "drawtext=fontfile=/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf:textfile=like_count.txt:reload=1:fontcolor=black:fontsize=70:box=1:boxcolor=white@1.0:boxborderw=10:x=w-tw-10:y=75,drawtext=fontfile=/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf:textfile=view_count.txt:reload=1:fontcolor=black:fontsize=70:box=1:boxcolor=white@1.0:boxborderw=10:x=w-tw-10:y=75+th+10,drawtext=fontfile=/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf:textfile=sub_count.txt:reload=1:fontcolor=black:fontsize=70:box=1:boxcolor=white@1.0:boxborderw=10:x=w-tw-10:y=75+th*2+20" \
        -c:v libx264 -preset veryfast -b:v 6800k -maxrate 6800k -bufsize 13600k -pix_fmt yuv420p -g 60 \
        -c:a aac -b:a 128k -ar 44100 \
        -f flv "$RTMP_URL"

    # If FFmpeg exits (whether due to success, which it shouldn't for a stream, or failure),
    # the script continues here.

    echo "FFmpeg stream process ended. Retrying in $RETRY_DELAY seconds..."
    # Wait for the specified delay before the while loop starts the next iteration.
    sleep "$RETRY_DELAY"
done
