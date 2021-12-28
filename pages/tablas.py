# ---- Import libraries ----
import streamlit as st

def app(df):
    df_grouped_plant = df.groupby(["Planta"])[["Energía Vertida (MWh)","Tiempo de Limitación (h)"]].sum().reset_index()
    col1,col2 = st.columns(2)
    with col1:
        st.markdown("<h1 style='text-align: center;'> Resumen por planta </h1>", unsafe_allow_html=True)
        st.dataframe(df_grouped_plant.sort_values(by=['Energía Vertida (MWh)'],ascending=False).style.format({'Energia':'{:,.2f}','TiempoLimitacion_Hrs':'{:,.0f}'}))
    with col2:
        st.text("")
    st.download_button(
       "Descargar tabla",
       df_grouped_plant.to_csv(),
       "DATA.csv",
       "text/csv",
       key='download-csv'
       )

    st.markdown("<h1 style='text-align: center;'> Tabla de limitaciones raw data</h1>", unsafe_allow_html=True)
    st.dataframe(df)
    st.download_button(
       "Descargar tabla",
       df.to_csv(),
       "DATA.csv",
       "text/csv",
       key='download-csv'
       )