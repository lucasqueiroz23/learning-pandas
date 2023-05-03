from Menu import Menu
from const import CLOSE_MENU
from Df_collection import DataFrameCollection

if __name__ == "__main__":
    df_collection = DataFrameCollection()
    menu = Menu(df_collection=df_collection)
    print("Welcome to our bookstore!\n")
    while menu.run() != CLOSE_MENU:
        print("\n")
