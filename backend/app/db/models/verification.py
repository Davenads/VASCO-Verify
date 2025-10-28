"""Verification database model."""

from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text, Boolean
from app.db.base import Base


class Verification(Base):
    """
    Model for manual verification of detections.

    Represents a human review of an AI detection.
    """

    __tablename__ = "verifications"

    id = Column(Integer, primary_key=True, index=True)

    # Foreign key to detection
    detection_id = Column(Integer, ForeignKey("detections.id"), nullable=False, index=True)

    # Verification decision
    decision = Column(String(50), nullable=False, index=True)
    # Decisions: accepted, rejected, uncertain

    # User identification (for future multi-user support)
    user_id = Column(String(50), default="anonymous", index=True)

    # Verification details
    confidence = Column(Integer, nullable=True)  # User confidence 1-5
    is_transient = Column(Boolean, nullable=True)
    is_artifact = Column(Boolean, nullable=True)
    is_cosmic_ray = Column(Boolean, nullable=True)
    is_known_object = Column(Boolean, nullable=True)

    # Tags
    tags = Column(String(255), nullable=True)  # Comma-separated tags

    # Notes
    notes = Column(Text, nullable=True)

    # Quality metrics
    review_time = Column(Integer, nullable=True)  # seconds spent reviewing

    # Timestamps
    verified_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    def __repr__(self) -> str:
        return f"<Verification(id={self.id}, detection_id={self.detection_id}, decision='{self.decision}')>"
