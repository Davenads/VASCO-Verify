"""External event database model."""

from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, Text
from app.db.base import Base


class ExternalEvent(Base):
    """
    Model for external events (nuclear tests, UAP reports).

    Used for correlation analysis with detected transients.
    """

    __tablename__ = "external_events"

    id = Column(Integer, primary_key=True, index=True)

    # Event type
    event_type = Column(String(50), nullable=False, index=True)
    # Types: nuclear_test, uap_report, other

    # Event identification
    event_name = Column(String(255), nullable=True)
    event_date = Column(DateTime, nullable=False, index=True)

    # Location (if applicable)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    location_name = Column(String(255), nullable=True)

    # Nuclear test specific fields
    test_country = Column(String(50), nullable=True)
    test_yield_kt = Column(Float, nullable=True)  # Kilotons
    test_type = Column(String(50), nullable=True)  # atmospheric, underground, etc.

    # UAP report specific fields
    uap_report_id = Column(String(100), nullable=True)
    uap_source = Column(String(100), nullable=True)  # UFOCAT, NUFORC, etc.

    # Additional metadata
    description = Column(Text, nullable=True)
    source = Column(String(255), nullable=True)
    additional_metadata = Column(Text, nullable=True)  # JSON data

    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    def __repr__(self) -> str:
        return f"<ExternalEvent(id={self.id}, type='{self.event_type}', date={self.event_date})>"
