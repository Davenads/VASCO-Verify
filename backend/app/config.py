"""Application configuration settings."""

from typing import List
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    model_config = SettingsConfigDict(env_file=".env", case_sensitive=False)

    # Application
    PROJECT_NAME: str = "Transient Analysis Platform"
    VERSION: str = "1.0.0"
    API_V1_PREFIX: str = "/api/v1"
    ENVIRONMENT: str = "development"

    # Database
    DATABASE_URL: str = "sqlite:///./data/transients.db"

    # ML/AI Settings
    ML_MODEL_PATH: str = "./ml/data/models"
    TORCH_HOME: str = "./ml/data/models/.cache"
    INFERENCE_DEVICE: str = "cpu"
    BATCH_SIZE: int = 16
    CONFIDENCE_THRESHOLD: float = 0.5

    # External APIs
    PANSTARRS_API_URL: str = "https://catalogs.mast.stsci.edu/api/v0.1/panstarrs"
    GAIA_API_URL: str = "https://gea.esac.esa.int/tap-server/tap"
    API_RATE_LIMIT: int = 10
    API_CACHE_TTL: int = 3600

    # File Storage
    UPLOAD_DIR: str = "./data/plates/uploads"
    MAX_UPLOAD_SIZE: int = 524288000  # 500MB

    # Logging
    LOG_LEVEL: str = "INFO"
    LOG_FILE: str = "./data/app.log"

    # CORS
    BACKEND_CORS_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://127.0.0.1:3000"
    ]


settings = Settings()
