.PHONY: help install dev build up down logs restart clean test lint format migrate db-upgrade db-downgrade

help:
	@echo "Transient Analysis Platform - Development Commands"
	@echo ""
	@echo "Setup Commands:"
	@echo "  make install        - Install all dependencies"
	@echo "  make dev            - Start development environment"
	@echo ""
	@echo "Docker Commands:"
	@echo "  make up             - Start all services with docker-compose"
	@echo "  make down           - Stop all services"
	@echo "  make restart        - Restart all services"
	@echo "  make logs           - View logs (use SERVICE=backend for specific service)"
	@echo "  make build          - Rebuild Docker images"
	@echo ""
	@echo "Database Commands:"
	@echo "  make migrate        - Create new migration"
	@echo "  make db-upgrade     - Apply all migrations"
	@echo "  make db-downgrade   - Revert last migration"
	@echo ""
	@echo "Development Commands:"
	@echo "  make test           - Run all tests"
	@echo "  make lint           - Lint code"
	@echo "  make format         - Format code"
	@echo "  make clean          - Clean build artifacts"

install:
	@echo "Installing dependencies..."
	cd frontend && npm install
	cd backend && pip install -r requirements-dev.txt

dev:
	@echo "Starting development environment..."
	docker-compose up

up:
	@echo "Starting services..."
	docker-compose up -d
	@echo "Services started!"
	@echo "Frontend: http://localhost:3000"
	@echo "Backend: http://localhost:8000"
	@echo "API Docs: http://localhost:8000/docs"

down:
	@echo "Stopping services..."
	docker-compose down

restart:
	@echo "Restarting services..."
	docker-compose restart

logs:
ifdef SERVICE
	docker-compose logs -f $(SERVICE)
else
	docker-compose logs -f
endif

build:
	@echo "Building Docker images..."
	docker-compose build

migrate:
	@echo "Creating new migration..."
	cd backend && alembic revision --autogenerate -m "$(MSG)"

db-upgrade:
	@echo "Applying migrations..."
	docker-compose exec backend alembic upgrade head

db-downgrade:
	@echo "Reverting last migration..."
	docker-compose exec backend alembic downgrade -1

test:
	@echo "Running tests..."
	cd backend && pytest
	cd frontend && npm test

lint:
	@echo "Linting code..."
	cd backend && flake8 app/
	cd frontend && npm run lint

format:
	@echo "Formatting code..."
	cd backend && black app/ && isort app/
	cd frontend && npm run format

clean:
	@echo "Cleaning build artifacts..."
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	rm -rf frontend/dist
	rm -rf frontend/node_modules
	rm -rf backend/.pytest_cache
	rm -rf backend/htmlcov
	@echo "Clean complete!"
