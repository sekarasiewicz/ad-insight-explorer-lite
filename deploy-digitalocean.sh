#!/bin/bash

# 🌊 DigitalOcean App Platform Deployment Script
# This script helps deploy the Ad Insight Explorer Lite application to DigitalOcean

set -e

echo "🌊 DigitalOcean App Platform Deployment Script"
echo "================================================"

# Check if doctl is installed
if ! command -v doctl &> /dev/null; then
    echo "❌ DigitalOcean CLI (doctl) not found."
    echo "Please install it from: https://github.com/digitalocean/doctl/releases"
    echo "Or run: brew install doctl (on macOS)"
    exit 1
fi

# Check if user is authenticated
if ! doctl auth list &> /dev/null; then
    echo "🔐 Please authenticate with DigitalOcean..."
    doctl auth init
fi

echo "📋 Prerequisites check completed!"

echo ""
echo "🚀 Starting deployment process..."
echo ""

# Step 1: Create the app
echo "1️⃣ Creating DigitalOcean App..."
echo "   This will create a new app with both backend and frontend services."

# Create the app using the configuration file
doctl apps create --spec .do/app.yaml

echo ""
echo "2️⃣ Getting app information..."

# Get the app ID and URL
APP_ID=$(doctl apps list --format ID,Name --no-header | grep "ad-insight-explorer-lite" | awk '{print $1}')
APP_URL=$(doctl apps get $APP_ID --format Spec.Services[0].Ingress.Rule --no-header)

echo "App ID: $APP_ID"
echo "App URL: $APP_URL"

echo ""
echo "3️⃣ Waiting for deployment to complete..."

# Wait for the app to be deployed
doctl apps wait-for-deployment $APP_ID

echo ""
echo "🎉 Deployment completed successfully!"
echo ""
echo "📱 Your application is now live at:"
echo "   Main App: $APP_URL"
echo "   Backend API: $APP_URL/api"
echo "   API Docs: $APP_URL/docs"
echo ""
echo "🔧 Useful commands:"
echo "   doctl apps logs $APP_ID                    # View app logs"
echo "   doctl apps get $APP_ID                     # Get app details"
echo "   doctl apps create-deployment $APP_ID       # Redeploy app"
echo "   doctl apps delete $APP_ID                  # Delete app"
echo ""
echo "🌐 To add a custom domain:"
echo "   1. Go to DigitalOcean dashboard"
echo "   2. Navigate to your app"
echo "   3. Click 'Settings' → 'Domains'"
echo "   4. Add your custom domain"
echo ""
echo "Happy coding! 🌊✨" 