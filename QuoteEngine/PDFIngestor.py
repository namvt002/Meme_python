"""Parsing pdf file."""


import subprocess
from typing import List
from pathlib import Path
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
import random


class PDFIngestor(IngestorInterface):
    """PDFIngestor."""

    sp_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Implementation specific to PDF files."""
        try:
            if not cls.can_ingest(path):
                raise Exception('File not found in system')

            text_file = Path(f'./temp/{random.randint(0,100000000)}.txt')
            subprocess.call(['pdftotext', path, str(text_file)])

            quotes = []
            with open(text_file, "r", encoding='utf8') as file:
                for _, line in enumerate(file):
                    parsed = line.strip().split('-')
                    if parsed != ['']:
                        new_quote = QuoteModel(parsed[0], parsed[1])
                        quotes.append(new_quote)
            return quotes
        except Exception as e:
            print(f'An error parsing PDF file {e}')
            return []
