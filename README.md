# Transient Analysis Platform

AI-powered web application for verification of historical astronomical transients from POSS-I sky survey (1949-1957).

## Table of Contents

- [Overview](#overview)
- [Quick Start](#quick-start)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [First-Time Setup](#first-time-setup)
- [Development](#development)
  - [Project Structure](#project-structure)
  - [Common Commands](#common-commands)
  - [Tech Stack](#tech-stack)
- [Documentation](#documentation)
- [Current Status](#current-status)
- [Scientific Context](#scientific-context)
- [Contributing](#contributing)
  - [Development Workflow](#development-workflow)
- [Testing](#testing)
- [License](#license)
- [Acknowledgments](#acknowledgments)
- [Contact](#contact)
- [Roadmap](#roadmap)

## Overview

This platform enables independent verification of groundbreaking research linking astronomical transients with nuclear weapons testing and UAP reports. Using AI-powered detection (YOLOv8) combined with manual verification, researchers can reproduce published findings from *Nature Scientific Reports*.

**Key Features:**
- Upload and analyze POSS-I FITS files
- AI-powered transient detection using YOLOv8
- Manual verification interface with catalog cross-matching
- Statistical analysis and correlation tools
- Export results for further research

## Quick Start

### Prerequisites

- Docker Desktop (Windows, macOS, or Linux)
- Git

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/Davenads/VASCO-Verify.git
cd VASCO-Verify
```

2. **Copy environment configuration:**
```bash
cp .env.example .env
```

3. **Start the application:**
```bash
make up
```

Or using docker-compose directly:
```bash
docker-compose up -d
```

4. **Access the application:**
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Documentation: http://localhost:8000/docs

### First-Time Setup

Initialize the database:
```bash
# Using Docker
docker-compose exec backend alembic upgrade head

# Or run the init script
python scripts/init_db.py
```

## Development

### Project Structure

```
transient-analysis-platform/
├── frontend/          # React + TypeScript + Vite
├── backend/           # FastAPI + Python
├── ml/                # Machine learning training
├── data/              # Data storage (gitignored)
├── scripts/           # Utility scripts
├── context/           # Documentation
└── docker-compose.yml
```

### Common Commands

```bash
# Start development environment
make dev

# View logs
make logs

# Run tests
make test

# Apply database migrations
make db-upgrade

# Format code
make format

# Stop services
make down
```

### Tech Stack

**Frontend:**
- React 18+
- TypeScript
- Vite
- Tailwind CSS
- Zustand (state management)
- Axios

**Backend:**
- FastAPI
- Python 3.11+
- SQLAlchemy + Alembic
- SQLite (development) / PostgreSQL (production)

**AI/ML:**
- PyTorch 2.1+
- YOLOv8 (Ultralytics)
- OpenCV
- Astropy

**Deployment:**
- Docker Compose
- GitHub Actions (CI/CD)

## Documentation

Comprehensive documentation is available in the `context/` directory:

- [Quick Start Guide](context/00-Quick-Start.md)
- [Architecture Overview](context/01-Architecture.md)
- [Project Structure](context/02-Project-Structure.md)
- [Development Phases](context/03-Development-Phases.md)
- [Backend API Reference](context/04-Backend-API.md)
- [Commands Reference](context/13-Commands-Reference.md)

## Current Status

**Phase:** Phase 1 - Foundation (Week 1-2)
**Status:** ✅ Setup Complete

**Completed:**
- [x] Project structure initialized
- [x] Docker development environment
- [x] FastAPI backend with health endpoint
- [x] React + TypeScript frontend
- [x] Tailwind CSS styling
- [x] Database schema design
- [x] Alembic migrations setup

**Next Steps:**
- [ ] FITS file upload and processing (Week 3-4)
- [ ] Image viewer with pan/zoom
- [ ] AI model integration (Week 5-8)

## Scientific Context

This platform is based on research published in *Scientific Reports* (Nature) that identified:
- 107,875 transients in POSS-I images
- 45% increase in transients within ±1 day of nuclear tests
- 8.5% increase per additional UAP report
- Statistically significant correlations (p < 0.05)

**Research Paper:**
[Transients in POSS-I may be associated with nuclear testing and UAP reports](https://www.nature.com/articles/s41598-025-21620-3)

## Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) before submitting pull requests.

### Development Workflow

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Testing

Run the test suite:

```bash
# Backend tests
cd backend && pytest

# Frontend tests
cd frontend && npm test

# All tests
make test
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- VASCO Project for pioneering research on vanishing astronomical sources
- Nature Scientific Reports for publishing the foundational research
- Palomar Observatory for the POSS-I sky survey data
- Open-source community for the incredible tools that made this possible

## Contact

- **GitHub Issues:** [Create an issue](https://github.com/Davenads/VASCO-Verify/issues)
- **Discussions:** [GitHub Discussions](https://github.com/Davenads/VASCO-Verify/discussions)

## Roadmap

- **v1.0 (Week 14):** MVP with full detection and verification pipeline
- **v1.1:** Performance optimizations and additional catalog sources
- **v2.0:** Multi-user support, cloud deployment, POSS-II integration
- **v3.0:** Advanced ML features, API access, community features

---

**Built with:** 🔭 Astronomy • 🤖 AI • 🔬 Science • 💻 Open Source
