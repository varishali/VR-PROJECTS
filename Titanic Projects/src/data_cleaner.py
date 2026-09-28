import pandas as pd
def clean_data(df):
    """
    Missing value kop fill karta hai aur unnecesarry columns drop karta hai.
    """
    # direct Assignment se missing value fill 
    df['Age'] = df['Age'].fillna(df['Age'].median())
    df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

    # Unnecessary columns drop
    df = df.drop(columns=['Cabin','PassengerId','Ticket'])

    # missing value after cleaning 
    print(df.isnull().sum())

    print("-" * 50)

    return df

