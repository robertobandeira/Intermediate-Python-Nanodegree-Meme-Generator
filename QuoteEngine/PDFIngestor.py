from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from typing import List
import subprocess
import random
import os

class PDFIngestor():
    allowed_extensions = ['pdf']
    
    @classmethod
    def can_ingest(cls, path: str) -> bool:
        ext = path.split('.')[-1].lower()
        return ext in cls.allowed_extensions

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        temp_file = f'./tmp/{random.randint(0,10000)}.txt'
        call = subprocess.call(['xpdf', path, temp_file])
        print(path)
        print(temp_file)
        quotes = []
        with open(temp_file, 'r', encoding='UTF-8') as infile:
            for line in infile:
                line = line.strip('\n\r').strip()
                if len(line) > 0:
                    body, author = line.split(' - ')
                    quote = QuoteModel(body, author)
                    quotes.append(quote)

        os.remove(temp_file)
        
        return quotes