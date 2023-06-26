from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from typing import List
import pandas as pd

class CSVIngestor():
    allowed_extensions = ['csv']
    
    @classmethod
    def can_ingest(cls, path: str) -> bool:
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')
        
        quotes = []
        df = pd.read_csv(path)

        for idx, row in df.iterrows():
            quote = QuoteModel(row.body, row.author)
            quotes.append(quote)
        
        return quotes