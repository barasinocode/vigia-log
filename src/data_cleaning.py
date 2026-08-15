import pandas as pd


def load_and_clean_data(file_path):
    df = pd.read_csv(file_path)

    df = df.drop_duplicates()

    df["timestamp"] = pd.to_datetime(
        df["timestamp"],
        errors="coerce"
    )

    df = df.dropna(subset=["timestamp"])

    df["date"] = df["timestamp"].dt.date
    df["hour"] = df["timestamp"].dt.hour

    return df

    