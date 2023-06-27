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

        temp_file = f'{random.randint(0,1000000)}.txt'
        call = subprocess.run(['pdftotext', '-table', path, temp_file])

        quotes = []
        try:
            with open(temp_file, 'r', encoding='UTF-8') as infile:
                for line in infile.readlines():
                    line = line.strip('\n\r').strip()
                    if len(line) > 0:
                        body, author = line.split(' - ')
                        quote = QuoteModel(body, author)
                        quotes.append(quote)
        except:
            print("Error in handling converted txt")
        finally:
            os.remove(temp_file)
        
        return quotes