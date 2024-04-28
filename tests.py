from source.loggers import logging
from source.exceptions import CustomException
import os ,sys


def main():
    logging.info('Just Checking Logs Creating Or not')
    try:
        a=1/0

    except Exception as e:
        raise CustomException(e,sys)




if __name__ == '__main__':
    main()