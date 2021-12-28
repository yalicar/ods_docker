# ---- Import libraries ----
import streamlit as st
import plotly.express as px
import pandas as pd


# ---- Functions ----
def app(df):
    st.markdown("<h1 style='text-align: center;'> Gráficas </h1>", unsafe_allow_html=True)
    
    fig1 = px.line(
        df,x='Fecha', y="Energía Vertida (MWh)",
        labels={'Energía Vertida (MWh)':'MWh','Fecha':'Fecha'},
        line_group='Planta',
        color='Planta'
    )
    fig2 = px.bar(
        df.groupby(['Planta'])["Energía Vertida (MWh)"].sum().reset_index().sort_values(by=['Energía Vertida (MWh)'],ascending=False),
        x="Planta",
        y="Energía Vertida (MWh)",
        labels={'Energía Vertida (MWh)':'MWh','Planta':'Planta'},
        color="Planta"
    )
    fig3 = px.line(
        df.groupby(['Fecha'])["Energía Vertida (MWh)"].sum().reset_index(),
        x='Fecha', y="Energía Vertida (MWh)",
        labels={'Energía Vertida (MWh)':'Mwh','Fecha':'Fecha'},
    )
    fig4 = px.line(
        df.resample("M",on= "Fecha").sum().reset_index() ,
        x='Fecha', y="Energía Vertida (MWh)",
        labels={'Energía Vertida (MWh)':'Mwh','Planta':'Planta'}
    )
    fig5 = px.box(
        df[df!=0],
        x='Planta', y="Energía Vertida (MWh)",
        labels={'Energía Vertida (MWh)':'Mwh','Planta':'Planta'},
        color='Planta'
    )
    dfm=df
    dfm.Fecha = pd.DatetimeIndex(dfm.Fecha)
    fig6 = px.line(
        dfm.set_index("Fecha").groupby([pd.Grouper(freq = "M"), "Planta"]).sum().reset_index(),x='Fecha', y="Energía Vertida (MWh)",
        labels={'Energía Vertida (MWh)':'MWh','Fecha':'Fecha'},
        line_group='Planta',
        color='Planta'
    )
   
 


    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<h1 style='text-align: center;'> Limitaciones diarias </h1>", unsafe_allow_html=True)
        st.plotly_chart(fig3)
        st.markdown("<h1 style='text-align: center;'> Limitaciones diarias </h1>", unsafe_allow_html=True)
        st.plotly_chart(fig1)
        st.markdown("<h1 style='text-align: center;'> Boxplot </h1>", unsafe_allow_html=True)
        st.plotly_chart(fig5)

    with col2:
        st.markdown("<h1 style='text-align: center;'> Limitaciones mensuales </h1>", unsafe_allow_html=True)
        st.plotly_chart(fig4)
        st.markdown("<h1 style='text-align: center;'> Limitaciones mensuales </h1>", unsafe_allow_html=True)
        st.plotly_chart(fig6)
        st.markdown("<h1 style='text-align: center;'> Limitaciones acumuladas </h1>", unsafe_allow_html=True)
        st.plotly_chart(fig2)
        


        

    