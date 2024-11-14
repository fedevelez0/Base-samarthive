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
        padding: 5rem 1rem;
    }
    body {
        background-color: #004D40;
    }
    .stButton>button {
        display: block;
        margin: 1rem auto;
        background-color: transparent;
        border: none;
        color: transparent;
        height: 100px;
        width: 100px;
        position: relative;
        top: -120px;
    }
</style>
""", unsafe_allow_html=True)

# Título y subtítulo
st.title("Smarthive Home")
st.subheader("Control por Voz")

# Mostrar imagen de micrófono y usar como botón
image = Image.open('voice_icon.png')
st.image(image, width=100, use_column_width=True)

# Botón transparente
if st.button("", key="speak"):
    st.write("Esperando comando de voz...")
    # Aquí deberías integrar la lógica de reconocimiento de voz real
    # Simulación de respuesta
    command = "prender luz"  # Simulación de un comando de voz recibido
    st.write(f"Comando recibido: {command}")
    client.publish("home/luz", json.dumps({"command": "encender"}))
