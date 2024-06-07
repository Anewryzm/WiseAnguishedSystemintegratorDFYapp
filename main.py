import streamlit as st

# Encabezado de la aplicación
st.header('Desplegando una aplicación')

# Campo para recibir una consulta
consulta = st.text_area('Ingrese su consulta')

# Input de selección múltiple para escoger el lenguaje
lenguaje = st.selectbox('Seleccione el lenguaje', ('Español', 'Inglés'))

# Guardar los valores en variables
if st.button('Guardar'):
    st.write('Consulta:', consulta)
    st.write('Lenguaje seleccionado:', lenguaje)
