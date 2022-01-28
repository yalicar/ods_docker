# ---- Import libraries ----
from st_aggrid import AgGrid
import streamlit as st
from st_aggrid.grid_options_builder import GridOptionsBuilder
from st_aggrid.shared import GridUpdateMode


def app(df):
    shows = df
    gb = GridOptionsBuilder.from_dataframe(shows)

    #gb.configure_pagination(enabled=True)
    gb.configure_side_bar()
    gb.configure_default_column(groupable=True, value=True, enableRowGroup=True, aggFunc="sum", editable=True)
    #gb.configure_selection(selection_mode="multiple", use_checkbox=True)
    gridOptions = gb.build()

    AgGrid(
        shows,
        gridOptions=gridOptions,
        enable_enterprise_modules=True,
        height="600px",
        fit_columns_on_grid_load=True,
        theme="dark",
        quick_filter = True,
        update_mode= GridUpdateMode.SELECTION_CHANGED
    )
