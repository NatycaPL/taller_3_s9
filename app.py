import streamlit as st 
import plotly.express as px


st.title("Proyecto Natasha")

st.header("Objetivo del Informe")

st.write("El objetivo de este informe es mostrar algunos de mis trabajos.")
st.write("Este análisis permitirá formular recomendaciones orientadas a optimizar la estrategia de ventas y la gestión de inventario en función de los datos obtenido")

df = px.data.tips()

# st.dataframe(df) 

datos = df.rename(columns={
    'total_bill' : 'cuenta_total',
    'tip' : 'propina',
    'sex' : 'genero',
    'smoker' : 'fumador', 
    'day' : 'dia',
    'time' : 'hora',
     'size' : 'tamano_mesa'
    
})

# st.dataframe(datos)

st.sidebar.header('Título sidebar')

rango_cuenta = st.sidebar.slider(
    'Rango de cuenta',
    min_value=float(datos['cuenta_total'].min()),
    max_value=float(datos['cuenta_total'].max()),
    value=(float(datos['cuenta_total'].min()), float(datos['cuenta_total'].max()))
)

personas = st.sidebar.slider(
    '# Personas en la mesa',
    min_value=int(datos['tamano_mesa'].min()),
    max_value=int(datos['tamano_mesa'].max()),
    value=(int(datos['tamano_mesa'].min()), int(datos['tamano_mesa'].max()))
)

hora_seleccionada = st.sidebar.radio(
    'Hora del día', 
    options=['Todos', 'Lunch', 'Dinner']
)

mask = (
    (datos['cuenta_total'] >= rango_cuenta[0]) &
    (datos['cuenta_total'] <= rango_cuenta[1]) &
    (datos['tamano_mesa'] >= personas[0]) &
    (datos['tamano_mesa'] <= personas[1])
)

if hora_seleccionada != 'Todos':
    mask = mask & (datos['hora'] == hora_seleccionada)\
        
datos_filtrados = datos[mask]

st.divider()

st.subheader('Métricas de interés')

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
    label = 'Total de registros',
    value = len(datos_filtrados),
    delta = f"{len(datos_filtrados) - len(datos)} vs total"   
    )

with col2: 
    st.metric(
        label= 'Promedio de propinas',
        value=f"${datos_filtrados['propina'].mean():.2f}"
    )
    
with col3: 
    st.metric(
        label= 'Promedio de cuentas',
        value=f"${datos_filtrados['cuenta_total'].mean():.2f}"
    )

st.subheader('Datos filtrados')

st.dataframe(datos_filtrados)

st.subheader('Relación Cuenta/Propina')

fig = px.scatter(
    datos_filtrados,
    x='cuenta_total',
    y='propina', 
    color = 'hora',
    size = 'tamano_mesa',
    hover_data=['dia', 'fumador']
)

st.plotly_chart(fig)

cb_globos = st.checkbox("cb1")
st.write(cb_globos)

if cb_globos:
    st.snow


st.divider()

iris = px.data.iris()

col4, col5 =  st.columns([1,3])

with col4:
     st.write("Seleccione las especies a filtrar:")
     cb1 = st.checkbox("a. Setosa")
     cb2 = st.checkbox("b. Versicolor")
     cb3 = st.checkbox("c. Virginica")

with col5:
    especies = []

    if cb1:
        especies.append("setosa")

    if cb2:
        especies.append("versiculor")    

    if cb3:
        especies.append("virginica")

    st.write(especies)

