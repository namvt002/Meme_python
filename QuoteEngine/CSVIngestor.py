"""CSVIngestor"""


from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from typing import List
import pandas as pd


class CSVIngestor(IngestorInterface):
    """ CSVIngestor """
    sp_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        # Add logic to parse CSV file and convert to QuoteModel objects
        if not cls.can_ingest(path):
            raise ValueError('File not found in system')

        quotes = []

        try:
            doc_file = pd.read_csv(path, header=0, encoding="utf8")
        except pd.errors.EmptyDataError:
            # Handle the case where the csv file is empty
            print(f"Empty csv file")
            return quotes
        except pd.errors.ParserError:
            print(f"Error parsing csv file")
            return quotes

        for _, row in doc_file.iterrows():
            quote = QuoteModel(row['body'], row['author'])
            quotes.append(quote)
        return quotes
