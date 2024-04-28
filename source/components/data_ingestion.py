#data_ingestion file means we r reading data from different differnt source such as Database server,local system or S3 bucket server...so on
#in this file we r reading data from local system..then splitting data into train_set,test_set,raw_set 

#importing all the important library which is used in data_ingestion module
import pandas as pd,numpy as np
from sklearn.model_selection import train_test_split
from source.loggers import logging
from source.exceptions import CustomException
from dataclasses import dataclass #this class we used to define class variable
import os,sys


#creating class of DataingestionConfig in which we r defining where to store test,raw,train..data path as a class variable
class DataIngestionConfig():
    raw_data_path:str = os.path.join('artifacts','raw.csv')
    train_data_path:str = os.path.join('artifacts','train.csv')
    test_data_path:str = os.path.join('artifacts','test.csv')


#now creating another class dataingestion where we start data ingestion process
class DataIngestion():
    #now creating constructor method to initialize the DataIngestionConfig class object to access the class variable
    def __init__(self):
        self.data_ingestion_config_obj  = DataIngestionConfig()

    #creating another instance method that start initiating the dataingestion process
    def initiate_data_ingestion(self):
        logging.info('Data Ingestion Process is initiated....')
        try:
            logging.info('Reading dataset From Local System')
            df = pd.read_csv(r'D:\AUTOMOBILE_PROJECT_ML\notebook\data\Automobile_data.csv')

            logging.info('Successfully data readed from local system\n%s', df.head())

            logging.info('now creating artifacts folder to store  our datasets')
            
            os.makedirs(os.path.dirname(self.data_ingestion_config_obj.raw_data_path),exist_ok=True)

            df.to_csv(self.data_ingestion_config_obj.raw_data_path,index=False,header=True)
            logging.info('Raw Data save into artifacts folder')

            logging.info('Dividing the data into  Train and Test set')
            train_set,test_set = train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.data_ingestion_config_obj.train_data_path,index=False,header=True)
            test_set.to_csv(self.data_ingestion_config_obj.test_data_path,index=False,header=True)

            logging.info('Data Ingestion Done SuccessFully')

        except Exception as e:
            raise CustomException(e,sys)