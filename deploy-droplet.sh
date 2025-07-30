#!/bin/bash

echo "=== Droplet Deployment Script ==="
echo "This script deploys the application from Docker Hub images"
echo ""

# Check if Docker is running
if ! docker info > /dev/null 2>&1; then
    echo "❌ Docker is not running. Please start Docker first."
    exit 1
fi

# Check if we're logged into Docker Hub
if ! docker info | grep -q "Username"; then
    echo "❌ Not logged into Docker Hub. Please run 'docker login' first."
    exit 1
fi

echo "✅ Docker is running and logged in"
echo ""

# Stop any existing containers
echo "1. Stopping existing containers..."
docker compose -f docker-compose.registry.yml down 2>/dev/null || true
echo ""

# Clean up old images to save space
echo "2. Cleaning up old images..."
docker system prune -f
echo ""

# Pull latest images from Docker Hub
echo "3. Pulling latest images from Docker Hub..."
docker pull sebastiankarasiewicz/ad-insight-backend:latest
docker pull sebastiankarasiewicz/ad-insight-frontend:latest
echo ""

# Start the application
echo "4. Starting application..."
docker compose -f docker-compose.registry.yml up -d
echo ""

# Check if containers are running
echo "5. Checking container status..."
sleep 5
docker compose -f docker-compose.registry.yml ps
echo ""

# Show logs
echo "6. Recent logs:"
docker compose -f docker-compose.registry.yml logs --tail=10
echo ""

echo "=== Deployment Complete! ==="
echo "Your application should be available at:"
echo "  Frontend: http://$(curl -s ifconfig.me)"
echo "  Backend API: http://$(curl -s ifconfig.me):8000"
echo ""
echo "To view logs: docker compose -f docker-compose.registry.yml logs -f"
echo "To stop: docker compose -f docker-compose.registry.yml down" 