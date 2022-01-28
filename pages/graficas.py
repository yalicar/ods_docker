# ---- Import libraries ----
import streamlit as st
import plotly.express as px
import pandas as pd


# ---- Functions ----
def app(df):
    #st.markdown("<h1 style='text-align: center;'> Gráficas </h1>", unsafe_allow_html=True)
    
    fig1 = px.line(
        df,x='Fecha Limitacion', y="Estimacion Energia Vertida (mwh)",
        labels={'Estimacion Energia Vertida (mwh)':'MWh','Fecha Limitacion':'Fecha'},
        line_group='Planta',
        title='Estimacion Energia Vertida (Mwh) por Planta',
        color='Planta'
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
        df.groupby(['Fecha Limitacion'])["Estimacion Energia Vertida (mwh)"].sum().reset_index(),
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
    
   
   


 
    st.markdown("<h2 style='text-align: center;'> Limitaciones diarias </h2>", unsafe_allow_html=True)
    selection_plot = st.selectbox(
        "Seleccione un tipo de grafico",
        ["Linea (Por Planta Diaria)",
        "Linea (Por Planta Mensual)",
        "Linea (Total Diaria)",
        "Linea (Total Mensual)",
        "Barras (Por Planta)",
        "BoxPlot"])

    if selection_plot == "Linea (Por Planta Diaria)":
        st.plotly_chart(fig1)
    elif selection_plot == "Linea (Por Planta Mensual)":
        st.plotly_chart(fig2)
    elif selection_plot == "Linea (Total Diaria)":
        st.plotly_chart(fig3)
    elif selection_plot == "Linea (Total Mensual)":
        st.plotly_chart(fig4)
    elif selection_plot == "Barras (Por Planta)":
        st.plotly_chart(fig5)
    elif selection_plot == "BoxPlot":
        st.plotly_chart(fig6)




        


        

    