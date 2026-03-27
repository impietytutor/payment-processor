# utils.py
import logging
from typing import Dict, Any
from payment_processor.exceptions import PaymentProcessorException

def get_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """Get a logger instance with the given name and level."""
    logger = logging.getLogger(name)
    logger.setLevel(level)
    return logger

def validate_dict(input_dict: Dict[str, Any], required_keys: list[str]) -> None:
    """Validate a dictionary against a list of required keys."""
    for key in required_keys:
        if key not in input_dict:
            raise PaymentProcessorException(f"Missing required key '{key}'")

def hash_password(password: str, salt_length: int = 16) -> str:
    """Hash a password with a random salt."""
    import hashlib
    import secrets
    salt = secrets.token_hex(salt_length)
    hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), 100000)
    return f"{salt}:{hashed_password.hex()}"