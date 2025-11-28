#!/bin/bash

echo "🎥 Instagram Stream Key Setup for Streamlabs"
echo "=========================================="
echo ""
echo "1. Open Streamlabs OBS"
echo "2. Go to Settings → Stream tab"
echo "3. Select Instagram and connect your account"
echo "4. Copy the Stream Key from Streamlabs"
echo ""

# Check if config.env exists, create from example if not
if [ ! -f "config.env" ]; then
    if [ -f "config.env.example" ]; then
        cp config.env.example config.env
        echo "✅ Created config.env from template"
    else
        echo "❌ config.env.example not found. Creating basic config.env..."
        cat > config.env << 'EOF'
# YouTube Live Stream Key
YOUTUBE_STREAM_KEY=YOUR_YOUTUBE_STREAM_KEY

# Instagram Live Stream Key
INSTAGRAM_STREAM_KEY=YOUR_INSTAGRAM_STREAM_KEY
EOF
    fi
fi

read -p "Paste your Instagram Stream Key here: " stream_key
echo ""

if [ -z "$stream_key" ]; then
    echo "❌ No stream key provided. Exiting..."
    exit 1
fi

# Backup config file
cp config.env config.env.backup

# Update the Instagram stream key in config.env
sed -i "s/INSTAGRAM_STREAM_KEY=.*/INSTAGRAM_STREAM_KEY=$stream_key/" config.env

echo "✅ Instagram stream key updated successfully!"
echo "📁 Backup saved as: config.env.backup"
echo ""
echo "🚀 Ready to stream! Run:"
echo "   ./stream_ig.sh"
echo ""
echo "To restore backup: cp config.env.backup config.env"
