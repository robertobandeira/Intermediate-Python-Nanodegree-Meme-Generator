"""Strategy object that realizes DOCX case."""
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from typing import List
import docx


class DOCXIngestor(IngestorInterface):
    """Start an Ingestor to realize the interface for CSV."""

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse DOCX file to list of quotes."""
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                parse = para.text.split(' - ')
                quote = QuoteModel(parse[0], parse[1])
                quotes.append(quote)

        return quotes
