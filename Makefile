.PHONY: help build-docker run-docker stop-docker clean test test-watch test-coverage test-backend build-docker-prod run-docker-prod stop-docker-prod

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