#In this data_transformation file we r converting object column of dataset to numeric column and also doing standard scaling to input variable 
#so importing all the important library which is used in data_transformation module!!!

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler,OneHotEncoder,LabelEncoder
from sklearn.pipeline import Pipeline #this class we used to create chain of steps so output of 1st step used as input of 2nd steps
from sklearn.compose import ColumnTransformer #this class we used  to combine different pipelines
from sklearn.impute import SimpleImputer #to fill null value by mean or median or mode
import os,sys
from source.exceptions import CustomException
from source.loggers import logging
from source.utils import save_object
from source.components.data_ingestion import DataIngestion,DataIngestionConfig
from sklearn.base import  BaseEstimator, TransformerMixin
from dataclasses import dataclass #this class we used to define class variable 

#creating class of DataTransformationConfig in which we r define path of preprocessor.pkl file to store in artifacts folderas class variable
@dataclass
class DataTransformationConfig():
    preprocessor_path:str = os.path.join('artifacts','preprocessor.pkl')

class MultiColumnLabelEncoder(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, x, y=None):
        return self

    def transform(self, x):
        x_encoded = np.empty(x.shape, dtype=object)
        for i in range(x.shape[1]):
            le = LabelEncoder()
            x_encoded[:, i] = le.fit_transform(x[:, i])
        return x_encoded


#creating DataTransformation class  where all methods will be defined to do transformation on dataset
class DataTransformation():
    #creating constructor method to initialize the DataTransformationConfig class object toa ccess preprocessor path
    def __init__(self):
        self.preprocessor_config_obj = DataTransformationConfig()

    #creating instance method to do transformation on dataset and get transformation/preprocessor obj as rtn
    def get_transformation_object(self):
        logging.info('Starting Data Transformation to get preprocessor object')
        try:
            logging.info('Creating numeric pipeline and categorical pipeline through Given Dataset')

            #creating object of dataingestion and retrieving path of raw dataset
            di = DataIngestion()
            raw_path,_,_ = di.initiate_data_ingestion()
            target = 'price'

            raw_df = pd.read_csv(raw_path)
            
            #selecting input variable from raw_df object
            x = raw_df.drop(target,axis=1)

            #selecting numeric column from input variable of raw_df object
            numeric_features = x.select_dtypes(exclude='object').columns.to_list()

            #selecting categorical column from input variable of raw_df object
            categorical_features = x.select_dtypes(include='object').columns.to_list()


            #now creating numeric pipeline they fill null value by median and do scaling in it
            numeric_pipeline = Pipeline(steps=[
                ('imputing',SimpleImputer(strategy='median')), #filling null by median
                ('scaling',StandardScaler(with_mean=False)) #doing standard scaling to numeric features
            ])

            #now creating categorical pipeline they fill null value by mode and do convert object to numeric by labelencoder or onehotencoder and also do scaling in it
            categorical_pipeline = Pipeline(steps=[
                ('imputer',SimpleImputer(strategy='most_frequent')), #for missing values we are filling with most frequent
                ('labelencoder',MultiColumnLabelEncoder()), #converting category into numerical form
                ('scaling',StandardScaler(with_mean=False))#doing standard scaling to numeric features
            ])

            logging.info('Pipeline for numeric and categorical feature Completed Successfully')

            logging.info('Combine both Pipeline to generate preprocessor object')
            
            #combine both pipeline to get preprocess object using ColumnTransformer
            preprocessor = ColumnTransformer(transformers=[
                ('numeric_pipeline',numeric_pipeline,numeric_features),
                ('categorical_pipeline',categorical_pipeline,categorical_features)
            ])
            
            return preprocessor
        
        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_data_transformation(self,raw_path,train_path,test_path):
        logging.info('Initiating the Data Transformation')
        try:
            train_df = pd.read_csv(train_path)
            test_df  = pd.read_csv(test_path)

            logging.info('Train_set and test_set Readed Sucessfully...')

            target = 'price'

            logging.info('Selecting train_df se input and output feature')

            #selecting train_input feature and train_output feature from train_df
            input_feature_train_df = train_df.drop(target,axis=1)
            target_feature_train_df = train_df[target]

            logging.info('train_df se input and output feature selected successfully...')

            logging.info('Now Selecting test_df se input and output feature')
            input_feature_test_df = test_df.drop(target,axis=1)
            target_feature_test_df = test_df[target]
            logging.info('test_df se input and output feature selected successfully...')


            logging.info('Now doing Preprocessing to input feature of train_df and test_df')
            preprocessing_object = self.get_transformation_object()

            input_feature_train_array = preprocessing_object.fit_transform(input_feature_train_df) #train data we perform fit_transform built in method of preprocessor object
            input_feature_test_array = preprocessing_object.transform(input_feature_test_df)  #test data we perform transform built in method of preprocessor object

            logging.info('combining input_feature_train_array with target_feature_train_df lly for test_array also preparing')

            train_array = np.c_[input_feature_train_array,np.array(target_feature_train_df)]
            test_array = np.c_[input_feature_test_array,np.array(target_feature_test_df)]

            logging.info('Now Saving the preprocessor object to artifact folder')

            save_object (
                filepath = self.preprocessor_config_obj.preprocessor_path,
                object = preprocessing_object
            )

            return(
                train_array,
                test_array,
                self.preprocessor_config_obj.preprocessor_path
            )


        except Exception as e:
            raise CustomException(e,sys)

