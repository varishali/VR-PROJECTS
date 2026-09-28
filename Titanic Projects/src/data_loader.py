import pandas as pd

def load_and_inspect_data(filepath):
    """
    Data ko CSV se load karta hai aur basic detail orint karta hai
    """
    df = pd.read_csv(filepath)
    print("\n== INITIAL DATA INSPACTION ==")
    print(f"Data Shape: {df.shape}")

    print("\n== First 5 Rows:\n ", df.head())
    print("\n== Missing Value Before Cleaning:\n ", df.isnull().sum())
    print("-" * 50)
    return df

