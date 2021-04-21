import streamlit as st
from multiapp import MultiApp
from apps import ventas_dist, prediccion_2021

# import your app modules here
app = MultiApp()
st.set_page_config(layout="wide")
st.markdown("""
# Web app prediccion de ventas sell out protisa
Seleccione la escala temporal de prediccion (semanal, quincenal, mensual)
""")

# Add all your application here
app.add_app("Ventas Distribuidora año 2020", ventas_dist.app)
app.add_app("Prediccion ventas año 2021", prediccion_2021.app)

# The main app
app.run()
