import pandas as pd


class Book:
    """
    A book.
    """
    def __init__(self, name, price, author, year_of_publication):
        """
        Creates a new book.
        :param name: The name of the book.
        :param price: The price of the book. Should be a float.
        :param author: The author of the book.
        :param year_of_publication: The year that the book was published. Should be an int.
        """
        self.name = name
        self.price = price
        self.author = author
        self.year_of_publication = year_of_publication

    def to_df(self):
        """
        Converts the book to a dataframe.
        :return: The dataframe of the new book.
        """
        return pd.DataFrame(
            {
                "name": [self.name],
                "price": [self.price],
                "author": [self.author],
                "year_of_publication": [self.year_of_publication],
            }
        )
