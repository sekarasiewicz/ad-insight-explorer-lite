import logging
from typing import Optional


def setup_logger(name: str = "app", level: Optional[str] = None) -> logging.Logger:
    """
    Simple logger setup for demo purposes
    """
    logger = logging.getLogger(name)

    if not logger.handlers:  # Only add handler if none exists
        handler = logging.StreamHandler()
        formatter = logging.Formatter("%(levelname)s: %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    # Set level based on environment or default to INFO
    log_level = level or "INFO"
    logger.setLevel(getattr(logging, log_level.upper(), logging.INFO))

    return logger


# Create a simple logger instance
logger = setup_logger("app")
