# Project Structure

Complete file and folder organization for the platform.

## Root Structure

```
poss-transient-platform/
├── README.md                    # Project overview
├── LICENSE                      # Open source license
├── .gitignore                   # Git ignore rules
├── docker-compose.yml           # Docker orchestration
├── Makefile                     # Common commands
├── .env.example                 # Environment template
│
├── frontend/                    # React application
├── backend/                     # FastAPI application
├── ml/                          # ML training & experiments
├── data/                        # Data storage (gitignored)
├── docs/                        # Technical documentation
├── scripts/                     # Utility scripts
└── tests/                       # Integration tests
```

## Frontend Structure

```
frontend/
├── package.json
├── tsconfig.json
├── vite.config.ts
├── tailwind.config.js
├── index.html
├── .eslintrc.json
├── .prettierrc
│
├── public/
│   ├── favicon.ico
│   └── assets/
│
└── src/
    ├── main.tsx                 # Entry point
    ├── App.tsx                  # Root component
    ├── vite-env.d.ts
    │
    ├── components/              # Reusable UI components
    │   ├── common/              # Buttons, inputs, modals
    │   │   ├── Button.tsx
    │   │   ├── Modal.tsx
    │   │   ├── Input.tsx
    │   │   └── Spinner.tsx
    │   ├── image/               # Image viewing
    │   │   ├── PlateViewer.tsx
    │   │   ├── ImageCanvas.tsx
    │   │   ├── DetectionOverlay.tsx
    │   │   └── ViewportControls.tsx
    │   ├── detection/           # Detection review
    │   │   ├── DetectionReview.tsx
    │   │   ├── DetectionCard.tsx
    │   │   ├── VerificationForm.tsx
    │   │   └── NavigationControls.tsx
    │   └── analysis/            # Statistical analysis
    │       ├── Timeline.tsx
    │       ├── StatsPanel.tsx
    │       ├── CorrelationPlot.tsx
    │       └── ExportDialog.tsx
    │
    ├── pages/                   # Page-level components
    │   ├── HomePage.tsx
    │   ├── PlatesPage.tsx
    │   ├── DetectionPage.tsx
    │   ├── VerificationPage.tsx
    │   └── AnalysisPage.tsx
    │
    ├── hooks/                   # Custom React hooks
    │   ├── useApi.ts
    │   ├── useImage.ts
    │   ├── useDetections.ts
    │   └── useWebSocket.ts
    │
    ├── services/                # API client
    │   ├── api.ts               # Base API client
    │   ├── plates.ts
    │   ├── detections.ts
    │   ├── verifications.ts
    │   └── analysis.ts
    │
    ├── stores/                  # Zustand stores
    │   ├── imageStore.ts
    │   ├── detectionStore.ts
    │   ├── analysisStore.ts
    │   └── uiStore.ts
    │
    ├── types/                   # TypeScript types
    │   ├── plate.ts
    │   ├── detection.ts
    │   ├── verification.ts
    │   └── api.ts
    │
    ├── utils/                   # Helper functions
    │   ├── format.ts
    │   ├── validation.ts
    │   └── astronomy.ts
    │
    ├── styles/                  # Global styles
    │   └── globals.css
    │
    └── __tests__/               # Tests
        ├── components/
        ├── hooks/
        └── utils/
```

## Backend Structure

```
backend/
├── pyproject.toml               # Python project config
├── requirements.txt             # Dependencies
├── requirements-dev.txt         # Dev dependencies
├── alembic.ini                  # DB migration config
├── Dockerfile
├── .env
│
└── app/
    ├── __init__.py
    ├── main.py                  # FastAPI entry point
    ├── config.py                # Settings
    │
    ├── api/                     # API routes
    │   ├── __init__.py
    │   ├── dependencies.py
    │   └── v1/
    │       ├── __init__.py
    │       ├── plates.py
    │       ├── detections.py
    │       ├── verifications.py
    │       ├── analysis.py
    │       └── export.py
    │
    ├── core/                    # Business logic
    │   ├── __init__.py
    │   ├── image_processor.py
    │   ├── detector.py
    │   ├── ai_inference.py
    │   ├── catalog_query.py
    │   ├── statistics.py
    │   └── validator.py
    │
    ├── db/                      # Database
    │   ├── __init__.py
    │   ├── base.py
    │   ├── session.py
    │   └── models/
    │       ├── __init__.py
    │       ├── plate.py
    │       ├── detection.py
    │       ├── verification.py
    │       └── external_event.py
    │
    ├── ml/                      # Machine learning
    │   ├── __init__.py
    │   ├── models/
    │   │   ├── yolo_detector.py
    │   │   └── classifier.py
    │   ├── inference.py
    │   ├── preprocessing.py
    │   └── utils.py
    │
    ├── schemas/                 # Pydantic schemas
    │   ├── __init__.py
    │   ├── plate.py
    │   ├── detection.py
    │   ├── verification.py
    │   └── analysis.py
    │
    ├── services/                # Service layer
    │   ├── __init__.py
    │   ├── plate_service.py
    │   ├── detection_service.py
    │   ├── verification_service.py
    │   └── analysis_service.py
    │
    ├── utils/                   # Utilities
    │   ├── __init__.py
    │   ├── fits_utils.py
    │   ├── astronomy.py
    │   └── logging.py
    │
    └── tests/                   # Backend tests
        ├── __init__.py
        ├── conftest.py
        ├── test_api/
        ├── test_core/
        └── test_ml/
```

## ML Training Structure

```
ml/
├── notebooks/                   # Jupyter notebooks
│   ├── 01_data_exploration.ipynb
│   ├── 02_model_training.ipynb
│   └── 03_evaluation.ipynb
│
├── configs/                     # Training configs
│   ├── yolov8_base.yaml
│   └── training_config.py
│
├── train.py                     # Training script
├── evaluate.py                  # Evaluation script
├── export_model.py              # Model export
│
└── data/
    ├── raw/                     # Raw training data
    ├── processed/               # Processed data
    │   ├── images/
    │   │   ├── train/
    │   │   ├── val/
    │   │   └── test/
    │   └── labels/
    │       ├── train/
    │       ├── val/
    │       └── test/
    └── models/                  # Trained models
        ├── yolov8_transient_v1.pt
        └── checkpoints/
```

## Data Storage

```
data/                            # Gitignored
├── plates/                      # FITS files
│   ├── poss_i/
│   └── uploads/
│
├── catalogs/                    # Cached catalogs
│   ├── panstarrs/
│   └── gaia/
│
├── cache/                       # API cache
│
└── exports/                     # User exports
    ├── csv/
    ├── json/
    └── reports/
```

## Documentation

```
docs/
├── README.md                    # Docs index
├── 00-Quick-Start.md
├── 01-Architecture.md
├── 02-Project-Structure.md     # This file
├── 03-Development-Phases.md
├── 04-Backend-API.md
├── 05-Database.md
├── 06-AI-ML-Pipeline.md
├── 07-Frontend-Components.md
├── 08-Data-Pipeline.md
├── 09-Testing.md
├── 10-Deployment.md
├── 11-Code-Standards.md
├── 12-External-Dependencies.md
└── 13-Commands-Reference.md
```

## Scripts

```
scripts/
├── setup_env.sh                 # Environment setup
├── download_data.py             # Download sample data
├── seed_database.py             # Seed test data
├── migrate_db.sh                # Database migrations
├── backup_db.sh                 # Backup database
└── deploy.sh                    # Deployment script
```

## Configuration Files

```
Root level configs:
├── .env.example                 # Environment template
├── .gitignore                   # Git ignore
├── .dockerignore                # Docker ignore
├── docker-compose.yml           # Docker setup
├── Makefile                     # Common tasks

Frontend configs:
├── frontend/package.json        # NPM config
├── frontend/tsconfig.json       # TypeScript config
├── frontend/vite.config.ts      # Vite config
├── frontend/tailwind.config.js  # Tailwind config
├── frontend/.eslintrc.json      # ESLint rules
└── frontend/.prettierrc         # Prettier config

Backend configs:
├── backend/pyproject.toml       # Python project
├── backend/requirements.txt     # Dependencies
├── backend/alembic.ini          # Alembic config
└── backend/.flake8              # Flake8 rules
```

## Git Ignore Rules

```gitignore
# .gitignore

# Environment
.env
.env.local

# Dependencies
node_modules/
venv/
__pycache__/

# Build outputs
frontend/dist/
backend/app/__pycache__/
*.pyc
*.pyo

# Data (except samples)
data/
!data/samples/

# ML artifacts
ml/data/raw/
ml/data/processed/
ml/data/models/*.pt
!ml/data/models/.gitkeep

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Logs
*.log
logs/

# Test coverage
coverage/
.coverage
htmlcov/
```

## Key File Purposes

| File | Purpose |
|------|---------|
| `main.tsx` | React entry point |
| `App.tsx` | Root component with routing |
| `main.py` | FastAPI application setup |
| `config.py` | Centralized configuration |
| `docker-compose.yml` | Orchestrate all services |
| `Makefile` | Common development commands |
| `requirements.txt` | Python dependencies |
| `package.json` | Node dependencies |

---

**Next**: [03-Development-Phases.md](03-Development-Phases.md) - See the roadmap
