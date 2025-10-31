import sys
from src.exception import CustomeException
from src.logging import logging
import pandas as pd
from src.utils import load_object


class predict_pipline:
    
    def __init__(self):
        
        pass
    def predict(self,features):
        try:
            model_path='artifacts/model.pkl'
            preprocessor_path='artifact/preprocessor.pkl'

            model=load_object(model_path)
            preprocessor=load_object(preprocessor_path)

            input=preprocessor.transform(features)

            prediction=model.predict(input)

            return prediction
        
        except Exception as e:
            raise CustomeException(e,sys)   

class Customedata:

    def __init__(self,race_ethnicity,gender,reading_score,writing_score,parental_level_of_education,lunch,test_preparation_course):
        
        self.gender=gender
        self.race_ethnicity=race_ethnicity
        self.parental_level_of_education=parental_level_of_education
        self.lunch=lunch
        self.test_preparation_course=test_preparation_course
        self.reading_score=reading_score
        self.writing_score=writing_score
        
        


    def DataFarme(self):
        try:
            features={
            
            'gender':[self.gender],
            'race_ethnicity':[self.race_ethnicity],
            'parental_level_of_education':[self.parental_level_of_education],
            'lunch':[self.lunch],
            'test_preparation_course':[self.test_preparation_course],
            'writing_score':[self.writing_score],
            'reading_score':[self.reading_score],
            
            
            }    

            input_fields=pd.DataFrame(features)

            return input_fields
        
        except Exception as e:
            raise CustomeException(e,sys)

        




        