class QuoteModel():
    """Class to encapsulate quotes' body and author."""

    def __init__(self, body, author):
        self.body = body 
        self.author = author 

    def __str__(self):
        return f'{self.body} - {self.author}'
    
    def __repr__(self):
        return f'Quote: "{self.body}" - {self.author}'