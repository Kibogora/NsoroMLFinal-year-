import streamlit as st
import pandas as pd
import numpy as np
import joblib
import pickle

st.title('Air Quality Predictor')
#st.image(""""C:\Users\USER1\Desktop\download.jpeg"""")
st.header('This app uses 4 inputs to predict air quality in cities around the world using a model built on satellite (Zindi) data. use the form below to get started!')
st.text("Created by Planet Protectors Study Group")

# Add navigation links in the sidebar
st.sidebar.selectbox("Navigation", ["Home", "About", "Contact"])

model = pickle.load(open('Gradient_Boost_Model.pkl', 'rb'))

cols=['channel_sales', 'date_activ', 'date_end', 'cons_last_month', 'forecast_cons_12m', 'forecast_cons_year', 'mean_6m_price_peak', 'mean_3m_price_peak', 'churn']    

# Define the prediction function
def predict( channel_sales, cons_last_month, mean_6m_price_peak, mean_3m_price_peak, churn):
    
    prediction = model.predict([[channel_sales, cons_last_month, mean_6m_price_peak, mean_3m_price_peak, churn]])
    
    return prediction


precipitable_water_entire_atmosphere = st.number_input('Precipitable water', 0.00, 100.00)
relative_humidity_2m_above_ground = st.number_input('Relative humidity', 0.00, 100.00)
specific_humidity_2m_above_ground = st.number_input('Specific humidity', 0.00, 100.00)
temperature_2m_above_ground = st.number_input('Temperature', 0.00, 100.00)
gender = st.selectbox("gender", options=["male","female"])
age = st.slider("age", 0, 70)

if st.button('Predict number of consultant'):
    a_q = predict(channel_sales, cons_last_month, mean_6m_price_peak, mean_3m_price_peak, churn)
    st.success(f'The predicted number of consultant is {a_q[0]:.2f} PM2.5')











    
    
    
    
    
    
    
    
    
    
    