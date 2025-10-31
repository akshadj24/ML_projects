# This wil consist the commane functionality which remain smae throughout the project implemenatation 

import numpy as np
import pandas as pd
import sys
import os
from src.exception import CustomeException
from src.logging import logging
import dill
from sklearn.metrics import r2_score,root_mean_squared_error,roc_auc_score,mean_absolute_error


def save_file(file_path,obj):
    try:

        dir_path=os.path.dirname(file_path)

        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,'wb' ) as file_obj:
            dill.dump(obj,file_obj)

    except Exception as e:
        raise CustomeException(sys,e)        


def Evalute_model(x_tarin,y_tarin,x_test,y_test,models):
    report={}
    try:
        for i in range(len(list(models))):

            model=list(models.values())[i]

            model.fit(x_tarin,y_tarin)

            y_pred_train=model.predict(x_test)


            print(f'The performace evalutiuon of the model:{list(models.keys())[i]}')
            report[list(models.keys())[i]]=r2_score(y_test,y_pred_train)
            
            print("-"*24)

        return report

    except Exception as e:
        raise CustomeException(e,sys)

def load_object(file_path):
    try:
        with open(file_path,'rb') as file_obj:
            return dill.load(file_obj)
        
    except Exception as e:
        raise CustomeException(e,sys)  
                      






        



    

