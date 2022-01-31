# ---- Import libraries ----
import streamlit as st
import plotly.express as px
import pandas as pd
from pages import dataupdate


# ---- Functions ----
def app(df):
   
    fig1 = px.line(
        df,x='Fecha Limitacion', y="Estimacion Energia Vertida (mwh)",
        labels={'Estimacion Energia Vertida (mwh)':'MWh','Fecha Limitacion':'Fecha'},
        line_group='Planta',
        title='Estimacion Energia Vertida (Mwh) por Planta',
        color='Planta',
        
        
    )
    dfm=df
    dfm["Fecha Limitacion"] = pd.DatetimeIndex(dfm["Fecha Limitacion"])
    fig2 = px.line(
        dfm.set_index("Fecha Limitacion").groupby([pd.Grouper(freq = "M"), "Planta"]).sum().reset_index(),x='Fecha Limitacion', y="Estimacion Energia Vertida (mwh)",
        labels={'Estimacion Energia Vertida (mwh)':'MWh','Fecha Limitacion':'Fecha'},
        line_group='Planta',
        color='Planta'
    )
    fig3 = px.line(
        df.set_index("Fecha Limitacion").groupby([pd.Grouper(freq = "D")])["Estimacion Energia Vertida (mwh)"].sum().reset_index(),
        x='Fecha Limitacion', y="Estimacion Energia Vertida (mwh)",
        labels={'Estimacion Energia Vertida (mwh)':'Mwh','Fecha Limitacion':'Fecha'},
        title='Estimacion Energia Vertida (Mwh) total para la generacion renovable',
    )
    fig4 = px.line(
        df.resample("M",on= "Fecha Limitacion").sum().reset_index() ,
        x='Fecha Limitacion', y="Estimacion Energia Vertida (mwh)",
        labels={'Estimacion Energia Vertida (mwh)':'Mwh','Planta':'Planta'}
    )

    fig5 = px.bar(
        df.groupby(['Planta'])["Estimacion Energia Vertida (mwh)"].sum().reset_index().sort_values(by=['Estimacion Energia Vertida (mwh)'],ascending=False),
        x="Planta",
        y="Estimacion Energia Vertida (mwh)",
        labels={'Estimacion Energia Vertida (mwh)':'MWh','Planta':'Planta'},
        title="Estimacion Energia Vertida (Mwh) por Planta",
        color="Planta"
    )
    fig6 = px.box(
        df[df!=0],
        x='Planta', y="Estimacion Energia Vertida (mwh)",
        labels={'Estimacion Energia Vertida (mwh)':'Mwh','Planta':'Planta'},
        color='Planta',
    )
# ---- Selectbox ----
    st.markdown("<h2 style='text-align: center;'> Limitaciones diarias </h2>", unsafe_allow_html=True)
    selection_plot = st.selectbox(
        "Seleccione un tipo de grafico",
        ["Linea (Por Planta Diaria)",
        "Linea (Por Planta Mensual)",
        "Linea (Total Diaria)",
        "Linea (Total Mensual)",
        "Barras (Por Planta)",
        "BoxPlot"])

# ---- Seleccion de grafico ----
    if selection_plot == "Linea (Por Planta Diaria)":
        st.plotly_chart(fig1)
        data_excel =  dataupdate.to_excel(df)
        st.download_button(
            "Descargar .xlsx",
            data_excel,
            "Limitaciones.xlsx",
            "text/csv",
            key='download-xlsx'
        )
    elif selection_plot == "Linea (Por Planta Mensual)":
        st.plotly_chart(fig2)
        df2 = dfm.set_index("Fecha Limitacion").groupby([pd.Grouper(freq = "M"), "Planta"]).sum().reset_index()
        df2 = df2.loc[:,["Fecha Limitacion","Planta","Tiempo Limitado (hrs)","Estimacion Energia Vertida (mwh)"]]
        data_excel =  dataupdate.to_excel(df2)
        st.download_button(
            "Descargar .xlsx",
            data_excel,
            "Limitaciones.xlsx",
            "text/csv",
            key='download-xlsx'
        )
    elif selection_plot == "Linea (Total Diaria)":
        st.plotly_chart(fig3)
        df3 = df.set_index("Fecha Limitacion").groupby([pd.Grouper(freq = "D")])["Estimacion Energia Vertida (mwh)"].sum().reset_index()
        data_excel =  dataupdate.to_excel(df3)
        st.download_button(
            "Descargar .xlsx",
            data_excel,
            "Limitaciones.xlsx",
            "text/csv",
            key='download-xlsx'
        )
    elif selection_plot == "Linea (Total Mensual)":
        st.plotly_chart(fig4)
        data_excel =  dataupdate.to_excel(df.resample("M",on= "Fecha Limitacion").sum().reset_index())
        st.download_button(
            "Descargar .xlsx",
            data_excel,
            "Limitaciones.xlsx",
            "text/csv",
            key='download-xlsx'
        )
    elif selection_plot == "Barras (Por Planta)":
        st.plotly_chart(fig5)
    elif selection_plot == "BoxPlot":
        st.plotly_chart(fig6)




        


        

    