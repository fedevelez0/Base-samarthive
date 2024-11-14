import streamlit as st
from PIL import Image
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
        display: block;
        margin: auto;
        background: url('voice_icon.png') no-repeat center center; /* Asegúrate de que 'voice_icon.png' es el archivo correcto y está en el directorio adecuado */
        border: none;
        color: transparent; /* Hace el texto invisible */
        height: 100px;
        width: 100px;
        cursor: pointer;
    }
</style>
""", unsafe_allow_html=True)

# Título y subtítulo
st.title("Smarthive Home")
st.subheader("Control por Voz")

# Botón que activa el reconocimiento de voz
if st.button("", key="speak"):
    st.write("Esperando comando de voz...")
    # Simula la recepción de un comando (integrar lógica de reconocimiento de voz real aquí)
    command = "prender luz"
    st.write(f"Comando recibido: {command}")
    client.publish("home/luz", json.dumps({"command": "encender"}))

# Otros botones como luz y acceso, si son necesarios
col1, col2 = st.columns(2)
with col1:
    if st.button("Luz"):
        client.publish("home/luz", json.dumps({"command": "toggle_luz"}))
with col2:
    if st.button("Acceso"):
        client.publish("home/acceso", json.dumps({"command": "toggle_acceso"}))
