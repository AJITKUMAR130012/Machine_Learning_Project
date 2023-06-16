import streamlit as st
import pickle
import numpy as np

# import the model
pipe = pickle.load(open('GradientBoostingRegressor.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))

st.title("Car Price Predictor")

name = st.selectbox('Car Name',df['name'].unique())

company = st.selectbox('Brand', df["company"].unique())

year = (st.number_input('Enter the current year'))

km_driven = (st.number_input('Enter the kilometer'))

fuel_type = st.selectbox('Fuel_type', df["fuel_type"].unique())

if st.button('Predict Price'):
    year=int(year)
    km_driven=int(km_driven)

    query = np.array([name,company,year,km_driven,fuel_type])
    query = query.reshape(1,5)
    st.title("The predicted price of this configuration is " + str(pipe.predict(query)))


