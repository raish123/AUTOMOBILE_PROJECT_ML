from source.loggers import logging
from source.exceptions import CustomException
import os ,sys
from source.components.data_ingestion import DataIngestion,DataIngestionConfig


def main():
    logging.info('Just Checking artifacts Created Or not')
    try:
        di = DataIngestion()
        di.initiate_data_ingestion()

    except Exception as e:
        raise CustomException(e,sys)




if __name__ == '__main__':
    main()