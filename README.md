# Ad Insights Explorer Lite

A recruitment task implementation for analyzing ad content and detecting anomalies using FastAPI backend and React frontend.

## 🎯 Project Overview

This application processes data from the JSONPlaceholder API to identify anomalies in ad content and provide insights through a modern web dashboard.

### Key Features

- **Anomaly Detection**: Identifies short titles, duplicate titles, and bot-like behavior
- **Text Analysis**: Analyzes word frequency and unique words per user
- **Real-time Processing**: Fetches and processes data on-demand from external API
- **Modern Dashboard**: React frontend with filtering, sorting, and visualization
- **Docker Support**: Complete containerization for development and production

## 🏗️ Architecture

- **Backend**: FastAPI (Python 3.13) with anomaly detection and text analysis services
- **Frontend**: React + TypeScript + Vite with shadcn/ui components
- **Data Source**: JSONPlaceholder API (https://jsonplaceholder.typicode.com/posts)
- **Deployment**: Docker Compose for both development and production environments

## 🚀 Quick Start

### Prerequisites

- Docker and Docker Compose
- Node.js 18+ (for local development)
- Python 3.13+ (for local development)

### Running the Application

#### Development Mode
```bash
# Run application with Docker (development)
make run-docker
```

Access the application:
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs

#### Production Mode
```bash
# Run application with Docker (production)
make run-docker-prod
```

Access the application:
- **Frontend**: http://localhost (port 80)
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost/docs

### Local Development

```bash
# Backend (from backend/ directory)
python3.13 -m uvicorn app.main:app --reload --port 8000

# Frontend (from frontend/ directory)
npm run dev
```

## 📊 API Endpoints

### Core Endpoints

```
GET /api/posts/                    # Fetch all posts
GET /api/posts/{user_id}           # Fetch posts by user
GET /api/anomalies/                # Detect and return anomalies
GET /api/anomalies/summary         # Get anomaly summary statistics
GET /api/summary/                  # Get overall data summary
GET /api/summary/word-frequency    # Get most frequent words
GET /api/summary/top-users         # Get top users by unique words
```

### Example Responses

#### Anomalies Response
```json
{
  "anomalies": [
    {
      "userId": 1,
      "id": 1,
      "title": "Short",
      "reason": "short_title",
      "details": "Title length: 5 characters (threshold: 15)"
    }
  ],
  "total": 1,
  "summary": {
    "short_titles": 1,
    "duplicate_titles": 0,
    "bot_like_behavior": 0
  }
}
```

#### Summary Response
```json
{
  "topUsers": [
    {
      "userId": 1,
      "uniqueWordCount": 45,
      "totalPosts": 10,
      "uniqueWords": ["word1", "word2", ...]
    }
  ],
  "mostFrequentWords": [
    {
      "word": "the",
      "count": 150
    }
  ],
  "totalPosts": 100,
  "totalUsers": 10
}
```

## 🔍 Anomaly Detection

The application detects three types of anomalies:

### 1. Short Titles
- **Threshold**: Titles with less than 15 characters
- **Purpose**: Identify potentially incomplete or low-quality content

### 2. Duplicate Titles
- **Detection**: Same user posting identical titles
- **Purpose**: Identify potential spam or automated posting

### 3. Bot-like Behavior
- **Detection**: Users with multiple similar titles (similarity > 80%)
- **Purpose**: Identify automated or bot-generated content

## 📈 Data Analysis Features

### Word Frequency Analysis
- Extracts and counts all words from post titles and bodies
- Filters out common stop words
- Provides top N most frequent words

### User Analysis
- Calculates unique words per user
- Identifies top users by vocabulary diversity
- Tracks posting patterns

### Text Similarity
- Uses SequenceMatcher for title similarity detection
- Configurable similarity threshold (default: 80%)
- Groups similar titles for bot detection

## 🛠️ Development

### Project Structure

```
ad-insight-explorer-lite/
├── backend/
│   ├── app/
│   │   ├── api/routes/           # API endpoints
│   │   ├── services/             # Business logic
│   │   │   ├── anomaly_detector.py
│   │   │   ├── text_analyzer.py
│   │   │   └── jsonplaceholder_service.py
│   │   ├── models.py             # Pydantic models
│   │   └── main.py               # FastAPI app
│   ├── tests/                    # Backend tests
│   └── Dockerfile                # Backend container
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── dashboard/        # Dashboard components
│   │   │   └── ui/               # shadcn/ui components
│   │   ├── services/             # API services
│   │   └── types/                # TypeScript types
│   ├── tests/                    # Frontend tests
│   ├── Dockerfile                # Frontend dev container
│   ├── Dockerfile.prod           # Frontend production container
│   └── Caddyfile                 # Caddy configuration
├── docker-compose.yml            # Development Docker setup
├── docker-compose.prod.yml       # Production Docker setup
└── Makefile                      # Build and run commands
```

### Available Commands

```bash
# Build and run
make build-docker                # Build Docker images
make run-docker                  # Run application with Docker (development)
make run-docker-prod             # Run application with Docker (production)
make stop-docker                 # Stop all containers

# Testing
make test                        # Run frontend tests locally
make test-backend                # Run backend tests locally
make test-coverage               # Run frontend tests with coverage

# Development
make test-watch                  # Run frontend tests in watch mode

# Cleanup
make clean                       # Clean up Docker resources
```

## 🧪 Testing

### Backend Tests ✅
- **Configuration Tests**: Environment variable loading and validation
- **Service Tests**: Anomaly detection and text analysis logic
- **API Tests**: Endpoint functionality and response validation

### Frontend Tests ✅
- **Component Tests**: Dashboard components and UI elements
- **Integration Tests**: API service integration
- **Coverage**: Comprehensive test coverage for critical components

### Running Tests

```bash
# Backend tests
make test-backend

# Frontend tests
make test

# All tests with coverage
make test-coverage
```

## 🚀 Deployment

### Local Docker Deployment

```bash
make run-docker
```

This starts:
- **Backend API**: FastAPI server on port 8000
- **Frontend**: Vite dev server on port 3000
- **All services**: Running in development mode

### DigitalOcean Droplet Deployment (Recommended)

For production deployment, we recommend using a DigitalOcean Droplet for full control and reliability:

1. **Quick Deploy**: Follow the detailed guide in [DROPLET_DEPLOYMENT.md](./DROPLET_DEPLOYMENT.md)

2. **Automated Deployment**: Run the deployment script:
   ```bash
   ./deploy-droplet.sh
   ```

   **Note**: The script requires an existing Droplet. If you don't have one, create it manually:
   ```bash
   doctl compute droplet create ad-insight-explorer --size s-1vcpu-1gb --image ubuntu-22-04-x64 --region nyc1 --ssh-keys <your-ssh-key-id>
   ```

DigitalOcean Droplet provides:
- ✅ Full control over the environment
- ✅ Reliable Docker and Docker Compose deployment
- ✅ Automatic SSL certificates with Let's Encrypt
- ✅ Cost-effective pricing (~$6/month)
- ✅ Easy monitoring and maintenance
- ✅ No build platform restrictions

### DigitalOcean App Platform Deployment (Alternative)

For App Platform deployment, see [DIGITALOCEAN_DEPLOYMENT.md](./DIGITALOCEAN_DEPLOYMENT.md).



### Environment Configuration

The application uses environment variables for configuration:

```bash
# Backend Configuration
SERVER_PORT=8000
SERVER_HOST=0.0.0.0
LOG_LEVEL=INFO

# Analysis Configuration
SHORT_TITLE_THRESHOLD=15
BOT_DETECTION_THRESHOLD=5

# Frontend Configuration
VITE_API_BASE_URL=http://localhost:8000
```

## 📋 Recruitment Task Requirements

This implementation fulfills the following requirements:

### ✅ Backend Requirements
- [x] Python backend (FastAPI)
- [x] Fetch data from JSONPlaceholder API
- [x] Detect anomalies (short titles, duplicates, bot behavior)
- [x] Provide summaries (top users, word frequency)
- [x] RESTful API endpoints
- [x] Docker containerization

### ✅ Frontend Requirements
- [x] React frontend with TypeScript
- [x] Dashboard for data visualization
- [x] Filtering and sorting capabilities
- [x] Modern UI with shadcn/ui components
- [x] Responsive design
- [x] Docker containerization

### ✅ Technical Requirements
- [x] Docker and Docker Compose setup
- [x] Comprehensive testing suite
- [x] Type safety throughout the stack
- [x] Modern development practices
- [x] Clean, maintainable code structure

## 🎯 Key Technical Decisions

### No Database Required
This application is designed as a stateless, real-time data analysis tool that:
- Fetches fresh data on each request
- Processes data in memory
- Provides immediate insights without persistence
- Scales horizontally without data synchronization issues

### Technology Stack
- **Backend**: FastAPI for high-performance async API
- **Frontend**: React 19 with modern hooks and TypeScript
- **UI**: shadcn/ui for consistent, accessible components
- **Testing**: Vitest for frontend, pytest for backend
- **Deployment**: Docker with Caddy for production serving

## 📝 Notes

This project is created for recruitment purposes to demonstrate:
- Full-stack development capabilities
- Modern web development practices
- Docker containerization expertise
- Testing and quality assurance
- API design and implementation
- Frontend development with modern frameworks

The application is production-ready and demonstrates best practices for building scalable, maintainable web applications.