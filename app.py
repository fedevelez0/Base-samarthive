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
        background-color: transparent;
        border: none;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# Título y subtítulo
st.title("Smarthive Home")
st.subheader("Control por Voz")

# Cargar y mostrar la imagen como botón
image = Image.open('voice_icon.png')
if st.button("", key="speak", help="Hablar"):
    st.write("Esperando comando de voz...")
    # Aquí debe ir la lógica de reconocimiento de voz que integre con el sistema MQTT
    # Simulación de respuesta
    st.write("Comando reconocido: 'prender luz'")
    client.publish("home/luz", json.dumps({"command": "encender"}))

# Añadir otros controles o información según sea necesario
st.write("Interactúa con la imagen para activar el control de voz.")
