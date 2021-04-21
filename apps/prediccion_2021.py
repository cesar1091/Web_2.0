import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def app():
    st.write('---')
    st.write("""
    # Ventas Protisa por distribuidora año 2021
    """)

    expander_bar = st.beta_expander('About')
    expander_bar.markdown("""
    * **Python libraries:** streamlit, pandas, numpy, PIL, sklearn
    * **Data source:** Base de datos de Protisa
    """)
    dataset = pd.read_csv('C:/Users/DELL/github/Web_2.0/apps/data_2021.csv', index_col=0)
    dist_names = dataset.CodigoDistribuidor.unique()
    # page layout
    # divide page to 3 columns
    col1 = st.sidebar
    col2, col3 = st.beta_columns((1,1))
    # Sidebar
    col1.header("Seleccione los distribuidores:")

    dist_select = col1.multiselect('Seleccione la distribuidora', dist_names)

    df_selected = dataset[dataset['CodigoDistribuidor'].isin(dist_select)]

    col2.subheader('Line Plot - ventas acumuladas - prediccion')
    for i in dist_select:
        col2.subheader(i)
        chart_data_1 = pd.DataFrame(df_selected[df_selected['CodigoDistribuidor']==i][['Ventas_acumuladas','prediccion']],columns=['Ventas_acumuladas','prediccion'])
        chart_data_1.index = pd.to_datetime(df_selected[df_selected['CodigoDistribuidor']==i]['CodigoFecha'])
        col2.line_chart(chart_data_1)

    col3.subheader('Prediccion - DataFrame')
    for i in dist_select:
        col3.subheader(i)
        chart_data_2 = pd.DataFrame(df_selected[df_selected['CodigoDistribuidor']==i][['Ventas_acumuladas','prediccion']],columns=['Ventas_acumuladas','prediccion'])
        chart_data_2.index = pd.to_datetime(df_selected[df_selected['CodigoDistribuidor']==i]['CodigoFecha'])
        col3.dataframe(chart_data_1)
