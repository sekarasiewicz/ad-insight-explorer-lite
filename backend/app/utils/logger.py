import logging
import sys
from typing import Optional
from ..config import settings


def setup_logger(
    name: str = "quick_index", level: Optional[str] = None
) -> logging.Logger:
    """Setup logger with configurable level"""
    logger = logging.getLogger(name)

    # Set log level
    log_level = level or settings.log_level
    level_map = {"DEBUG": logging.DEBUG, "INFO": logging.INFO, "ERROR": logging.ERROR}
    logger.setLevel(level_map.get(log_level.upper(), logging.INFO))

    # Create console handler if not exists
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(logging.DEBUG)

        # Create formatter
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)

        # Add handler to logger
        logger.addHandler(handler)

    return logger


# Global logger instance
logger = setup_logger()
