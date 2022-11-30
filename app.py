import streamlit as st
import pandas as pd
import numpy as np


st.write("""
# Numerical Division App

This app computes the legible division of Two numbers
""")
#Get Input

st.header('User Input for Division')

def user_input():
    num_1 = st.number_input("First Number (Dividend)",min_value=-1.797e+308,max_value=1.797e+308)
    num_2 = st.number_input("Second Number (Divisor)",min_value=-1.797e+308,max_value=1.797e+308)
    
    data = {'num_1': float(num_1),
            'num_2': float(num_2)
            }
    
    return data

df = user_input()

st.subheader('Input by User')
st.write(df) 

st.subheader('Computed Value')

if df['num_2']==0:
    st.write(f"Result: Invalid input 0 for operand 2. Try Again")    
else:

    prediction = df['num_1']/df['num_2']
    st.write("Result:",prediction)
    st.write(f" Division of {df['num_1']} by {df['num_1']}: {prediction}")
