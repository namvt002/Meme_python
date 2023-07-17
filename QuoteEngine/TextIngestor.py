"""Parsing the contents of a text file."""


from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TextIngestor(IngestorInterface):
    """Checks file path ends with the `.txt`."""

    sp_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Implementation specific to text files."""
        if not cls.can_ingest(path):
            """Show error"""
            raise ValueError('Unsupported file type')

        quotes = []

        try:
            with open(path, 'r', encoding='utf8') as file:
                for line in file:
                    line = line.strip()
                    if line:
                        parts = line.split('-')
                        if len(parts) == 2:
                            body, author = parts
                            quote = QuoteModel(body, author)
                            quotes.append(quote)
        except FileNotFoundError:
            print(f"File not found in system")

        return quotes
