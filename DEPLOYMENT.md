# Deployment Guide

This project uses Docker Hub for deployment to avoid memory constraints on small droplets.

## Prerequisites

1. **Docker Hub Account**: You need a Docker Hub account (username: `sekarasiewicz`)
2. **Docker Login**: Run `docker login` on both your local machine and droplet

## Deployment Process

### Step 1: Build and Push Images (Local Machine)

On your local development machine:

```bash
# Build and push images to Docker Hub
make docker-build-push
```

This will:
- Build both backend and frontend images
- Tag them as `sekarasiewicz/ad-insight-backend:latest`
- Tag them as `sekarasiewicz/ad-insight-frontend:latest`
- Push them to Docker Hub

### Step 2: Deploy on Droplet

On your droplet server:

```bash
# Deploy from Docker Hub images
./deploy-droplet.sh
```

This will:
- Pull the latest images from Docker Hub
- Start the application containers
- Show deployment status and URLs

## Alternative Commands

### Local Development
```bash
# Build and run locally
make run-docker

# Build and run production locally
make run-docker-prod
```

### Droplet Deployment
```bash
# Pull and run from registry
make docker-pull-run

# Or manually:
docker compose -f docker-compose.registry.yml up -d
```

## Management Commands

```bash
# View logs
docker compose -f docker-compose.registry.yml logs -f

# Stop application
docker compose -f docker-compose.registry.yml down

# Restart application
docker compose -f docker-compose.registry.yml restart

# Update to latest images
docker compose -f docker-compose.registry.yml pull
docker compose -f docker-compose.registry.yml up -d
```

## Benefits of This Approach

1. **No Memory Issues**: Droplet doesn't need to build images
2. **Fast Deployment**: Just pulls pre-built images
3. **Consistent Builds**: Same images everywhere
4. **Easy Updates**: Just push new images and pull on droplet

## Troubleshooting

### If images don't exist on Docker Hub:
```bash
# Build and push first
make docker-build-push
```

### If deployment fails:
```bash
# Check Docker Hub login
docker login

# Check available images
docker images

# Clean up and retry
docker system prune -f
./deploy-droplet.sh
```

## Docker Hub Images

The following images are available on Docker Hub:
- `sekarasiewicz/ad-insight-backend:latest`
- `sekarasiewicz/ad-insight-frontend:latest`

You can view them at: https://hub.docker.com/r/sekarasiewicz/ 