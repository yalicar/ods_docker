# ---- Import libraries ----
from json import encoder
import streamlit as st
import database
import pandas as pd

import pandas as pd
from io import BytesIO
from pyxlsb import open_workbook as open_xlsb
import streamlit as st

# ---- Load data ----
def to_excel(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name='Sheet1')
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']
    format1 = workbook.add_format({'num_format': '0.00'}) 
    worksheet.set_column('A:A', None, format1)  
    writer.save()
    processed_data = output.getvalue()
    return processed_data 

#@st.cache(allow_output_mutation=True)
def app(df):
   #csv=df.to_csv(index=False)

   data_excel = to_excel(df)

   st.download_button(
       "Descargar .xlsx",
       data_excel,
       "Limitaciones.xlsx",
       "text/csv",
       key='download-xlsx'
   )
   df2 = None
   df2 =st.file_uploader("Upload a file", type=["xlsx"])
   
   if df2 is None:
       st.write("No hay datos para mostrar")
   else:
       st.write(df)
       df2=pd.read_excel(df2)

       pwd = st.text_input("Ingrese la contraseña",type="password")
       if pwd:
           if pwd == "1234Abc.":
               btn = st.button("Actualizar base de datos")
               if btn:
                   database.upload_to_database(df2)
                   st.write("Base de datos actualizada")
           else:
               st.write("Contraseña incorrecta")

        


   return None
