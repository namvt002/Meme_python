"""The `parse` method uses the `Document`."""


from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
import docx


class DocxIngestor(IngestorInterface):
    """Document."""

    sp_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """parse."""
        if not cls.can_ingest(path):
            raise Exception("File not found in system")

        try:
            quotes = []
            document = docx.Document(path)
            for paragraph in document.paragraphs:
                if paragraph.text:
                    parts = paragraph.text.split('-')
                    if len(parts) == 2:
                        body, author = parts
                        quote = QuoteModel(body, author)
                        quotes.append(quote)
        except Exception:
            raise Exception(f"Error parsing file docx")

        return quotes
