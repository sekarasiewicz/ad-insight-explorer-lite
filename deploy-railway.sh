#!/bin/bash

# 🚂 Railway Deployment Script for Ad Insight Explorer Lite
# This script helps automate the deployment process to Railway

set -e

echo "🚂 Railway Deployment Script"
echo "=============================="

# Check if Railway CLI is installed
if ! command -v railway &> /dev/null; then
    echo "❌ Railway CLI not found. Installing..."
    npm install -g @railway/cli
fi

# Check if user is logged in
if ! railway whoami &> /dev/null; then
    echo "🔐 Please login to Railway..."
    railway login
fi

echo "📋 Prerequisites check completed!"

echo ""
echo "🚀 Starting deployment process..."
echo ""

# Create new project (if not exists)
echo "1️⃣ Creating Railway project..."
railway init

# Deploy backend service
echo "2️⃣ Deploying backend service..."
railway up --service backend

# Get backend URL
echo "3️⃣ Getting backend service URL..."
BACKEND_URL=$(railway domain --service backend)
echo "Backend URL: $BACKEND_URL"

# Set frontend environment variable
echo "4️⃣ Configuring frontend service..."
railway variables set BACKEND_URL=$BACKEND_URL --service frontend

# Deploy frontend service
echo "5️⃣ Deploying frontend service..."
railway up --service frontend

# Get frontend URL
echo "6️⃣ Getting frontend service URL..."
FRONTEND_URL=$(railway domain --service frontend)
echo "Frontend URL: $FRONTEND_URL"

echo ""
echo "🎉 Deployment completed successfully!"
echo ""
echo "📱 Your application is now live at:"
echo "   Frontend: $FRONTEND_URL"
echo "   Backend API: $BACKEND_URL"
echo "   API Docs: $BACKEND_URL/docs"
echo ""
echo "🔧 Useful commands:"
echo "   railway logs --service backend    # View backend logs"
echo "   railway logs --service frontend   # View frontend logs"
echo "   railway open --service frontend   # Open frontend in browser"
echo "   railway status                    # Check service status"
echo ""
echo "Happy coding! 🚂✨" 