#!/bin/bash

echo "🎥 Instagram Stream Key Setup for Streamlabs"
echo "=========================================="
echo ""
echo "1. Open Streamlabs OBS"
echo "2. Go to Settings → Stream tab"
echo "3. Select Instagram and connect your account"
echo "4. Copy the Stream Key from Streamlabs"
echo ""
read -p "Paste your Instagram Stream Key here: " stream_key
echo ""

if [ -z "$stream_key" ]; then
    echo "❌ No stream key provided. Exiting..."
    exit 1
fi

# Backup original file
cp stream_ig.sh stream_ig.sh.backup

# Update the stream key in the script
sed -i "s/YOUR_INSTAGRAM_STREAM_KEY/$stream_key/" stream_ig.sh

echo "✅ Stream key updated successfully!"
echo "📁 Backup saved as: stream_ig.sh.backup"
echo ""
echo "🚀 Ready to stream! Run:"
echo "   ./stream_ig.sh"
echo ""
echo "To restore backup: cp stream_ig.sh.backup stream_ig.sh"
