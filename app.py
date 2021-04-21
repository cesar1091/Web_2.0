import streamlit as st
from multiapp import MultiApp
from apps import ventas_dist

# import your app modules here
app = MultiApp()
st.set_page_config(layout="wide")
st.markdown("""
# Web app prediccion de ventas sell out protisa
Seleccione la escala temporal de prediccion (semanal, quincenal, mensual)
""")

# Add all your application here
app.add_app("Ventas Distribuidora", ventas_dist.app)

# The main app
app.run()
