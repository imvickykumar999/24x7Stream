#!/bin/bash

ffmpeg -re -stream_loop -1 -i LoopVideo.mp4 \
-c:v libx264 -preset superfast -b:v 2000k -maxrate 2000k -bufsize 4000k \
-pix_fmt yuv420p -g 60 -c:a aac -b:a 128k -ar 44100 \
-f flv "rtmp://a.rtmp.youtube.com/live2/YOUR_YOUTUBE_STREAM_KEY" > stream_log.txt 2>&1
