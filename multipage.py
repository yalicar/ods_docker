# ---- Import libraries ----
import streamlit as st
import datetime

# ---- Define the multipage class to manage the multiple apps in our program ----
class MultiPage: 

    # ---- Contrucctor de la clase ----
    def __init__(self,df) -> None:
        self.pages = []
        self.df = df
    
    # ---- Metodo para agregar paginas al proyecto ----
    def add_page(self, title, func) -> None: 
        self.pages.append(
            {
                "title": title, 
                "function": func
            }
        )
    # ---- Funcion principal run
    def run(self):
        # ---- Drodown to select the page to run ----
        page = st.sidebar.selectbox(
            'App Navigation', 
            self.pages, 
            format_func=lambda page: page['title']
        )
        # ---- run the app function ----
        page['function'](self.df)
    
    # ---- Decorador ----
    @classmethod
    def filter(cls,df):
        # ---- Filtro por pais ----
        all_plants = st.sidebar.checkbox(
            "All Plants",
            value=True,
            key="all_plants",
        )
        planta = st.sidebar.multiselect(
            'Filtro por planta',
            df["Planta"].unique()
        )
        # ---- Filtro por fecha ----
        start_date = st.sidebar.date_input(
            "Start date",
            min_value= min(df["Fecha"]),
            value= datetime.date(2020,1,1),
        )
        end_date = st.sidebar.date_input(
            "End date",
            min_value= min(df["Fecha"])
        )
        
        if all_plants:
            df_filtered = df
        else:
            df_filtered = df[df["Planta"].isin(planta)
            ]
        df_filtered = df_filtered[(df_filtered["Fecha"].dt.date >= start_date) &
                                (df_filtered["Fecha"].dt.date <= end_date)]
        return cls(df_filtered)


    