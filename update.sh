#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

echo "=================================================="
echo "🚀 Starting IvyTech Nexus / Wearable Suite Update"
echo "=================================================="

# 1. Pull the latest changes from the repository
echo "==> Pulling latest changes from git..."
git pull origin main

# 2. Check and fix requirements.txt syntax if needed (ensuring >= instead of ->)
echo "==> Verifying requirements.txt syntax..."
if [ -f "requirements.txt" ]; then
    sed -i 's/->/>=/g' requirements.txt
    echo "✓ Requirements syntax checked and verified."
fi

# 3. Check if Docker and Docker Compose are available
echo "==> Checking Docker environment..."
if ! command -v docker &> /dev/null; then
    echo "❌ Docker could not be found. Please install Docker first."
    exit 1
fi

if ! docker compose version &> /dev/null; then
    echo "❌ Docker Compose V2 could not be found."
    exit 1
fi

# 4. Stop existing containers to prevent port or device conflicts
echo "==> Stopping existing containers..."
cd docker
docker compose down || true

# 5. Build and start containers using Docker Compose
echo "==> Building and starting Docker containers..."
docker compose up --build -d

echo "=================================================="
echo "✅ Update complete! Services are up and running."
echo "=================================================="

# 6. Show container status and logs summary
docker compose ps
