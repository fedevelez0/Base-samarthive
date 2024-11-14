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
        border: none;
        color: transparent;
        background-color: transparent;
        height: 100%;
        width: 100%;
    }
</style>
""", unsafe_allow_html=True)

# Título y subtítulo
st.title("Smarthive Home")
st.subheader("Control por Voz")

# Cargar y mostrar la imagen como botón
image_path = 'voice_icon.png'
image = Image.open(image_path)

col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    st.write("")  # Espacio en blanco
with col2:
    st.image(image, use_column_width=True)
    if st.button("", key="speak", help="Presiona el icono para hablar"):
        st.write("Esperando comando de voz...")
        # Aquí debes integrar tu lógica de reconocimiento de voz
        st.write("Reconocimiento de voz activado")
        # Simular un comando recibido y enviarlo via MQTT
        client.publish("home/control", json.dumps({"command": "toggle_light"}))
with col3:
    st.write("")  # Espacio en blanco
