# FastAPI React Kit

A simple template for FastAPI and React projects with Docker support.

## Features

- **Simple API**: FastAPI backend with a Hello World endpoint
- **Modern Frontend**: React + TypeScript with Vite
- **Docker Support**: Development and production environments
- **Testing**: Unit tests for both backend and frontend
- **Type Safety**: Full TypeScript support

## Architecture

- **Backend**: FastAPI (Python) with simple REST endpoints
- **Frontend**: React + TypeScript + Vite
- **Deployment**: Docker Compose for both dev and prod environments

## Quick Start

### Prerequisites

- Docker
- Docker Compose

### Running the Application

#### Development Mode

```bash
# Run development environment with Docker
make run-docker-dev
```

#### Production Mode

```bash
# Run production environment with Docker
make run-docker-prod
```

### API Documentation

Once the backend is running, visit:
- **Interactive API Docs**: http://localhost:8000/docs
- **Alternative API Docs**: http://localhost:8000/redoc

## API Endpoints

### Hello World Endpoint

```
GET /api/hello
```

**Response:**
```json
{
  "message": "Hello, World!"
}
```

### Root Endpoint

```
GET /
```

**Response:**
```json
{
  "message": "FastAPI React Kit API",
  "version": "1.0.0",
  "docs": "/docs"
}
```

### Health Check

```
GET /health
```

Returns: `{"status": "healthy"}`

## Configuration

The backend supports environment variables for configuration.

### Environment Variables

Environment variables can be set in several ways:

#### 1. `.env` file (Recommended for Docker Compose)

Create a `.env` file in the project root (copy from `.env.example`):

```bash
# Backend Configuration
SERVER_PORT=8000
SERVER_HOST=0.0.0.0
LOG_LEVEL=INFO

# Frontend Configuration
VITE_API_URL=http://localhost:8000

# Development overrides (uncomment to use)
# LOG_LEVEL=DEBUG
# SERVER_PORT=9000
# VITE_API_URL=http://localhost:9000
```

#### 2. System Environment Variables

You can also set environment variables directly:

```bash
# Server Configuration
SERVER_PORT=8000
SERVER_HOST=0.0.0.0

# Logging Configuration  
LOG_LEVEL=INFO  # Options: DEBUG, INFO, WARNING, ERROR, CRITICAL
```

### Docker Environment

Environment variables are automatically set in Docker Compose files:
- **Development**: `docker-compose.dev.yml` (LOG_LEVEL=DEBUG)
- **Production**: `docker-compose.prod.yml` (LOG_LEVEL=INFO)  
- **Testing**: `docker-compose.test.yml` (LOG_LEVEL=DEBUG)

## Development

### Project Structure

```
fastapi-react-kit/
├── backend/
│   ├── app/
│   │   ├── utils/
│   │   ├── main.py
│   │   ├── models.py
│   │   └── config.py
│   └── tests/
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── services/
│   │   └── types/
│   └── src/__tests__/
├── docker-compose.dev.yml
├── docker-compose.prod.yml
└── Makefile
```

### Docker Commands

```bash
# Build Docker images
make build-docker

# Stop Docker containers
make stop-docker

# Clean up
make clean
```

### Custom Environment Variables

You can override environment variables directly when running the Makefile targets:

```bash
# Override any environment variable
SERVER_PORT=9000 LOG_LEVEL=DEBUG make run-docker-dev
```

## Testing

### Backend Tests ✅
- **Configuration**: Tests for settings and environment variable loading
- **API Endpoints**: Tests for Hello World and health endpoints

### Frontend Tests ⚠️
- **Component Tests**: Require DOM environment
  - ColorModeButton component
  - UI components

## Deployment

### Production Docker

```bash
make run-docker-prod
```

This starts:
- Backend API on port 8000
- Frontend served by Caddy on port 80
- All services in production mode

### Environment Variables

For production deployment, you can override the default environment variables:

```bash
# Override default settings
export SERVER_PORT=9000
export LOG_LEVEL=ERROR

# Then run with custom settings
make run-docker-prod
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Run the test suite
6. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

The MIT License is a permissive license that allows for:
- Commercial use
- Modification
- Distribution
- Private use

The only requirement is that the license and copyright notice be included in all copies or substantial portions of the software.