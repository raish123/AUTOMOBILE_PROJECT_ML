from source.exceptions import CustomException
import os,sys
from source.loggers import logging
import dill




def save_object(filepath,object):
    logging.info('Saving The file object into Artifacts Folder')
    try:
        if not os.path.exists('artifacts'):
            os.makedirs('artifacts',exist_ok=True)

        with open(filepath,'wb') as file:
            dill.dump(object,file)

        logging.info('File saved successfully to Artifact Folder: %s', object)
    except Exception as e:
        raise CustomException(e,sys)