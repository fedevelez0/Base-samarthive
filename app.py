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

# Personalizar la interfaz con CSS para hacer el botón completamente transparente y bien ubicado
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
        height: 200px;  /* Ajustar según el tamaño de tu imagen */
        width: 200px;
        position: absolute;
        top: 50%;  /* Ajustar si es necesario para centrar */
        left: 50%;
        transform: translate(-50%, -50%);
    }
</style>
""", unsafe_allow_html=True)

# Título y subtítulo
st.title("Smarthive Home")
st.subheader("Control por Voz")

# Cargar y mostrar la imagen como botón
image = Image.open('voice_icon.png')
st.image(image, use_column_width=False)
if st.button("", key="speak"):
    st.write("Esperando comando de voz...")
    # Simular la recepción de un comando (integrar lógica de reconocimiento de voz real aquí)
    command = "prender luz"
    st.write(f"Comando recibido: {command}")
    client.publish("home/luz", json.dumps({"command": "encender"}))
