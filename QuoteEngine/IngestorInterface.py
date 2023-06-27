"""Abstracts ingestor into interface class."""
from .QuoteModel import QuoteModel
from abc import ABC, abstractmethod
from typing import List


class IngestorInterface(ABC):
    """Abstract class to be realized for different types of file."""

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Check whether it's the right ingestor for the extension."""
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Abstract method to be realized and parse different file types."""
        pass
