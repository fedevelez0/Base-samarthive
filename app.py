import streamlit as st
from streamlit_bokeh_events import streamlit_bokeh_events
from bokeh.models import CustomJS, Button
import paho.mqtt.client as paho
import json

# Configuración del cliente MQTT
broker = "broker.hivemq.com"
port = 1883
client = paho.Client("Controlador")
def on_publish(client, userdata, result):
    print("Data published \n")
    pass

client.on_publish = on_publish
client.connect(broker, port)

# Personalizar la interfaz con CSS
st.markdown("""
<style>
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .reportview-container .main .block-container {
        padding-top: 5rem;
        padding-bottom: 5rem;
    }
    body {
        background-color: #004D40;
    }
    .stButton>button {
        color: white;
        border: 2px solid white;
        border-radius: 30px;
        height: 50px;
        width: 150px;
        font-size: 16px;
        font-weight: bold;
        text-transform: uppercase;
        background-color: transparent;
        display: block;
        margin: 10px auto;
    }
</style>
""", unsafe_allow_html=True)

# Título y subtítulo
st.title("Smarthive Home")
st.subheader("Control por Voz")

# Botones para acciones
col1, col2, col3 = st.columns([1,1,2])  # Ajuste para centrar los botones
with col1:
    if st.button("Luz"):
        client.publish("home/luz", json.dumps({"command": "toggle_luz"}))
with col2:
    if st.button("Acceso"):
        client.publish("home/acceso", json.dumps({"command": "toggle_acceso"}))

# Inicializar el reconocimiento de voz con el mismo estilo de botón
if st.button("Hablar"):
    st.write("Esperando comando de voz...")
    # Simulación de recepción de comando (implementar la lógica real aquí)

# Aquí iría la lógica para el reconocimiento de voz si se utiliza alguna biblioteca específica o integración con servicios externos
