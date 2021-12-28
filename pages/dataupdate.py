# ---- Import libraries ----
from json import encoder
import streamlit as st
import database
import pandas as pd

# ---- Load data ----
#@st.cache(allow_output_mutation=True)
def app(df):
   csv=df.to_csv(index=False)
   st.download_button(
       "Descargar CSV",
       csv,
       "Limitaciones.csv",
       "text/csv",
       key='download-csv'
   )
   df2 = None
   df2 =st.file_uploader("Upload a file", type=["csv"])
   
   if df2 is None:
       st.write("No hay datos para mostrar")
   else:
       st.write(df)
       df2=pd.read_csv(df2)

       pwd = st.text_input("Ingrese la contraseña",type="password")
       if pwd == "1234Abc.":
           btn = st.button("Actualizar base de datos")
           if btn:
               database.upload_to_database(df2)
               st.write("Base de datos actualizada")
       else:
           st.write("Contraseña incorrecta")


   return None
