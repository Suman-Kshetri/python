import pandas as pd


def clean_data(df):
    # Missing values
    df["age"].fillna(df["age"].mean(), inplace=True)
    
    # Remove duplicates
    df = df.drop_duplicates()
    
    # Data types
    df["date"] = pd.to_datetime(df["date"])
    
    # Outliers
    Q1 = df["salary"].quantile(0.25)
    Q3 = df["salary"].quantile(0.75)
    IQR = Q3 - Q1
    df = df[(df["salary"] >= Q1 - 1.5*IQR) & (df["salary"] <= Q3 + 1.5*IQR)]
    
    # Encoding
    df = pd.get_dummies(df, columns=["city"], drop_first=True)
    
    return df