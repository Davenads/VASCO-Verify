"""FITS plate database model."""

from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, Text
from app.db.base import Base


class Plate(Base):
    """
    Model for POSS-I photographic plate metadata.

    Represents a single FITS file with associated astronomical metadata.
    """

    __tablename__ = "plates"

    id = Column(Integer, primary_key=True, index=True)

    # File information
    filename = Column(String(255), nullable=False, unique=True, index=True)
    file_path = Column(String(512), nullable=False)
    file_size = Column(Integer, nullable=False)  # bytes
    upload_date = Column(DateTime, default=datetime.utcnow, nullable=False)

    # Astronomical metadata
    plate_id = Column(String(50), nullable=True, index=True)  # Original plate identifier
    observation_date = Column(DateTime, nullable=True, index=True)
    exposure_time = Column(Float, nullable=True)  # seconds
    ra = Column(Float, nullable=True)  # Right Ascension (degrees)
    dec = Column(Float, nullable=True)  # Declination (degrees)
    field_center_ra = Column(Float, nullable=True)
    field_center_dec = Column(Float, nullable=True)

    # Image properties
    width = Column(Integer, nullable=True)  # pixels
    height = Column(Integer, nullable=True)  # pixels
    pixel_scale = Column(Float, nullable=True)  # arcsec/pixel
    limiting_magnitude = Column(Float, nullable=True)

    # Filter/Telescope info
    filter_name = Column(String(50), nullable=True)
    telescope = Column(String(100), default="Palomar 48-inch Schmidt")
    observatory = Column(String(100), default="Palomar Observatory")

    # Processing status
    status = Column(String(50), default="uploaded", index=True)
    # Status values: uploaded, processing, completed, failed

    # Additional metadata (JSON-like text field)
    additional_metadata = Column(Text, nullable=True)

    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    def __repr__(self) -> str:
        return f"<Plate(id={self.id}, filename='{self.filename}', date={self.observation_date})>"
