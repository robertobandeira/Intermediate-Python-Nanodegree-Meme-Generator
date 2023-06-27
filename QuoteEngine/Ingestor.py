from .CSVIngestor import CSVIngestor
from .TXTIngestor import TXTIngestor
from .DOCXIngestor import DOCXIngestor
from .PDFIngestor import PDFIngestor
from .IngestorInterface import IngestorInterface
from typing import List
from .QuoteModel import QuoteModel

class Ingestor(IngestorInterface):
    ingestors = [CSVIngestor, TXTIngestor, DOCXIngestor, PDFIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)