# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 17:35:32 2023

@author: HP
"""

from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json

app = FastAPI()

class model_input(BaseModel):
    
    Pergnancies : int
    Glucose : int
    BloodPressure : int
    SkinThickness : int
    Insulin : int
    BMI : float
    DiabetesPedigreeFunction : float
    Age = int
    
diabetes_model = pickle.load(open('diabetesmodel.sav' , 'rb'))

@app.post('/diabetes_prediction')
def diabetes_pred(input_parameters : model_input):
    input_data = input_parameters.json()
    input_dictonary = json.loads(input_data)
    
    preg = input_dictonary['Pergnancies']
    glu = input_dictonary['Glucose']
    bp = input_dictonary['BloodPressure']
    skin = input_dictonary['SkinThickness']
    insulin = input_dictonary['Insulin']
    bmi = input_dictonary['BMI']
    dpf = input_dictonary['DiabetesPedigreeFunction']
    age = input_dictonary['Age']
    
    
    input_list = [preg,glu,bp,skin,insulin,bmi,dpf,age]
    
    prediction = diabetes_model.predict([input_list])
    
    if prediction[0] == 0:
        return 'The person is not diabetic'
    else:
        return 'The person is diabetic'
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    