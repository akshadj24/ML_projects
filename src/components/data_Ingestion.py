# lets get started with the implemenation of the data ingection 
import os
import sys 
from src.exception import CustomeException
from src.logging import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses  import dataclass

@dataclass
class DataIngectionConfig:
    # all the output will be stored in the artifactr folder
    train_data_path:str=os.path.join('artifact','Train.csv')
    test_data_path:str=os.path.join('artifact','test.csv')
    raw_data_path:str=os.path.join('artifact','data.csv')

class DataIngection:
    def __init__(self):
        self.ingestion_config=DataIngectionConfig()


    def intitate_data_ingestion(self):
           logging.info("Entered into data ingection method )r component")

           try:
                df=pd.read_csv('NoteBook\Data\stud.csv')
                logging.info('Dataset has been read sucessfully as Dataframe')

                os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
                df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

                logging.info("train_test_splitting")

                train_set,tets_set=train_test_split(df,test_size=0.30,random_state=42)

                train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
                tets_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
                
                logging.info("Train and test data stored in the respective csv files")

                return(
                    self.ingestion_config.train_data_path,
                    self.ingestion_config.test_data_path,
                    self.ingestion_config.raw_data_path,

                )
                
           except Exception as e:
              raise CustomeException(e,sys)
           
if __name__=='__main__':
     D1=DataIngection()

     D1.intitate_data_ingestion()


                