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
    .stImage>img {
        cursor: pointer;  /* Cambia el cursor para indicar que es clickeable */
    }
</style>
""", unsafe_allow_html=True)

# Título y subtítulo
st.title("Smarthive Home")
st.subheader("Control por Voz")

# Mostrar imagen de micrófono y usar como botón
image_path = 'voice_icon.png'
image = Image.open(image_path)

def execute_voice_command():
    st.write("Esperando comando de voz...")
    # Simula la recepción de un comando (integrar lógica de reconocimiento de voz real aquí)
    command = "prender luz"  # Simula recibir un comando de voz
    st.write(f"Comando recibido: {command}")
    client.publish("home/luz", json.dumps({"command": "encender"}))

if st.image(image, use_column_width=True, output_format="PNG", on_click=execute_voice_command):
    pass  # El botón es completamente invisible y se activa el JS para el reconocimiento de voz
