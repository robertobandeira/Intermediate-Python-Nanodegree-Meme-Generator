"""Encapsulate quotes' body and author."""


class QuoteModel():
    """Class to encapsulate quotes' body and author."""

    def __init__(self, body, author):
        """Instantiate the class with its body and author."""
        self.body = body
        self.author = author

    def __str__(self):
        """Represent the string version of the quote."""
        return f'{self.body} - {self.author}'

    def __repr__(self):
        """Represent the quote."""
        return f'Quote: "{self.body}" - {self.author}'
