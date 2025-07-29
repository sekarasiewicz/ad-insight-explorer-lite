#!/bin/bash

echo "=== Testing Build Process ==="
echo "This script will test the build process locally before deploying to droplet"
echo ""

# Test backend build
echo "1. Testing backend build..."
cd backend
if docker build -t test-backend .; then
    echo "✅ Backend build successful"
else
    echo "❌ Backend build failed"
    exit 1
fi
cd ..

echo ""

# Test frontend build
echo "2. Testing frontend build..."
cd frontend
if docker build -t test-frontend .; then
    echo "✅ Frontend build successful"
else
    echo "❌ Frontend build failed"
    exit 1
fi
cd ..

echo ""

# Test full production build
echo "3. Testing full production build..."
if docker compose -f docker-compose.prod.yml build; then
    echo "✅ Full production build successful"
else
    echo "❌ Full production build failed"
    exit 1
fi

echo ""
echo "=== All builds successful! ==="
echo "You can now deploy to your droplet server." 