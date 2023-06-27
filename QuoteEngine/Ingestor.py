"""Interface to standardize and hide complexity of different extensions."""
from .CSVIngestor import CSVIngestor
from .TXTIngestor import TXTIngestor
from .DOCXIngestor import DOCXIngestor
from .PDFIngestor import PDFIngestor
from .IngestorInterface import IngestorInterface
from typing import List
from .QuoteModel import QuoteModel


class Ingestor(IngestorInterface):
    """Class standardizes and hides complexity of different extensions."""

    ingestors = [CSVIngestor, TXTIngestor, DOCXIngestor, PDFIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Go through different ingestors to find the right one."""
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
        raise Exception('File extension not accepted')
