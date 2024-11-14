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
    .stImage>img {
        cursor: pointer;  /* Cambia el cursor para indicar que es clickeable */
    }
</style>
""", unsafe_allow_html=True)

# Título y subtítulo
st.title("Smarthive Home")
st.subheader("Control por Voz")

# Mostrar imagen de micrófono y usar como botón
image = Image.open('voice_icon.png')
clicked = st.image(image, use_column_width=True, output_format="PNG", on_click=lambda: execute_voice_command())

def execute_voice_command():
    st.write("Esperando comando de voz...")
    # Aquí integras tu lógica de reconocimiento de voz
    # Simulación de comando recibido
    command = "prender luz"  # Simula recibir un comando de voz
    st.write(f"Comando recibido: {command}")
    client.publish("home/luz", json.dumps({"command": "encender"}))

# Otra lógica o botones adicionales si necesarios
# Ejemplo: Botones para controlar otras funciones
col1, col2 = st.columns(2)
with col1:
    if st.button("Luz"):
        client.publish("home/luz", json.dumps({"command": "toggle_luz"}))
with col2:
    if st.button("Acceso"):
        client.publish("home/acceso", json.dumps({"command": "toggle_acceso"}))
