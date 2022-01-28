import pandas as pd 
import streamlit as st 
from st_aggrid import AgGrid

st.set_page_config(page_title="Netflix Shows", layout="wide") 
st.title("ODS Limitaciones")

shows = pd.read_excel("data/limitaciones.xlsx",engine="openpyxl")

AgGrid(shows)

# my