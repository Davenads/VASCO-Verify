#!/usr/bin/env python3
"""Initialize the database with tables."""

import sys
from pathlib import Path

# Add parent directory to path to import app modules
sys.path.insert(0, str(Path(__file__).parent.parent / "backend"))

from app.db.base import Base
from app.db.session import engine
from app.db.models import Plate, Detection, Verification, ExternalEvent


def init_db() -> None:
    """Create all database tables."""
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully!")
    print(f"Tables created: {', '.join(Base.metadata.tables.keys())}")


if __name__ == "__main__":
    init_db()
