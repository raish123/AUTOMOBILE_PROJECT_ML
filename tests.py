from source.loggers import logging
from source.exceptions import CustomException
import os ,sys
from source.components.data_ingestion import DataIngestion,DataIngestionConfig
from source.components.data_transformation import DataTransformation,DataIngestionConfig


def main():
    logging.info('Just Checking artifacts Created Or not')
    try:
        di = DataIngestion()
        raw_path,train_path,test_path = di.initiate_data_ingestion()

        #creating object of DataTransformation class
        dt = DataTransformation()
        train_array,test_array,preprocessor_filepath = dt.initiate_data_transformation(raw_path,train_path,test_path)

        logging.info('train array will be\n%s',train_array)

    except Exception as e:
        raise CustomException(e,sys)




if __name__ == '__main__':
    main()