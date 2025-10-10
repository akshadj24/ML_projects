# data transformation
import pandas as pd 
import numpy as np
import sys
import os
from src.logging import logging
from src.exception import CustomeException
from data_Ingestion import DataIngection
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from src.utils import save_file

class Data_transformation:
    def __init__(self):
    #    self.train_data_path=os.path('artifact/Train.csv')
       self.preprocessor_path=os.path.join('artifact/preprocessor.pkl')
       

    def trasform_data(self):
        try:
            logging.info("Entered into the datatraformation")
            
          

            cat_features1=['gender','race_ethnicity','parental_level_of_education','lunch','test_preparation_course']
            num_features1=[ 'writing_score','reading_score']
            
            cat_pipeline=Pipeline(steps=[
                ("inputer",SimpleImputer(strategy="most_frequent")),
                ("onehot",OneHotEncoder(handle_unknown='ignore')),
                ("StandardScaler",StandardScaler(with_mean=False))
            ])

            num_pipeline=Pipeline(steps=[
                ("inputer",SimpleImputer(strategy='mean')),
                ("StandardScaler",StandardScaler())
            ])


            transformer=ColumnTransformer([
                ("numerical_pipeline",num_pipeline,num_features1),
                ('categorical_pipeline',cat_pipeline,cat_features1)
            ])


            return transformer
        
        except Exception as e:
           raise CustomeException(sys,e)

    def Initiate_trsformation(self,train_path,test_path):
            

        try:
            logging.info("datatraformation started")

            df_train=pd.read_csv(train_path)
            df_test=pd.read_csv(test_path)

            df_feature_train=df_train.drop('math_score',axis=1)
            df_feature_train_target=df_train['math_score']

            df_feature_test=df_test.drop('math_score',axis=1)
            df_feature_test_target=df_test['math_score']


            tarnformer=self.trasform_data()

            df_train_transformed=tarnformer.fit_transform(df_feature_train)
            df_test_transformed=tarnformer.transform(df_feature_test)
            

            logging.info("Transformation of the train and the test data done Sucessfully!!")


            logging.info("Combining the target and the independent features")

            train_transformed_arr=np.c_[
                df_train_transformed,np.array(df_feature_train_target)          ]


            test_transformed_arr=np.c_[
           df_test_transformed,np.array(df_feature_test_target)
            ]

            save_file(self.preprocessor_path,tarnformer)
            
            return(
                train_transformed_arr,test_transformed_arr,self.preprocessor_path
            )
        
        except Exception as e:
             raise CustomeException(sys,e)

# if __name__=="__main__":

#     d1=Data_transformation()

#     ding=DataIngection()

#     train_path=ding.ingestion_config.train_data_path()
#     test_path=ding.ingestion_config.test_data_path()


#     d1.Initiate_trsformation(train_path,test_path)

