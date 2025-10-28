"""Database models package."""

from app.db.models.plate import Plate
from app.db.models.detection import Detection
from app.db.models.verification import Verification
from app.db.models.external_event import ExternalEvent

__all__ = ["Plate", "Detection", "Verification", "ExternalEvent"]
