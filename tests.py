import unittest
import joblib
import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline
from utils import get_mean_house_price, predict_house_price_from_input


class Tester(unittest.TestCase):

    def test_get_mean_house_price(self):
        mean = get_mean_house_price()
        print(f'Mean = {mean}')
        self.assertIsInstance(mean, int)

    def test_predict_house_price_from_input(self):
        house = {
            "area": 7420,
            "bedrooms": 4,
            "bathrooms": 2,
            "stories": 3,
            "mainroad": "yes",
            "guestroom": "no",
            "basement": "no",
            "hotwaterheating": "no",
            "airconditioning": "yes",
            "parking": 2,
            "prefarea": "yes",
            "furnishingstatus": "furnished"
        }

        house_df = pd.DataFrame([house])
        pipeline = joblib.load('pipeline.pkl')

        predicted_price = predict_house_price_from_input(pipeline, house_df)
        print(f'\nPredicted price = {predicted_price}')
        # Assert that the predicted price is an integer
        self.assertIsInstance(predicted_price, int)


if __name__ == '__main__':
    unittest.main()
