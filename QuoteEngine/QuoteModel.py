"""QuoteModel."""


class QuoteModel:
    """QuoteModel."""
    body: str
    author: str

    def __init__(self, body: str, author: str) -> None:
        """init body and author."""
        self.body = body
        self.author = author

    def __repr__(self) -> str:
        """print repr."""
        return f"{self.body} - {self.author}"
