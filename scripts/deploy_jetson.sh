#!/bin/bash
# Deployment script for NVIDIA Jetson Orin Nano
echo "Deploying Wearable Invisible Suit firmware to Jetson Orin Nano..."
sudo apt-get update && sudo apt-get install -y python3-pip python3-opencv
pip3 install -r requirements.txt
echo "Deployment complete. Run 'python3 src/main.py' to start active camouflage."
