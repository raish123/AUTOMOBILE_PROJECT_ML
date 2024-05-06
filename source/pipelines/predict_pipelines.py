import pandas as pd
import numpy as np
import dill
import os
import sys
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from source.exceptions import CustomException
from source.loggers import logging
from source.utils import load_object

class PredictPipeline():
    def __init__(self):
        pass

    def predict(self, feature):
        try:
            preprocessor_path = 'artifacts/preprocessor.pkl'
            model_path = 'artifacts/model.pkl'

            model = load_object(model_path)
            preprocessor = load_object(preprocessor_path)

            logging.info('Successfully loaded model and preprocessor. Now transforming and predicting new data.')

            logging.info('The preprocessor used to transform new data:\n%s', preprocessor)

            # Transforming features using the preprocessor
            scaling = preprocessor.transform(feature)
            prediction = model.predict(scaling)

            return prediction
        except Exception as e:
            raise CustomException(e, sys)

class CustomData():
    def __init__(self,
                symboling: int,
                normalized_losses: int,
                make: str,
                fuel_type: str,
                body_style: str,
                drive_wheels: str,
                engine_location: str,
                width: float,
                height: float,
                engine_type: str,
                engine_size: int,
                horsepower: int,
                city_mpg: int,
                highway_mpg: int):

        self.symboling = symboling
        self.normalized_losses = normalized_losses
        self.make = make
        self.fuel_type = fuel_type
        self.body_style = body_style
        self.drive_wheels = drive_wheels
        self.engine_location = engine_location
        self.width = width
        self.height = height
        self.engine_type = engine_type
        self.engine_size = engine_size
        self.horsepower = horsepower
        self.city_mpg = city_mpg
        self.highway_mpg = highway_mpg

    def get_data_as_dataframe(self):
        custom_data_input_dict = {
            "symboling": [self.symboling],
            "normalized_losses": [self.normalized_losses],
            "make": [self.make],
            "fuel_type": [self.fuel_type],
            "body_style": [self.body_style],
            "drive_wheels": [self.drive_wheels],
            "engine_location": [self.engine_location],
            "width": [self.width],
            "height": [self.height],
            "engine_type": [self.engine_type],
            "engine_size": [self.engine_size],
            "horsepower": [self.horsepower],
            "city_mpg": [self.city_mpg],
            "highway_mpg": [self.highway_mpg]
        }

        return pd.DataFrame(custom_data_input_dict)
