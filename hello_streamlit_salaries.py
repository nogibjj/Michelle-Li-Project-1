"""
streamlit run hello_streamlit_salaries.py --server.enableCORS=false
"""
import streamlit as st
from dblib.salaries import load_data

dataframe = load_data()
st.table(dataframe.head())
