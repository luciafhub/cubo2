import streamlit as st
import pandas as pd
import altair as alt

# Suprimir ngrok, por usar la Cloud

# Cargar los archivos CSV con los datos ficticios
@st.cache_data
def cargar_datos(nombre_archivo):
    return pd.read_csv(nombre_archivo)

# Cargar cada tabla
enfermeras = cargar_datos("bbdd/enfermeras_1k.csv")
pacientes = cargar_datos("bbdd/pacientes_1k.csv")
alertas = cargar_datos("bbdd/alertas_1k.csv")
centros = cargar_datos("bbdd/centros_100.csv")
intervenciones = cargar_datos("bbdd/intervenciones_1k.csv")
medidas = cargar_datos("bbdd/medidas_1k.csv")
pacientes_enfermeras = cargar_datos("bbdd/pacientes_enfermeras_1k.csv")
registro_login = cargar_datos("bbdd/registro_login_1k.csv")
sensores = cargar_datos("bbdd/sensores_500.csv")
sesiones = cargar_datos("bbdd/sesiones_1k.csv")
tipo_sensor = cargar_datos("bbdd/tipo_sensor.csv")

# Título de la aplicación
st.title("Análisis de Datos de Salud - Cubolab")

# Menú de selección de tabla
tabla_seleccionada = st.selectbox("Selecciona la tabla para analizar:", 
                                  ["Enfermeras", "Pacientes", "Alertas", "Centros", "Intervenciones", 
                                   "Medidas", "Pacientes_Enfermeras", "RegistroLogin", "Sensores", "Sesiones", "TipoSensor"])

# Mostrar y analizar cada tabla en función de la selección
if tabla_seleccionada == "Enfermeras":
    st.write("### Tabla: Enfermeras")
    st.dataframe(enfermeras.head())

    analisis = st.selectbox("Selecciona el análisis para Enfermeras:", 
                            ["Distribución por Sexo", "Distribución por Rol", "Edad por Rol"])

    if analisis == "Distribución por Sexo":
        st.write("Distribución de Enfermeras por Sexo")
        st.bar_chart(enfermeras["sexo"].value_counts())

    elif analisis == "Distribución por Rol":
        st.write("Distribución de Enfermeras por Rol")
        st.bar_chart(enfermeras["rol"].value_counts())

    elif analisis == "Edad por Rol":
        st.write("Distribución de Edad por Rol")
        chart = alt.Chart(enfermeras).mark_boxplot().encode(
            x='rol:N',
            y='edad:Q',
            color='rol:N'
        )
        st.altair_chart(chart, use_container_width=True)

elif tabla_seleccionada == "Pacientes":
    st.write("### Tabla: Pacientes")
    st.dataframe(pacientes.head())

    analisis = st.selectbox("Selecciona el análisis para Pacientes:", 
                            ["Distribución por Centro", "Pacientes con Cubo"])

    if analisis == "Distribución por Centro":
        st.write("Cantidad de Pacientes por Centro")
        st.bar_chart(pacientes["id_centro"].value_counts())

    elif analisis == "Pacientes con Cubo":
        st.write("Distribución de Pacientes con o sin Cubo")
        st.bar_chart(pacientes["tieneCubo"].value_counts())

elif tabla_seleccionada == "Alertas":
    st.write("### Tabla: Alertas")
    st.dataframe(alertas.head())

    analisis = st.selectbox("Selecciona el análisis para Alertas:", 
                            ["Alertas por Sensor", "Alertas por Paciente"])

    if analisis == "Alertas por Sensor":
        st.write("Distribución de Alertas por Sensor")
        st.bar_chart(alertas["sensor"].value_counts())

    elif analisis == "Alertas por Paciente":
        st.write("Cantidad de Alertas por Paciente")
        st.bar_chart(alertas["id_usuario"].value_counts())

elif tabla_seleccionada == "Centros":
    st.write("### Tabla: Centros")
    st.dataframe(centros.head())

    analisis = st.selectbox("Selecciona el análisis para Centros:", 
                            ["Centros Activos/Inactivos", "Fechas de Registro"])

    if analisis == "Centros Activos/Inactivos":
        st.write("Distribución de Centros Activos e Inactivos")
        st.bar_chart(centros["visible"].value_counts())

    elif analisis == "Fechas de Registro":
        st.write("Histograma de Fechas de Registro de los Centros")
        chart = alt.Chart(centros).mark_bar().encode(
            x=alt.X("year(fecha):T", title="Año"),
            y='count()'
        )
        st.altair_chart(chart, use_container_width=True)

elif tabla_seleccionada == "Intervenciones":
    st.write("### Tabla: Intervenciones")
    st.dataframe(intervenciones.head())

    analisis = st.selectbox("Selecciona el análisis para Intervenciones:", 
                            ["Intervenciones por Rol", "Intervenciones por Centro"])

    if analisis == "Intervenciones por Rol":
        st.write("Distribución de Intervenciones por Rol de la Enfermera")
        st.bar_chart(intervenciones["rol"].value_counts())

    elif analisis == "Intervenciones por Centro":
        st.write("Distribución de Intervenciones por Centro")
        st.bar_chart(intervenciones["id_centro"].value_counts())

elif tabla_seleccionada == "Medidas":
    st.write("### Tabla: Medidas")
    st.dataframe(medidas.head())

    analisis = st.selectbox("Selecciona el análisis para Medidas:", 
                            ["Estado Emocional de Pacientes", "Niveles de Batería"])

    if analisis == "Estado Emocional de Pacientes":
        st.write("Distribución del Estado Emocional de los Pacientes")
        st.bar_chart(medidas["emocion"].value_counts())

    elif analisis == "Niveles de Batería":
        st.write("Distribución de los Niveles de Batería de los Sensores")
        chart = alt.Chart(medidas).mark_bar().encode(
            x=alt.X("bateria:Q", bin=True),
            y='count()'
        )
        st.altair_chart(chart, use_container_width=True)

elif tabla_seleccionada == "Pacientes_Enfermeras":
    st.write("### Tabla: Pacientes_Enfermeras")
    st.dataframe(pacientes_enfermeras.head())

    analisis = st.selectbox("Selecciona el análisis para Pacientes_Enfermeras:", 
                            ["Cantidad de Pacientes por Enfermera", "Enfermeras Asignadas a Pacientes"])

    if analisis == "Cantidad de Pacientes por Enfermera":
        st.write("Distribución de Pacientes por Enfermera")
        st.bar_chart(pacientes_enfermeras["id_enfermera"].value_counts())

    elif analisis == "Enfermeras Asignadas a Pacientes":
        st.write("Distribución de Enfermeras asignadas por Paciente")
        st.bar_chart(pacientes_enfermeras["id_paciente"].value_counts())

elif tabla_seleccionada == "RegistroLogin":
    st.write("### Tabla: RegistroLogin")
    st.dataframe(registro_login.head())
    
    analisis = st.selectbox("Selecciona el análisis para RegistroLogin:", 
                            ["Frecuencia de Logins por Enfermera", "Distribución de IPs"])

    if analisis == "Frecuencia de Logins por Enfermera":
        st.write("Cantidad de Logins por Enfermera")
        st.bar_chart(registro_login["id_enfermera"].value_counts())

    elif analisis == "Distribución de IPs":
        st.write("Distribución de IPs utilizadas")
        st.bar_chart(registro_login["ip_address"].value_counts())

elif tabla_seleccionada == "Sensores":
    st.write("### Tabla: Sensores")
    st.dataframe(sensores.head())

    analisis = st.selectbox("Selecciona el análisis para Sensores:", 
                            ["Sensores Activos/Inactivos", "Distribución por Tipo de Sensor", "Niveles de Batería"])

    if analisis == "Sensores Activos/Inactivos":
        st.write("Cantidad de Sensores Activos e Inactivos")
        st.bar_chart(sensores["activo"].value_counts())

    elif analisis == "Distribución por Tipo de Sensor":
        st.write("Distribución por Tipo de Sensor")
        st.bar_chart(sensores["tipo"].value_counts())

    elif analisis == "Niveles de Batería":
        st.write("Distribución de los Niveles de Batería")
        chart = alt.Chart(sensores).mark_bar().encode(
            x=alt.X("bateria:Q", bin=True),
            y='count()'
        )
        st.altair_chart(chart, use_container_width=True)

    elif tabla_seleccionada == "Sesiones":
        st.write("### Tabla: Sesiones")
        st.dataframe(sesiones.head())

        analisis = st.select

    elif tabla_seleccionada == "Sesiones":
        st.write("### Tabla: Sesiones")
        st.dataframe(sesiones.head())

        analisis = st.selectbox("Selecciona el análisis para Sesiones:", 
                                ["Frecuencia de Sesiones por Enfermera"])

        if analisis == "Frecuencia de Sesiones por Enfermera":
            st.write("Cantidad de Sesiones por Enfermera")
            st.bar_chart(sesiones["id_enfermera"].value_counts())

    elif tabla_seleccionada == "TipoSensor":
        st.write("### Tabla: TipoSensor")
        st.dataframe(tipo_sensor.head())

        analisis = st.selectbox("Selecciona el análisis para TipoSensor:", 
                                ["Distribución de Tipos de Sensores"])

        if analisis == "Distribución de Tipos de Sensores":
            st.write("Distribución de Tipos de Sensores")
            st.bar_chart(tipo_sensor["nombre"].value_counts())


# streamlit run appentera.py