import streamlit as st
from PIL import Image
import paho.mqtt.client as paho
import json

# Configuración del cliente MQTT
broker = "broker.hivemq.com"
port = 1883
client = paho.Client("controlador")
def on_publish(client, userdata, result):
    print("data published \n")
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
        height: 100px;  /* Ajustar al tamaño de tu imagen */
        width: 100px;
    }
</style>
""", unsafe_allow_html=True)

# Título y subtítulo
st.title("Smarthive Home")
st.subheader("Control por Voz")

# Mostrar imagen de micrófono y usar como botón
image_path = 'voice_icon.png'
image = Image.open(image_path)

# Colocar un botón transparente sobre la imagen
if st.button("", key="mic"):
    st.write("Esperando comando de voz...")
    # Aquí integrarás la lógica real de reconocimiento de voz
    # Simulación de respuesta
    command = "prender luz"  # Simular recibir un comando de voz
    st.write(f"Comando recibido: {command}")
    client.publish("home/luz", json.dumps({"command": "encender"}))

# Código adicional para otros botones si es necesario
