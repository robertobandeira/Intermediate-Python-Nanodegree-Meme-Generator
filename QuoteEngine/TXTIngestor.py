"""Strategy object that realizes TXT case."""
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from typing import List


class TXTIngestor(IngestorInterface):
    """Start an Ingestor to realize the interface for TXT."""

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse TXT file to list of quotes."""
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        with open(path, 'r', encoding='UTF-8') as infile:
            for line in infile:
                body, author = line.strip('\n').split(' - ')
                quote = QuoteModel(body, author)
                quotes.append(quote)

        return quotes
