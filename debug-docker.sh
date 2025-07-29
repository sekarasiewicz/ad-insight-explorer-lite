#!/bin/bash

echo "=== Docker Build Debug Script ==="
echo "This script will help debug Docker build issues on your droplet"
echo ""

# Check Docker version
echo "1. Checking Docker version:"
docker --version
echo ""

# Check available disk space
echo "2. Checking available disk space:"
df -h
echo ""

# Check available memory
echo "3. Checking available memory:"
free -h
echo ""

# Check network connectivity to PyPI
echo "4. Testing network connectivity to PyPI:"
curl -I https://pypi.org/simple/ 2>/dev/null | head -1
echo ""

# Clean up Docker system
echo "5. Cleaning up Docker system:"
docker system prune -f
echo ""

# Try building with verbose output
echo "6. Attempting Docker build with verbose output:"
echo "Building backend image..."
docker build -t backend-debug ./backend --no-cache --progress=plain 2>&1 | tee build.log

echo ""
echo "=== Build completed ==="
echo "Check build.log for detailed output"
echo "If the build failed, the log will show exactly where it failed" 