from sqlalchemy import create_engine
import streamlit as st
import pandas as pd


def upload_to_database(df):
    """
    Upload to a database.
    """
    #df = connect_to_database()
    engine = create_engine("mysql://ycardenas:1234Abc.@190.92.22.22/SolarDB")
    cnx = engine.connect()
    df.to_sql(name='Limitaciones_ODS',con=cnx,if_exists='replace',index=False)
    cnx.close()
    return None

#@st.cache(allow_output_mutation=True)
def connect_to_database():

    # ---- Connect to the database ----
    engine = create_engine("mysql://ycardenas:1234Abc.@190.92.22.22/SolarDB")
    cnx = engine.connect()

    # ---- Consulta a la base de datos ----
    frase = "SELECT * from Limitaciones_ODS"
    df= pd.read_sql_query(frase, cnx)
    cnx.close()
    return df
