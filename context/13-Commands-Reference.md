# Commands Reference

Quick reference for common development operations.

## Docker Commands

### Start/Stop Services
```bash
# Start all services
docker-compose up -d

# Stop all services
docker-compose down

# Restart a service
docker-compose restart backend

# View logs
docker-compose logs -f backend
docker-compose logs -f frontend

# Shell into container
docker-compose exec backend bash
docker-compose exec frontend sh
```

### Build & Cleanup
```bash
# Rebuild containers
docker-compose build --no-cache

# Remove containers and volumes
docker-compose down -v

# Remove images
docker-compose down --rmi all

# Clean everything
docker system prune -a
```

## Database Commands

### Migrations
```bash
# Create new migration
docker-compose exec backend alembic revision -m "description"

# Run migrations
docker-compose exec backend alembic upgrade head

# Rollback one migration
docker-compose exec backend alembic downgrade -1

# Show current revision
docker-compose exec backend alembic current

# Show migration history
docker-compose exec backend alembic history
```

### Database Operations
```bash
# Seed database
docker-compose exec backend python scripts/seed_database.py

# Backup database
docker-compose exec backend sqlite3 /app/data/transient.db ".backup '/app/data/backup.db'"

# Restore database
docker-compose exec backend sqlite3 /app/data/transient.db ".restore '/app/data/backup.db'"

# Access database directly
docker-compose exec backend sqlite3 /app/data/transient.db
```

## Development Commands

### Backend
```bash
# Start backend locally
cd backend
source venv/bin/activate
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Run tests
pytest
pytest tests/test_api/  # specific directory
pytest -v  # verbose
pytest --cov=app  # with coverage

# Lint
flake8 app/
black app/ --check
isort app/ --check

# Format
black app/
isort app/
```

### Frontend
```bash
# Start frontend locally
cd frontend
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview

# Run tests
npm test
npm run test:watch
npm run test:coverage

# Lint
npm run lint
npm run lint:fix

# Type check
npm run type-check
```

## AI/ML Commands

### Training
```bash
# Train model
cd ml
python train.py

# Resume training from checkpoint
python train.py --resume runs/detect/exp/weights/last.pt

# Evaluate model
python evaluate.py --model runs/detect/exp/weights/best.pt

# Export model
python export_model.py --model best.pt --format onnx
```

### TensorBoard
```bash
# View training metrics
tensorboard --logdir ml/runs/detect

# View in browser: http://localhost:6006
```

## Data Commands

### Download Sample Data
```bash
# Download POSS-I plates
python scripts/download_data.py --survey poss_i --count 10

# Download catalog data
python scripts/download_data.py --catalog panstarrs --region "180.5 45.2 15.0"
```

### Process Data
```bash
# Batch process plates
python scripts/batch_process.py --input data/plates/ --output data/processed/

# Generate training dataset
python ml/prepare_dataset.py --input data/raw/ --output ml/data/processed/
```

## Testing Commands

### Run All Tests
```bash
# Backend
cd backend && pytest

# Frontend
cd frontend && npm test

# Integration tests
pytest tests/integration/

# E2E tests
pytest tests/e2e/
```

### Coverage
```bash
# Backend coverage
pytest --cov=app --cov-report=html
open htmlcov/index.html

# Frontend coverage
npm run test:coverage
open coverage/index.html
```

## Git Commands

### Workflow
```bash
# Create feature branch
git checkout -b feature/detection-ui

# Stage and commit
git add .
git commit -m "feat: add detection review interface"

# Push to remote
git push origin feature/detection-ui

# Update from main
git checkout main
git pull origin main
git checkout feature/detection-ui
git rebase main
```

### Commit Message Convention
```
feat: Add new feature
fix: Fix bug
docs: Update documentation
test: Add tests
refactor: Refactor code
perf: Performance improvement
chore: Maintenance task
```

## Makefile Commands

If you create a `Makefile` in the root:

```bash
# Start development
make dev

# Run all tests
make test

# Lint all code
make lint

# Format all code
make format

# Build for production
make build

# Deploy
make deploy

# Clean build artifacts
make clean
```

Example `Makefile`:
```makefile
.PHONY: dev test lint format build deploy clean

dev:
	docker-compose up -d

test:
	cd backend && pytest
	cd frontend && npm test

lint:
	cd backend && flake8 app/
	cd frontend && npm run lint

format:
	cd backend && black app/ && isort app/
	cd frontend && npm run lint:fix

build:
	docker-compose build

deploy:
	./scripts/deploy.sh

clean:
	docker-compose down -v
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type d -name node_modules -exec rm -rf {} +
```

## Utility Scripts

### Environment Setup
```bash
# Setup development environment
./scripts/setup_env.sh

# Install dependencies
cd backend && pip install -r requirements.txt
cd frontend && npm install
```

### Health Checks
```bash
# Check backend
curl http://localhost:8000/health

# Check frontend
curl http://localhost:3000

# Check all services
./scripts/health_check.sh
```

## Production Commands

### Deployment
```bash
# Build production images
docker-compose -f docker-compose.prod.yml build

# Deploy to server
ssh user@production-server "cd /opt/app && docker-compose pull && docker-compose up -d"

# View production logs
ssh user@production-server "docker-compose logs -f"
```

### Monitoring
```bash
# Check container stats
docker stats

# View resource usage
docker-compose exec backend ps aux
docker-compose exec backend free -h
docker-compose exec backend df -h
```

## Troubleshooting Commands

### Reset Everything
```bash
# Nuclear option - reset to clean state
docker-compose down -v
rm -rf data/
rm -rf ml/data/models/*.pt
git clean -fdx  # WARNING: removes all untracked files
docker-compose up -d
docker-compose exec backend alembic upgrade head
docker-compose exec backend python scripts/seed_database.py
```

### Check GPU
```bash
# Verify GPU is available
nvidia-smi

# Check CUDA in Docker
docker run --rm --gpus all nvidia/cuda:11.8.0-base-ubuntu22.04 nvidia-smi

# Test PyTorch GPU
docker-compose exec backend python -c "import torch; print(torch.cuda.is_available())"
```

### Debug Containers
```bash
# Check container status
docker-compose ps

# Inspect container
docker inspect poss-backend

# View container logs
docker logs poss-backend --tail 100 -f

# Check port bindings
docker port poss-backend
```

## Quick Fixes

### Port Already in Use
```bash
# Find process using port
lsof -i :8000  # macOS/Linux
netstat -ano | findstr :8000  # Windows

# Kill process
kill -9 <PID>

# Or change port in docker-compose.yml
```

### Permission Errors
```bash
# Fix file permissions
sudo chown -R $USER:$USER .
chmod -R 755 .
```

### Module Not Found
```bash
# Reinstall dependencies
cd backend && pip install -r requirements.txt
cd frontend && rm -rf node_modules && npm install
```

---

**Tip**: Add commonly used commands to your shell aliases in `~/.bashrc` or `~/.zshrc`:

```bash
alias dcu="docker-compose up -d"
alias dcd="docker-compose down"
alias dcl="docker-compose logs -f"
alias dcr="docker-compose restart"
alias dcb="docker-compose build"
```
