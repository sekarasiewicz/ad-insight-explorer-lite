#!/bin/bash

echo "=== Simple Deployment Script ==="
echo "This script builds backend locally and deploys everything"
echo ""

# Check if Docker is running
if ! docker info > /dev/null 2>&1; then
    echo "❌ Docker is not running. Please start Docker first."
    exit 1
fi

echo "✅ Docker is running"
echo ""

# Stop any existing containers
echo "1. Stopping existing containers..."
docker compose -f docker-compose.registry.yml down 2>/dev/null || true
echo ""

# Clean up old images to save space
echo "2. Cleaning up old images..."
docker system prune -f
echo ""

# Build backend locally (this works)
echo "3. Building backend image..."
cd backend
if docker build -t ad-insight-backend:latest .; then
    echo "✅ Backend built successfully"
else
    echo "❌ Backend build failed"
    exit 1
fi
cd ..

echo ""

# Start the application (frontend will build during startup)
echo "4. Starting application..."
docker compose -f docker-compose.registry.yml up -d
echo ""

# Check if containers are running
echo "5. Checking container status..."
sleep 10
docker compose -f docker-compose.registry.yml ps
echo ""

# Show logs
echo "6. Recent logs:"
docker compose -f docker-compose.registry.yml logs --tail=10
echo ""

echo "=== Deployment Complete! ==="
echo "Your application should be available at:"
echo "  Frontend: http://localhost"
echo "  Backend API: http://localhost:8000"
echo ""
echo "To view logs: docker compose -f docker-compose.registry.yml logs -f"
echo "To stop: docker compose -f docker-compose.registry.yml down" 