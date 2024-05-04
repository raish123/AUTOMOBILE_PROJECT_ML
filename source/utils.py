from source.exceptions import CustomException
import os,sys
from source.loggers import logging
import dill
from sklearn.metrics import r2_score,mean_squared_error




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
    



def evaluate_model(x_train ,y_train ,x_test ,y_test ,models):
    report = {}

    try:   
        for i in range(len(models)):
            model = list(models.values())[i]

            #now training the model by using fit() built in method of models
            model.fit(x_train,y_train)

            #now testing the model and predicting the output variable
            y_train_pred = model.predict(x_train)

            y_test_pred = model.predict(x_test)

            #now checking the accuracy of model
            train_model_score = r2_score(y_train,y_train_pred)
            test_model_score = r2_score(y_test,y_test_pred)

            logging.info('appending scores to dictionary')
            
            report[list(models.keys())[i]]= test_model_score

        return report
    
    except Exception as e:
        raise CustomException(e,sys)