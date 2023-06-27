"""Strategy object that realizes PDF case."""
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from typing import List
import subprocess
import random
import os


class PDFIngestor(IngestorInterface):
    """Start an Ingestor to realize the interface for PDF."""

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse PDF file to list of quotes."""
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        temp_file = f'./tmp/{random.randint(0,1000000)}.txt'
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
        except Exception:
            print("Error in handling converted txt")
        finally:
            os.remove(temp_file)

        return quotes
