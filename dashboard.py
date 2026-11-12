import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(page_title='Promise Intelligence Chile', layout='wide')
st.title('Promise Intelligence Chile')
st.caption('Monitoreo de promesas comerciales | IKEA vs Falabella')
st.info('Piloto en preparación. No hay fechas reales verificadas todavía.')
regions = ['Región Metropolitana', 'Valparaíso', 'Biobío', 'Antofagasta']
a, b = st.columns(2)
with a:
    st.multiselect('Regiones', regions, default=regions)
with b:
    st.multiselect('Modalidad', ['HD', 'C&C'], default=['HD', 'C&C'])
st.subheader('Capturas históricas')
file = Path('observaciones.csv')
if file.exists():
    df = pd.read_csv(file)
    st.dataframe(df, use_container_width=True)
else:
    st.write('Sin capturas registradas. El bot aún no está conectado.')
st.caption('Las fechas se publicarán solo después de verificar la promesa visible al cliente.')
