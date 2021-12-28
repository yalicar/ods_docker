# ---- Import libraries ----
import streamlit as st
import database
import pandas as pd

# ---- formato de la pagina ----
st.set_page_config(layout="wide")

# ---- Custom imports -----
from multipage import MultiPage
from pages import tablas,graficas,dataupdate

# ---- Connect to data base ----

df = database.connect_to_database()
df.fillna(0, inplace=True)
df['Fecha'] = pd.to_datetime(df['Fecha'] ,errors = 'coerce',format = '%Y-%m-%d')



if df.empty:
    st.text("Por favor, cargue la base de datos primero.")
else:    
    # ---- Create an instance of the app ----
    app = MultiPage.filter(df)

    # ---- Add all your application ----

    #app.add_page("Mapa",mapa.app)
    app.add_page("Tablas",tablas.app)
    app.add_page("Gráficas",graficas.app)
    app.add_page("Actualizar datos",dataupdate.app)


    # ---- The main app ----
    app.run()
