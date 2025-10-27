# POSS-I Transient Analysis Platform - AI Assistant Context

**Project Name**: VASCO Verify / OpenTransient (TBD)  
**Purpose**: AI-powered web application for public verification of historical astronomical transients  
**Status**: Pre-development / Planning Phase  
**Target**: MVP in 14 weeks

---

## Quick Context for AI Assistants

This is a platform that enables anyone to:
1. **Upload** historical sky survey images (POSS-I FITS files from 1949-1957)
2. **Detect** transient phenomena using AI (YOLOv8-based detection)
3. **Verify** detections through manual review interface
4. **Analyze** correlations with nuclear weapons tests and UAP reports
5. **Reproduce** published scientific findings from Nature Scientific Reports

**Key Goal**: Democratize verification of groundbreaking research linking astronomical transients with nuclear testing and UAP sightings.

---

## Documentation Structure

All supporting documentation is located in the `context/` folder at the project root.

### Start Here
- **[context/docs/README.md](context/docs/README.md)** - Documentation index and navigation hub

### Essential Reading (in order)
1. **[context/docs/00-Quick-Start.md](context/docs/00-Quick-Start.md)** - Installation & setup (5 min)
2. **[context/docs/01-Architecture.md](context/docs/01-Architecture.md)** - System design, tech stack, principles
3. **[context/docs/02-Project-Structure.md](context/docs/02-Project-Structure.md)** - File/folder organization
4. **[context/docs/03-Development-Phases.md](context/docs/03-Development-Phases.md)** - 14-week roadmap with tasks

### Reference Documentation
- **[context/docs/04-Backend-API.md](context/docs/04-Backend-API.md)** - API endpoints, request/response formats
- **[context/docs/13-Commands-Reference.md](context/docs/13-Commands-Reference.md)** - Common commands & operations

### Additional Context
- **[context/DOCUMENTATION-SUMMARY.md](context/DOCUMENTATION-SUMMARY.md)** - Overview of documentation structure
- **[context/poss-i-analysis-platform-proposal.md](context/poss-i-analysis-platform-proposal.md)** - Formal proposal for researchers
- **[context/app-names.md](context/app-names.md)** - Potential names for the platform
- **[context/technical-build-reference.md](context/technical-build-reference.md)** - Original comprehensive reference (archived)

---

## Tech Stack Summary

```
Frontend:  React 18+ | TypeScript | Vite | Tailwind CSS | Zustand
Backend:   FastAPI | Python 3.10+ | SQLAlchemy | SQLite→PostgreSQL
AI/ML:     PyTorch 2.1+ | YOLOv8 | OpenCV | Astropy
Deploy:    Docker Compose | GitHub Actions
```

---

## Architecture Overview

```
Browser (React/TS) 
    ↕ REST API
Backend (FastAPI/Python)
    ├─ AI/ML (PyTorch + YOLOv8)
    ├─ Database (SQLite)
    └─ File Storage (FITS files)
    ↕ External APIs
External Services (DSS, PanSTARRS, Gaia)
```

**Key Principles:**
- **Local-first**: Runs on user's machine (no cloud required)
- **API-first**: Backend exposes RESTful API
- **Container-based**: Docker for reproducibility
- **Progressive enhancement**: Works on CPU, optimized for GPU

---

## Project Structure (High-Level)

```
poss-transient-platform/
├── frontend/           # React TypeScript app
│   └── src/
│       ├── components/  # UI components
│       ├── pages/       # Route pages
│       ├── services/    # API client
│       └── stores/      # State management
│
├── backend/            # FastAPI Python app
│   └── app/
│       ├── api/         # Route definitions
│       ├── core/        # Business logic
│       ├── db/          # Database models
│       ├── ml/          # AI/ML code
│       └── services/    # Service layer
│
├── ml/                 # Training & experiments
│   ├── train.py
│   ├── evaluate.py
│   └── data/
│
├── docs/               # Documentation (YOU ARE HERE)
├── data/               # Storage (gitignored)
└── scripts/            # Utility scripts
```

**Full structure**: See [context/docs/02-Project-Structure.md](context/docs/02-Project-Structure.md)

---

## Development Workflow

### Getting Started
```bash
# Clone repo
git clone <repo-url>
cd poss-transient-platform

# Start services
docker-compose up -d

# Run migrations
docker-compose exec backend alembic upgrade head

# Access app
# Frontend: http://localhost:3000
# Backend: http://localhost:8000/docs
```

### Common Tasks
```bash
# View logs
docker-compose logs -f backend

# Run tests
cd backend && pytest
cd frontend && npm test

# Format code
cd backend && black app/ && isort app/
cd frontend && npm run lint:fix
```

**Full commands**: See [context/docs/13-Commands-Reference.md](context/docs/13-Commands-Reference.md)

---

## Current Development Phase

**Phase 1: Foundation (Weeks 1-4)**

**Priority Tasks:**
- [ ] Set up Docker development environment
- [ ] Create FastAPI backend with health endpoint
- [ ] Create React frontend with routing
- [ ] Implement FITS file loading (Astropy)
- [ ] Build basic image viewer
- [ ] Create database schema

**Next Phase**: AI Integration (Weeks 5-8)

**Full roadmap**: See [context/docs/03-Development-Phases.md](context/docs/03-Development-Phases.md)

---

## AI/ML Context

**Objective**: Train YOLOv8 to detect transient objects in historical sky survey images

**Transient Definition**: 
- Point-like objects appearing in one image but NOT in:
  - Reference images taken before
  - All subsequent modern surveys (PanSTARRS, Gaia)
- Duration: <50 minutes (single exposure)

**Training Data Needs:**
- Positive examples: Verified transients from VASCO project (to be requested)
- Negative examples: Artifacts, cosmic rays, known stars
- Data augmentation: Rotation, brightness, noise

**Performance Targets:**
- Precision: ≥85%
- Recall: ≥80%
- Inference speed: <3 seconds per plate (GPU)

**Model Architecture**: YOLOv8 nano/small with transfer learning

---

## Scientific Context

**Research Paper**: 
[Transients in POSS-I may be associated with nuclear testing and UAP reports](https://www.nature.com/articles/s41598-025-21620-3)  
*Scientific Reports* (Nature), 2025

**Key Findings:**
- 107,875 transients identified in POSS-I (1949-1957)
- Transients **45% more likely** on dates within ±1 day of nuclear tests
- **8.5% increase** in transients for each additional UAP report
- Associations are **statistically significant** (p < 0.05)

**This Platform's Purpose**: 
Enable independent verification of these findings through transparent, reproducible AI analysis.

---

## Code Style & Standards

### Python (Backend)
- **Formatter**: Black (line length 100)
- **Import sorting**: isort
- **Linting**: flake8
- **Type hints**: Required for public functions
- **Docstrings**: Google style
- **Testing**: pytest with ≥80% coverage

### TypeScript (Frontend)
- **Formatter**: Prettier
- **Linting**: ESLint + TypeScript strict mode
- **Style**: Functional components, React Hooks
- **State**: Zustand (lightweight)
- **Testing**: Vitest + React Testing Library

### Commit Messages
```
feat: Add new feature
fix: Fix bug
docs: Update documentation
test: Add tests
refactor: Refactor code
perf: Performance improvement
chore: Maintenance
```

**Full standards**: See [context/docs/11-Code-Standards.md](context/docs/11-Code-Standards.md) (to be created)

---

## API Quick Reference

**Base URL**: `http://localhost:8000/api/v1`

**Key Endpoints:**
```
POST /plates/upload          # Upload FITS file
GET  /plates/{id}            # Get plate details
POST /detections/run         # Run AI detection
GET  /detections/{id}        # Get detection
POST /verifications          # Submit verification
POST /analysis/chi-square    # Run statistical test
POST /export/csv             # Export results
```

**Full API docs**: See [context/docs/04-Backend-API.md](context/docs/04-Backend-API.md)

---

## Key Modules Overview

| Module | Location | Purpose |
|--------|----------|---------|
| Image Processing | `backend/app/core/image_processor.py` | FITS loading, preprocessing, difference imaging |
| AI Detection | `backend/app/ml/inference.py` | YOLOv8 inference, confidence scoring |
| Catalog Query | `backend/app/core/catalog_query.py` | PanSTARRS/Gaia cross-matching |
| Statistics | `backend/app/core/statistics.py` | Chi-square, Mann-Whitney U, GLM |
| Verification | `backend/app/services/verification_service.py` | User annotations, consensus |
| Plate Viewer | `frontend/src/components/image/PlateViewer.tsx` | Interactive image display |
| Detection Review | `frontend/src/components/detection/DetectionReview.tsx` | Manual verification UI |

---

## Domain-Specific Knowledge

### Astronomy Terms
- **FITS**: Flexible Image Transport System (astronomical image format)
- **POSS**: Palomar Observatory Sky Survey
- **PSF**: Point Spread Function (how stars appear in images)
- **WCS**: World Coordinate System (sky position mapping)
- **RA/Dec**: Right Ascension / Declination (celestial coordinates)

### Survey Catalogs
- **PanSTARRS DR1**: Modern optical survey (2010s)
- **Gaia DR3**: European space mission, precise stellar positions
- **DSS**: Digitized Sky Survey (scanned photographic plates)

### Scientific Methodology
- **Chi-square test**: Association between categorical variables
- **Mann-Whitney U**: Non-parametric comparison of groups
- **Spearman correlation**: Rank-based correlation
- **GLM**: Generalized Linear Model for count data

---

## Important Constraints

### What to Avoid
- NO Authentication in MVP (local deployment only)
- NO Real-time features in MVP (WebSockets - future)
- NO Multi-user features in MVP (single-user first)
- NO Advanced ML techniques (keep it simple - YOLOv8 is enough)
- NO Blockchain/crypto anything (not relevant)

### What to Prioritize
- YES Reproducibility (exact results every time)
- YES Transparency (visible AI decision-making)
- YES Documentation (explain everything)
- YES Performance (fast inference on consumer GPUs)
- YES Simplicity (easy setup, clear UX)

---

## Known Challenges & Solutions

### Challenge: Limited Training Data
**Solution**: Use transfer learning (pretrained YOLOv8) + data augmentation + synthetic examples

### Challenge: FITS Files Are Large
**Solution**: Stream processing, thumbnail generation, progressive loading

### Challenge: Cross-Catalog Matching Slow
**Solution**: Implement caching, async queries, rate limiting

### Challenge: Statistical Reproducibility
**Solution**: Fixed random seeds, deterministic algorithms, version pinning

---

## When Helping with Code

### Always Consider:
1. **Is this in the MVP scope?** (Check Phase 1-5 in development roadmap)
2. **Does it follow the tech stack?** (No unnecessary dependencies)
3. **Is it testable?** (Include tests or test strategy)
4. **Is it documented?** (Add comments, update docs)
5. **Is it reproducible?** (Deterministic, version-locked)

### Code Review Checklist:
- [ ] Follows style guide (Black/Prettier formatted)
- [ ] Has type hints/types (Python/TypeScript)
- [ ] Includes tests
- [ ] Updates documentation if needed
- [ ] No hardcoded credentials or secrets
- [ ] Handles errors gracefully
- [ ] Considers performance (especially for AI inference)

---

## Getting Help

### Documentation
1. **First**: Check [context/docs/README.md](context/docs/README.md) for relevant doc
2. **Stuck?**: Read [context/docs/13-Commands-Reference.md](context/docs/13-Commands-Reference.md)
3. **Architecture questions?**: See [context/docs/01-Architecture.md](context/docs/01-Architecture.md)

### External Resources
- **FastAPI**: https://fastapi.tiangolo.com/
- **React**: https://react.dev/
- **YOLOv8**: https://docs.ultralytics.com/
- **Astropy**: https://docs.astropy.org/
- **Scientific Paper**: https://www.nature.com/articles/s41598-025-21620-3

---

## Success Metrics (for AI to optimize for)

### Technical
- **AI Precision**: ≥85%
- **AI Recall**: ≥80%
- **Inference Speed**: <3 sec/plate (GPU)
- **API Response**: <100ms (simple queries)
- **Test Coverage**: ≥80%

### Scientific
- **Reproducibility**: Match paper results within 5%
- **Verifications**: Enable 10+ detections/minute review speed
- **Inter-rater reliability**: ≥70% agreement

### User Experience
- **Setup time**: <5 minutes (Docker)
- **First detection**: <10 minutes from setup
- **Documentation clarity**: 80%+ task completion rate

---

## Current Priority (Week 1-2)

**Focus**: Foundation setup

**Immediate Tasks:**
1. Initialize repository structure (see [context/docs/02-Project-Structure.md](context/docs/02-Project-Structure.md))
2. Create `docker-compose.yml` for dev environment
3. Scaffold FastAPI backend with health endpoint
4. Scaffold React frontend with routing
5. Set up database with Alembic migrations

**Output**: Working application that responds to HTTP requests and displays a basic UI

---

## Future Context (Post-MVP)

**Version 2.0+ (Not in Current Scope):**
- Multi-user authentication
- Cloud deployment option
- Real-time collaboration
- Additional sky surveys (POSS-II, SERC)
- Mobile application
- Advanced ML techniques (active learning, ensemble models)
- Integration with professional astronomical databases

**For now**: Focus only on MVP (Phase 1-5, single-user, local deployment)

---

## Notes for AI Code Assistants

### When Writing Backend Code:
- Always use type hints: `def process_image(image: np.ndarray) -> Detection:`
- Use Pydantic models for API schemas
- Prefer async/await for I/O operations
- Handle errors with proper HTTP status codes
- Log important operations (use structured logging)

### When Writing Frontend Code:
- Use functional components with hooks (no class components)
- Prefer composition over prop drilling (use Zustand for global state)
- Always handle loading and error states
- Use TypeScript strictly (no `any` types unless absolutely necessary)
- Keep components small and focused (<200 lines)

### When Working with AI/ML:
- Always set random seeds for reproducibility
- Document model assumptions and limitations
- Provide confidence scores with all predictions
- Enable CPU fallback (not everyone has GPUs)
- Cache model weights locally (don't re-download)

### When Writing Tests:
- Test the happy path AND error cases
- Use fixtures for common setup
- Mock external API calls
- Test edge cases (empty inputs, large inputs, invalid inputs)
- Aim for 80%+ coverage

---

## Ready to Code?

1. **Read**: [context/docs/00-Quick-Start.md](context/docs/00-Quick-Start.md) for installation
2. **Understand**: [context/docs/01-Architecture.md](context/docs/01-Architecture.md) for system design  
3. **Navigate**: [context/docs/02-Project-Structure.md](context/docs/02-Project-Structure.md) for where files go
4. **Plan**: [context/docs/03-Development-Phases.md](context/docs/03-Development-Phases.md) for what to build
5. **Build**: Start with Phase 1, Week 1-2 tasks

**Questions?** Check the context/docs/ first, they're comprehensive and up-to-date.

---

**Last Updated**: October 27, 2025  
**Version**: 1.0 (Pre-development)  
**Maintainer**: Project Lead
