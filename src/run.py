import pandas as pd

if __name__ == "__main__":
    df = pd.DataFrame()
    i = 3
    while i > 0:
        name = input("Name: ")
        age = int(input("Age: "))

        new_df = pd.DataFrame({
            "name": name,
            "age": age,
        }, index=[i])

        df = pd.concat([df, new_df], ignore_index=True)
        i -= 1

    print(df)
