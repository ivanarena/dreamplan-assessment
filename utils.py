import pandas as pd
from pathlib import Path


def load_dataset():
    return pd.read_csv(Path("Housing.csv"))


def get_mean_house_price():
    dataset = load_dataset()
    # convert to int for coherence with the dataset
    return int(dataset["price"].mean())


def predict_house_price_from_input(pipeline, house_df):
    predicted_price = pipeline.predict(house_df)
    # convert to int for coherence with the dataset
    return int(predicted_price[0])
