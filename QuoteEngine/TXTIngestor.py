from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from typing import List

class TXTIngestor():
    allowed_extensions = ['txt']
    
    @classmethod
    def can_ingest(cls, path: str) -> bool:
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')
        
        quotes = []
        with open(path, 'r') as infile:
            for line in infile.read():
                print(line)
                body, author = line.split(' - ')
                quote = QuoteModel(body, author)
                quotes.append(quote)
        
        return quotes