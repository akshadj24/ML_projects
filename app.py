from flask import Flask,redirect,request,render_template,url_for# type: ignore
from src.logging import logging
from src.exception import CustomeException
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from src.components.pipeline.predict_pipeline import Customedata,predict_pipline
import sys


application=Flask(__name__)

app=application
@app.route('/')
def method_name():
    return  render_template('index.html')

@app.route('/fill_form',methods=['GET','POST'])
def form_details():
    try:

        if request.method=='GET':
            return render_template('form.html')
            
        else:
                
                
            gender=request.form['gender']
            race_ethnicity=request.form['race_ethnicity']
            parental_level_of_education=request.form['parental_level_of_education']
            lunch=request.form['lunch']
            test_preparation_course=request.form['test_preparation_course']
            writing_score=request.form['writing_score']
            reading_score=request.form['reading_score']
                
               

            data=Customedata(race_ethnicity,gender,reading_score,writing_score,parental_level_of_education,lunch,test_preparation_course)
                
            dataframe=data.DataFarme()

            p1=predict_pipline()
            math_score=p1.predict(dataframe)

            return render_template('form.html',score=math_score[0])
            
    except Exception as e:
            raise CustomeException(e,sys)    


if __name__=='__main__':
    app.run(host="0.0.0.0",debug=True)


          
    






