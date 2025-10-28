"""Detection database model."""

from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.db.base import Base


class Detection(Base):
    """
    Model for AI-detected transient objects.

    Represents a single detection from YOLOv8 model inference.
    """

    __tablename__ = "detections"

    id = Column(Integer, primary_key=True, index=True)

    # Foreign key to plate
    plate_id = Column(Integer, ForeignKey("plates.id"), nullable=False, index=True)

    # Detection coordinates (pixel space)
    x = Column(Float, nullable=False)  # X coordinate in image
    y = Column(Float, nullable=False)  # Y coordinate in image
    width = Column(Float, nullable=False)  # Bounding box width
    height = Column(Float, nullable=False)  # Bounding box height

    # Astronomical coordinates (sky space)
    ra = Column(Float, nullable=True)  # Right Ascension (degrees)
    dec = Column(Float, nullable=True)  # Declination (degrees)

    # Detection confidence
    confidence = Column(Float, nullable=False, index=True)  # 0.0 to 1.0
    model_version = Column(String(50), nullable=False)  # e.g., "yolov8_v1"

    # Classification
    object_type = Column(String(50), default="transient", index=True)
    # Types: transient, artifact, cosmic_ray, known_star, uncertain

    # Verification status
    verified = Column(Boolean, default=False, index=True)
    verification_status = Column(String(50), default="pending", index=True)
    # Status: pending, accepted, rejected, uncertain

    # Cross-matching results
    panstarrs_matches = Column(Integer, default=0)
    gaia_matches = Column(Integer, default=0)
    catalog_data = Column(Text, nullable=True)  # JSON data

    # Additional metadata
    notes = Column(Text, nullable=True)

    # Timestamps
    detected_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    # Relationships
    # plate = relationship("Plate", back_populates="detections")

    def __repr__(self) -> str:
        return f"<Detection(id={self.id}, plate_id={self.plate_id}, confidence={self.confidence:.2f})>"
