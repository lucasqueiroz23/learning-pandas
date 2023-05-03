import pandas as pd


class DataFrameCollection:
    """
    A collection of DataFrames.
    """
    def __init__(self):
        self.books = pd.DataFrame()

    def add_book(self, book):
        """
        Adds a book to the book df.
        :param book: The DataFrame of the new book.
        :return: The updated book collection.
        """
        self.books = pd.concat([self.books, book], ignore_index=True)
