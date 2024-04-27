# Automobile Price Prediction

## Overview
This project aims to predict automobile prices based on various features such as symboling, normalized losses, make, fuel type, body style, drive wheels, engine location, width, height, engine type, engine size, horsepower, city mpg, and highway mpg.

## Dataset
The dataset used for this project contains the following features:

- **symboling**: Insurance risk rating (-3, -2, -1, 0, 1, 2, 3).
- **normalized-losses**: Normalized losses in use as a relative average loss payment per insured vehicle year.
- **make**: Manufacturer's brand.
- **fuel-type**: Type of fuel (gas, diesel).
- **body-style**: Body style of the car (sedan, hatchback, wagon, hardtop, convertible).
- **drive-wheels**: Type of drive wheels (4wd, fwd, rwd).
- **engine-location**: Location of the engine (front, rear).
- **width**: Width of the car.
- **height**: Height of the car.
- **engine-type**: Type of engine (dohc, dohcv, l, ohc, ohcf, ohcv, rotor).
- **engine-size**: Size of the engine (in liters).
- **horsepower**: Horsepower of the car.
- **city-mpg**: Miles per gallon (mpg) in the city.
- **highway-mpg**: Miles per gallon (mpg) on the highway.

## Model Building
Various machine learning algorithms can be used to build the prediction model, including but not limited to:

- Linear Regression
- Lasso Regularization(for feature selection)
- Ridge Regularization(for feature selection)

## Evaluation Metrics
The performance of the model can be evaluated using metrics such as:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R-squared (R²) score

## Usage
To use this project:

1. Ensure Python is installed on your system.
2. Install the required libraries mentioned in the `requirements.txt` file.
3. Run the main script for data preprocessing, model training, and evaluation.
4. Tune the hyperparameters for better performance if necessary.
5. Deploy the trained model for inference in production.

## Future Improvements
Some potential areas for improvement include:

- Feature engineering to create new meaningful features.
- Hyperparameter tuning for better model performance.
- Trying out different algorithms and ensemble techniques.
- Incorporating additional relevant features if available.

## Contributors
- Raees Azam Shaikh

## License
This project is licensed under the [MIT License](LICENSE).
