import os
import sys
from src.exception import CustomeException
from src.logging import logging
from sklearn.linear_model import LinearRegression,Lasso,Ridge,ElasticNet
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor,AdaBoostRegressor
from xgboost import XGBRegressor
from sklearn.tree import DecisionTreeRegressor
from dataclasses import dataclass
# from src.components.data_transformation import Data_transformation
# from src.components.data_Ingestion import DataIngection
from sklearn.metrics import r2_score,root_mean_squared_error,roc_auc_score,mean_absolute_error
import pandas as pd
from src.utils import Evalute_model,save_file


class Model_Train:
    Model:str=os.path.join('artifacts/model.pkl')
    
class Model_Trainning:

    def __init__(self):
        self.model_path=Model_Train()


    def Trainning(self,train_array,test_array):

        try:
          
            x_train,y_tarin,x_test,y_test=(train_array[:,:-1],train_array[:,-1],test_array[:,:-1],test_array[:,-1])


            model={
                "Linear_Regression":LinearRegression(),
                "XGB_Regressor":XGBRegressor(),
                "Elastic_net":ElasticNet(),
                "lasso":Lasso(),
                "Ridge":Ridge(),
                "AdaBoost_Regressor":AdaBoostRegressor(),
                "Decision_Tree":DecisionTreeRegressor(),
                "S_V_M":SVR(),
                "Random_Forest":RandomForestRegressor()}
            
            

            model_report=Evalute_model(x_train,y_tarin,x_test,y_test,models=model)

            best_score=max(list(model_report.values()))

            Best_model_name=list(model_report.keys())[list(model_report.values()).index(max(list(model_report.values())))]

            
            save_file(file_path=self.model_path.Model,obj=model[Best_model_name])
                        
            return best_score
        

        except Exception as e:
            raise CustomeException(sys,e)
        




        



        


