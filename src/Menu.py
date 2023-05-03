import time
from const import CLOSE_MENU, BUY_BOOK, ADD_BOOK, CHECK_BOOK_DATA
from Book import Book
from Df_collection import DataFrameCollection


class Menu:
    """
    The app's main menu.
    """
    def __init__(self, df_collection: DataFrameCollection):
        self.df_collection = df_collection

    def invalid_input_error(self):
        """
        This function is called whenever the user enters invalid
        input.
        :return: -1, indicating that an error occurred.
        """
        invalid_input_message = "Please, enter a valid number!\n\n"
        print(invalid_input_message)
        time.sleep(1)
        return -1

    def run(self):
        time.sleep(0.5)
        print("What would you like to do?")
        time.sleep(0.5)
        print("1 - Check book data")
        print("2 - Buy book")
        print("3 - Close menu")
        print("4 - Add book to store")

        user_choice = input(">> ")
        try:
            user_choice = int(user_choice)
            if user_choice == CLOSE_MENU:
                print("GOODBYE!")
                time.sleep(1)
                return user_choice

            if user_choice == BUY_BOOK:
                print("YOU CHOOSE 2")
                return user_choice

            if user_choice == CHECK_BOOK_DATA:
                print(self.df_collection.books)
                return user_choice

            if user_choice == ADD_BOOK:
                self.add_book()
                return user_choice

            else:
                raise Exception

        except Exception:
            return self.invalid_input_error()

    def add_book(self):
        """
        Adds a book to the store.
        :return:
        """
        name = input("What's the name of the book?\n>> ")
        time.sleep(0.5)
        author = input("What's the name of the author?\n>> ")
        time.sleep(0.5)
        # treat user input for price
        try:
            price = input("What's the price of the book?\n>> ")
            price = float(price)
            time.sleep(0.5)

        except Exception:
            return self.invalid_input_error()

        # treat user input for publication year
        try:
            publication_year = input("What's the year of publication?\n>> ")
            publication_year = int(publication_year)
            time.sleep(0.5)

        except Exception:
            return self.invalid_input_error()

        book = Book(name=name, author=author, price=price, year_of_publication=publication_year)
        self.df_collection.add_book(book.to_df())
