import numpy

class ScoreCounter:
    def __init__(self, book_vals):
        self.processed = set()
        self.book_vals = book_vals
        self.score = 0

    def add(self, books):
        for book in books:
            if book not in self.processed:
                self.processed.add(book)
                self.score += self.book_vals[book]
