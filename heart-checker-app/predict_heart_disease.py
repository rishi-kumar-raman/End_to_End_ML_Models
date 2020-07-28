import streamlit as st
import pandas as pd
import numpy as np
import time
import pickle

st.title('Predict Heart Disease')
st.text('Please enter the Following Info to know the result')
model=pickle.load(open('logistic_regression.pkl','rb'))
# st.write(str(model))

age=st.text_input(label='Age',value="0")

sex=st.selectbox('Gender',["Male","Female"])
if(sex=="Male"):
    sex="0"
else:
    sex="1"
chest_pain=st.text_input(label='Chest_pain',value="0")
trestbps=st.text_input(label='Resting blood Pressure',value="0")
cholestrol=st.text_input(label='Serum in mg/dl',value="0")
fbs=st.selectbox('is fasting blood sugar greater than 120 mg/dl',["0","1"])
restecg=st.selectbox('Resting ECG results',["0","1","2"])
thalach=st.text_input(label='Maximum Heart Rate Achieved',value="0")

exang=st.selectbox('Excercise Induced Angina',["0","1"])
oldpeak=st.text_input(label='ST Depression Induced by exercise relative to Rest',value="0")
slope=st.selectbox('The slope of peak exercise ST segment',["0","1","2"])
ca=st.selectbox('No of major vessels coloured',["0","1","2","3","4"])
thal=st.selectbox('Thal',["0","1","2","3"])

pred=model.predict([[int(age),int(sex),float(chest_pain),int(trestbps),int(cholestrol),int(fbs),int(restecg),int(thalach),int(exang),float(oldpeak),int(slope),int(ca),int(thal)]])

if(st.button("Check the patient")):
    with st.spinner("Predicting the Result"):
        time.sleep(1)
    if(pred==0):
        st.header('Patient has a heart Problem')
    else:
        st.header('Patient is Healthy')
