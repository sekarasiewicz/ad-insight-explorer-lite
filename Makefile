.PHONY: help build-docker run-docker run-docker-prod stop-docker clean test test-watch test-coverage test-backend

help: ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Targets:'
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  %-15s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

build-docker: ## Build Docker images
	docker compose build

run-docker: ## Run application with Docker (development)
	docker compose up --build

run-docker-prod: ## Run application with Docker (production)
	docker compose -f docker-compose.prod.yml up --build -d

stop-docker: ## Stop Docker containers
	docker compose down
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