"""Implement abstract base class."""


from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """Methods specific to their respective file types."""
    sp_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        # Method checks if the file path ends.
        ext = path.split('.')[-1].lower()
        return ext in cls.sp_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """parse."""
        pass
