# Development Phases

14-week roadmap from foundation to production-ready MVP.

## Overview

| Phase | Duration | Focus | Deliverable |
|-------|----------|-------|-------------|
| 1 | Weeks 1-4 | Foundation | Working app that loads/displays FITS |
| 2 | Weeks 5-8 | AI Integration | Functional AI detection |
| 3 | Weeks 9-10 | Verification | Manual review interface |
| 4 | Weeks 11-12 | Analysis | Statistical tools |
| 5 | Weeks 13-14 | Polish | Production-ready MVP |

---

## Phase 1: Foundation (Weeks 1-4)

**Goal**: Get basic infrastructure running

### Week 1-2: Setup & Architecture
- [ ] Initialize Git repository with proper structure
- [ ] Set up Docker development environment
- [ ] Create FastAPI backend scaffold with health endpoint
- [ ] Create React frontend scaffold with routing
- [ ] Design and implement database schema
- [ ] Write initial documentation

**Checklist:**
```bash
✓ docker-compose up works
✓ Backend responds at /health
✓ Frontend loads at localhost:3000
✓ Database migrations run
✓ Can commit and push code
```

### Week 3-4: Core Data Pipeline
- [ ] Implement FITS file loading (Astropy)
- [ ] Create image preprocessing pipeline
- [ ] Build basic difference imaging algorithm
- [ ] Implement database models (SQLAlchemy)
- [ ] Create API endpoints for plates
- [ ] Build frontend image viewer with pan/zoom

**Deliverables:**
- Working FITS file upload
- Image display in browser
- Database storing plate metadata

**Success Criteria:**
- Can upload a FITS file via API
- File appears in database
- Image displays correctly in frontend
- No critical bugs in core pipeline

---

## Phase 2: AI Integration (Weeks 5-8)

**Goal**: Functional AI-powered transient detection

### Week 5-6: Model Development
- [ ] Acquire/generate training data
  - Request labeled data from Dr. Bruehl
  - Collect public astronomical transients
  - Create synthetic data via augmentation
- [ ] Set up training pipeline (YOLOv8)
- [ ] Train initial detection model
- [ ] Evaluate on validation set
- [ ] Document model performance

**Targets:**
- Precision: ≥85%
- Recall: ≥80%
- Training time: <24 hours on single GPU

### Week 7-8: Model Integration
- [ ] Integrate trained model into backend
- [ ] Implement GPU/CPU inference options
- [ ] Create batch processing system
- [ ] Add confidence scoring and filtering
- [ ] Build API endpoint for detection
- [ ] Implement async job queue

**Deliverables:**
- Trained model checkpoint
- Inference API endpoint
- Batch processing capability

**Success Criteria:**
- Model inference completes in <3 seconds (GPU) or <60 seconds (CPU)
- API accepts plates and returns detections
- Confidence scores are meaningful
- Can process multiple plates in batch

---

## Phase 3: Verification Interface (Weeks 9-10)

**Goal**: Enable human review of AI detections

### Week 9: Review UI
- [ ] Build detection review page
- [ ] Implement side-by-side image comparison
- [ ] Create detection overlay visualization
- [ ] Add zoom/pan controls for detailed inspection
- [ ] Build annotation form (accept/reject/uncertain)
- [ ] Implement tagging system
- [ ] Add keyboard shortcuts for fast review

**UX Requirements:**
- Users can review ≥10 detections/minute
- Clear visual distinction between detection and background
- Intuitive controls (arrow keys for navigation)

### Week 10: Validation Tools
- [ ] Implement PanSTARRS catalog query
- [ ] Implement Gaia DR3 catalog query
- [ ] Add automatic cross-matching
- [ ] Create PSF analysis visualization
- [ ] Build consensus calculation system
- [ ] Implement export functionality (CSV, JSON)

**Deliverables:**
- Complete verification workflow
- Catalog cross-matching
- Export verified transients

**Success Criteria:**
- Users can efficiently review and annotate detections
- Catalog queries return results in <2 seconds
- Consensus calculation works correctly
- Exports produce valid, usable files

---

## Phase 4: Statistical Analysis (Weeks 11-12)

**Goal**: Reproduce published statistical findings

### Week 11: Analysis Tools
- [ ] Import nuclear test dates (from public sources)
- [ ] Import UAP report data (UFOCAT)
- [ ] Implement chi-square test
- [ ] Implement Mann-Whitney U test
- [ ] Implement Spearman correlation
- [ ] Build GLM with negative binomial distribution
- [ ] Add relative risk calculation

**Statistical Tests to Implement:**
```python
- Chi-square: nuclear testing vs. transients
- Mann-Whitney U: transient counts by group
- Spearman rho: transients vs. UAP reports
- GLM: count regression for transients
```

### Week 12: Visualization & Reproducibility
- [ ] Create timeline visualization (transients + events)
- [ ] Build scatter plots for correlations
- [ ] Add histogram for distributions
- [ ] Create heatmap for temporal density
- [ ] Implement "Reproduce Paper" feature
- [ ] Generate statistical reports

**Deliverables:**
- All statistical tests functional
- Interactive visualizations
- Reproducibility verification module

**Success Criteria:**
- Statistical results match published paper (within 5%)
- Visualizations are clear and informative
- Can reproduce main findings with one click
- Reports are publication-ready

---

## Phase 5: Polish & Documentation (Weeks 13-14)

**Goal**: Production-ready platform

### Week 13: Refinement
- [ ] Performance optimization
  - Profile slow endpoints
  - Add caching where appropriate
  - Optimize database queries
  - Reduce bundle size (frontend)
- [ ] Error handling improvements
- [ ] Add loading states and progress bars
- [ ] Implement user feedback (toasts, notifications)
- [ ] Cross-browser testing (Chrome, Firefox, Safari, Edge)
- [ ] Accessibility improvements (ARIA labels, keyboard nav)
- [ ] Security review

**Performance Targets:**
- API response: <100ms for simple queries
- Frontend load: <2 seconds
- AI inference: <3 seconds (GPU)

### Week 14: Documentation & Deployment
- [ ] Complete user guide with screenshots
- [ ] Record video tutorials (5-10 minutes)
- [ ] Write scientific methodology documentation
- [ ] Create deployment guide
- [ ] Set up CI/CD pipeline (GitHub Actions)
- [ ] Prepare demo data and examples
- [ ] Write contribution guidelines
- [ ] Create GitHub release v1.0

**Deliverables:**
- Comprehensive documentation
- Video tutorials
- Production deployment
- GitHub release

**Success Criteria:**
- All tests passing (≥80% coverage)
- Documentation complete and clear
- Beta testers can deploy without assistance
- No critical bugs
- Performance targets met

---

## Progress Tracking

Use this checklist to track progress:

```markdown
## Phase 1: Foundation
- [ ] Week 1-2: Setup & Architecture (0/6 tasks)
- [ ] Week 3-4: Core Data Pipeline (0/6 tasks)

## Phase 2: AI Integration  
- [ ] Week 5-6: Model Development (0/5 tasks)
- [ ] Week 7-8: Model Integration (0/6 tasks)

## Phase 3: Verification Interface
- [ ] Week 9: Review UI (0/7 tasks)
- [ ] Week 10: Validation Tools (0/6 tasks)

## Phase 4: Statistical Analysis
- [ ] Week 11: Analysis Tools (0/7 tasks)
- [ ] Week 12: Visualization (0/6 tasks)

## Phase 5: Polish & Documentation
- [ ] Week 13: Refinement (0/8 tasks)
- [ ] Week 14: Documentation (0/8 tasks)

**Overall Progress: 0/65 tasks complete**
```

## Risk Mitigation

| Risk | Impact | Mitigation |
|------|--------|------------|
| Insufficient training data | High | Request data early, use augmentation, synthetic data |
| Model underperforms | High | Set realistic expectations, allow manual fallback |
| External API rate limits | Medium | Implement caching, respect rate limits |
| Scope creep | Medium | Strict MVP definition, defer non-critical features |
| Technical blockers | Medium | Weekly check-ins, ask for help early |

## Definition of Done

A phase is complete when:
- [ ] All tasks are checked off
- [ ] Tests are written and passing
- [ ] Code is reviewed and merged
- [ ] Documentation is updated
- [ ] Demo works end-to-end
- [ ] No critical bugs

## Post-MVP Roadmap

**After v1.0 release:**

**v1.1** (1-2 months)
- Performance optimizations
- Additional catalog sources (SIMBAD, VizieR)
- Improved AI model (more training data)
- User authentication (for multi-user deployments)

**v2.0** (3-6 months)
- Support for POSS-II and other surveys
- Cloud deployment option
- Real-time collaboration features
- Mobile-responsive design
- Advanced analytics dashboard

**v3.0** (6-12 months)
- Machine learning improvements (active learning)
- Integration with professional databases
- API for programmatic access
- Community features (forums, leaderboards)

---

**Next**: [04-Backend-API.md](04-Backend-API.md) - Design your API endpoints
