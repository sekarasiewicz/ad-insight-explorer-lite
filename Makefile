.PHONY: help build-docker run-docker stop-docker clean test test-watch test-coverage test-backend build-docker-prod run-docker-prod stop-docker-prod docker-build-push docker-pull-run docker-login deploy-simple

help: ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Targets:'
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  %-15s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

build-docker: ## Build Docker images (development)
	docker compose build

run-docker: ## Run application with Docker (development)
	docker compose up --build

stop-docker: ## Stop Docker containers (development)
	docker compose down

build-docker-prod: ## Build Docker images for prod/production
	docker compose -f docker-compose.prod.yml build

run-docker-prod: ## Run application with Docker for prod/production
	docker compose -f docker-compose.prod.yml up --build -d

stop-docker-prod: ## Stop Docker containers for prod/production
	docker compose -f docker-compose.prod.yml down

docker-login: ## Login to Docker Hub
	@echo "Please login to Docker Hub:"
	docker login

docker-build-push: ## Build and push images to Docker Hub
	@echo "Building and pushing images to Docker Hub..."
	@echo "Make sure you're logged in with: make docker-login"
	docker build -t ad-insight-backend:latest ./backend
	docker build -t ad-insight-frontend:latest ./frontend
	@echo "✅ Images built successfully!"
	@echo "To push to your registry, run:"
	@echo "  docker tag ad-insight-backend:latest YOUR_USERNAME/ad-insight-backend:latest"
	@echo "  docker tag ad-insight-frontend:latest YOUR_USERNAME/ad-insight-frontend:latest"
	@echo "  docker push YOUR_USERNAME/ad-insight-backend:latest"
	@echo "  docker push YOUR_USERNAME/ad-insight-frontend:latest"

docker-pull-run: ## Pull images from Docker Hub and run
	@echo "Pulling images from Docker Hub and running..."
	docker compose -f docker-compose.registry.yml up -d
	@echo "✅ Application running from Docker Hub images!"

deploy-simple: ## Deploy with backend from registry, frontend built locally
	@echo "Deploying with simple approach..."
	./deploy-simple.sh

clean: ## Clean up generated files
	docker system prune -f

test: ## Run frontend tests locally
	cd frontend && npm test

test-watch: ## Run frontend tests locally with watch mode
	cd frontend && npm run test:watch

test-coverage: ## Run frontend tests with coverage
	cd frontend && npm run test:coverage

test-backend: ## Run backend tests locally
	cd backend && ./venv/bin/python3.13 -m pytest tests/ -v