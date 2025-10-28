# Quick Start Guide

Get the POSS-I Transient Analysis Platform running in 5 minutes.

## Prerequisites

```bash
# Required
✓ Docker 24.0+ and Docker Compose 2.23+
✓ Git
✓ 16GB+ RAM
✓ 50GB+ free disk space

# Optional but recommended
◯ NVIDIA GPU with CUDA 11.8+ (for AI inference)
◯ Node.js 20+ (for local frontend development)
◯ Python 3.10+ (for local backend development)
```

## Installation

### Option 1: Docker (Recommended - Easiest)

```bash
# 1. Clone repository
git clone https://github.com/your-org/poss-transient-platform.git
cd poss-transient-platform

# 2. Copy environment file
cp .env.example .env

# 3. Start everything
docker-compose up -d

# 4. Run database migrations
docker-compose exec backend alembic upgrade head

# 5. (Optional) Load sample data
docker-compose exec backend python scripts/seed_database.py

# 6. Access the application
# Frontend: http://localhost:3000
# Backend API: http://localhost:8000
# API Docs: http://localhost:8000/docs
```

### Option 2: Local Development (For Active Development)

```bash
# Backend
cd backend
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows
pip install -r requirements.txt
alembic upgrade head
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Frontend (in separate terminal)
cd frontend
npm install
npm run dev
```

## Verify Installation

```bash
# Check backend health
curl http://localhost:8000/health

# Check frontend
curl http://localhost:3000

# Check API documentation
open http://localhost:8000/docs  # or visit in browser
```

## First Steps

### 1. Upload Your First Plate

```bash
# Using the API
curl -X POST "http://localhost:8000/api/v1/plates/upload" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@path/to/your/plate.fits"
```

### 2. Run Transient Detection

Visit http://localhost:3000 and:
1. Navigate to "Plates" tab
2. Select your uploaded plate
3. Click "Run Detection"
4. View results when processing completes

### 3. Verify Detections

1. Go to "Verification" tab
2. Review detected transients
3. Mark as accepted/rejected
4. Add notes if needed

## Common Issues

### Docker won't start
```bash
# Check Docker is running
docker ps

# Restart Docker daemon
sudo systemctl restart docker  # Linux
# or restart Docker Desktop (Mac/Windows)
```

### Port already in use
```bash
# Change ports in docker-compose.yml
# Frontend: change 3000:80 to 3001:80
# Backend: change 8000:8000 to 8001:8000
```

### GPU not detected
```bash
# Check NVIDIA drivers
nvidia-smi

# Ensure docker can access GPU
docker run --rm --gpus all nvidia/cuda:11.8.0-base-ubuntu22.04 nvidia-smi
```

### Database migration fails
```bash
# Reset database (WARNING: deletes all data)
docker-compose down -v
docker-compose up -d
docker-compose exec backend alembic upgrade head
```

## Next Steps

- **Understand the system**: Read [01-Architecture.md](01-Architecture.md)
- **Plan development**: Check [03-Development-Phases.md](03-Development-Phases.md)
- **Start coding**: Follow implementation guides in docs/

## Getting Help

- Check logs: `docker-compose logs -f backend`
- Join discussions: [GitHub Discussions](TBD)
- Report issues: [GitHub Issues](TBD)

---

**Ready to build?** Head to [01-Architecture.md](01-Architecture.md) to understand the system design.
