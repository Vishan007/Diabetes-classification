import numpy as np
import pickle
import streamlit as st

##loading the saved model
loaded_model = pickle.load(open('C:/Users/HP/Desktop/Projects/Multiple disease pred/diabetesmodel.sav' , 'rb'))

def diabetes_prediction(input_data):
    
    input_data_array = np.asarray(input_data)
    input_data_reshaped = input_data_array.reshape(1,-1)
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)
    if (prediction[0] == 1):
      return 'the person is diabetic'
    else:
      return 'the person is no diabetic'
      
      
      
def main():
    
    ##giving a title
    st.title('Diabetes prediction web app')
    
    ##getting the input data from the user
    Pergnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose level')
    BloodPressure = st.text_input('BloodPressure level')
    SkinThickness = st.text_input('SkinThickness')
    Insulin = st.text_input('Insulin level')
    BMI = st.text_input('BMI value')
    DiabetesPedigreeFunction = st.text_input('DiabetesPedigreeFunction')
    Age = st.text_input('Age')
    
    ##code for prediction
    diagnosis = ''
    ##creating a button for prediction
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([Pergnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]) 
    
    st.success(diagnosis)
    
    
    
if __name__ == '__main__':
    main()