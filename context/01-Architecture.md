# System Architecture

## High-Level Architecture

```
┌──────────────────────────────────────────────────────────┐
│                    CLIENT BROWSER                         │
│                                                            │
│  ┌──────────────────────────────────────────────────┐   │
│  │         React SPA (TypeScript)                    │   │
│  │  • Image Viewer  • Detection Review               │   │
│  │  • Analysis Tools • Export                        │   │
│  └──────────────────────────────────────────────────┘   │
└────────────────────────┬───────────────────────────────────┘
                         │ REST API (HTTP/JSON)
┌────────────────────────▼───────────────────────────────────┐
│                  BACKEND SERVER                            │
│  ┌──────────────────────────────────────────────────┐    │
│  │         FastAPI Application (Python)              │    │
│  │  • Image Processing  • AI Inference               │    │
│  │  • Statistical Analysis  • Data Management        │    │
│  └──────────────────────────────────────────────────┘    │
│                                                            │
│  ┌─────────┐  ┌──────────┐  ┌──────────────────┐        │
│  │ AI/ML   │  │ Database │  │  File Storage    │        │
│  │PyTorch  │  │ SQLite   │  │  (Local/S3)      │        │
│  └─────────┘  └──────────┘  └──────────────────┘        │
└────────────────────────┬───────────────────────────────────┘
                         │ External APIs
┌────────────────────────▼───────────────────────────────────┐
│              EXTERNAL SERVICES                             │
│  • DSS Plate Finder  • PanSTARRS  • Gaia DR3              │
└────────────────────────────────────────────────────────────┘
```

## Technology Stack

### Frontend
- **Framework**: React 18+ with TypeScript
- **Build**: Vite 5+
- **Styling**: Tailwind CSS
- **State**: Zustand
- **Image Viewing**: OpenLayers or Leaflet
- **Charts**: Recharts or D3.js

### Backend
- **Framework**: FastAPI (Python 3.10+)
- **Database**: SQLite → PostgreSQL
- **ORM**: SQLAlchemy 2.0+
- **AI/ML**: PyTorch 2.1+
- **Astronomy**: Astropy, photutils
- **Image**: OpenCV, Pillow

### Deployment
- **Container**: Docker + Docker Compose
- **CI/CD**: GitHub Actions
- **Docs**: MkDocs

## Architectural Principles

1. **Local-First**: Core functionality runs on user's machine
2. **Modular**: Loosely coupled services
3. **API-First**: Backend exposes REST API
4. **Stateless**: Each request is independent
5. **Progressive**: Works on CPU, optimized for GPU
6. **Container-Based**: Reproducible via Docker

## Key Design Decisions

| Component | Choice | Rationale |
|-----------|--------|-----------|
| Frontend | React + TypeScript | Large ecosystem, great DX, type safety |
| Backend | FastAPI | Fast, async, automatic docs, Python ML ecosystem |
| Database | SQLite → PostgreSQL | Simple for MVP, easy upgrade path |
| AI Framework | PyTorch | Research-friendly, astronomy community support |
| Deployment | Docker Compose | Single-command setup, reproducible |

## Data Flow

```
1. INPUT
   User uploads FITS or selects from DSS
   
2. PREPROCESSING  
   Load → Normalize → Background subtract
   
3. DETECTION
   AI inference → Filter by confidence → Extract candidates
   
4. VALIDATION
   Cross-match PanSTARRS → Cross-match Gaia → Flag known sources
   
5. VERIFICATION
   Present to user → Collect annotations → Calculate consensus
   
6. ANALYSIS
   Correlate with events → Statistical tests → Visualizations
   
7. OUTPUT
   Export catalog → Generate reports → Share results
```

## Module Overview

### Core Modules

1. **Image Processing**: FITS loading, preprocessing, difference imaging
2. **AI Detection**: Model inference, confidence scoring, filtering
3. **Catalog Query**: PanSTARRS/Gaia cross-matching
4. **Statistical Analysis**: Chi-square, Mann-Whitney U, GLM, correlations
5. **Verification**: User annotations, consensus calculation

### Support Modules

- **API Layer**: RESTful endpoints, request validation
- **Database**: ORM models, migrations
- **File Storage**: FITS files, exports, model checkpoints
- **Async Jobs**: Background processing for long-running tasks

## Security Considerations

- **No authentication** required for MVP (local deployment)
- **Input validation**: Check FITS file integrity
- **Rate limiting**: Prevent API abuse
- **CORS**: Configure for local development
- **File uploads**: Limit size, validate format

## Performance Targets

- **AI Inference**: <3 seconds per plate (GPU), <60 seconds (CPU)
- **API Response**: <100ms for simple queries
- **Frontend Load**: <2 seconds initial load
- **Database**: Support 100K+ transients without degradation

## Scalability Path

MVP focuses on single-user local deployment. Future scaling:

1. **Multi-user**: Add authentication, user management
2. **Cloud**: Deploy to AWS/GCP with load balancing
3. **Distributed**: Separate AI inference service
4. **Real-time**: WebSocket for live updates
5. **Big Data**: Migrate to PostgreSQL, add caching (Redis)

---

**Next**: [02-Project-Structure.md](02-Project-Structure.md) - See how files are organized
