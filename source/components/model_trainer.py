#in this file we r training the model and selecting best model for this dataset
#once we find the best model for this dataset then stored the model into pickle format
#so importing all the important library which is used for training the model
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression,Lasso,Ridge
from sklearn.metrics import r2_score,mean_squared_error
#if i doing hypertuning the model then we r usiung gridsearchcv class of sklearn
from sklearn.model_selection import GridSearchCV
from source.exceptions import CustomException
from source.loggers import logging
from source.utils import save_object,evaluate_model
import os,sys
from dataclasses import dataclass


#creating class for  ModelTrainerConfig where we mentioning the path of model.pkl file these path we defines as class variable
@dataclass
class ModelTrainerConfig():
    trained_model_config_path = os.path.join('artifacts','model.pkl')

#step2:- creating another class to initiate the training model
class ModelTrainer():
    #now creating constructor method to initialize the ModelTrainerConfig  class object in it!!
    def __init__(self):
        self.model_trainer_obj = ModelTrainerConfig()

    #creating instance method to initiate  the train_models method
    def initiate_training(self,train_array,test_array):
        logging.info('Initiate the traing the model')
        try:
            #defining models and its object in dict
            models = {
                'Linear_Regression':LinearRegression(),
                'Lasso':Lasso(),
                'Ridge':Ridge()
            }
            logging.info('Now Bifurgating the Train array and Test Array as Input and Output Variable')
            x_train,y_train,x_test,y_test = (
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )
            logging.info('Splitting Done perfectly')

            logging.info('Generating model Report')

            model_report:dict = evaluate_model(x_train = x_train,y_train = y_train,x_test = x_test,y_test = y_test,models = models)

            logging.info('Finding out Best Model with Accuracy')

            #to get the best Model Score from model_report dictatonary se
            best_model_score = max(sorted(model_report.values()))

            
            #to get best model from dict
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
                ]
            
            # Retrieve the best model based on the name
            best_model = models[best_model_name]

            
            if best_model_score>=0.4:
                logging.info('No Best Model Found')
            
            logging.info('Best Model Found')


            save_object(
                filepath = self.model_trainer_obj.trained_model_config_path,
                object = best_model
            )

            logging.info('Model File Save into Artifacts Folder')

            #to show best best model predicted score on test data
            y_pred = best_model.predict(x_test)
            r2_score_val = r2_score(y_test,y_pred)

            logging.info('best best model predicted score on test data\n%s',y_pred)

            return r2_score_val


        except Exception as e:
            raise CustomException(e,sys)
        
    
