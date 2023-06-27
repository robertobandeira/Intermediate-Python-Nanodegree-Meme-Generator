"""Strategy object that realizes CSV case."""
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from typing import List
import pandas as pd


class CSVIngestor(IngestorInterface):
    """Start an Ingestor to realize the interface for CSV."""

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse CSV file to list of quotes."""
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        df = pd.read_csv(path)

        for idx, row in df.iterrows():
            quote = QuoteModel(row.body, row.author)
            quotes.append(quote)

        return quotes
