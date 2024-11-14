import streamlit as st
from streamlit_bokeh_events import streamlit_bokeh_events
from bokeh.models import CustomJS
from PIL import Image
import paho.mqtt.client as paho
import json
import os

# Establecer cliente MQTT
broker = "broker.hivemq.com"
port = 1883
client = paho.Client("Controlador")
def on_publish(client, userdata, result):
    print("Data published \n")
    pass

# Configurar conexión
client.on_publish = on_publish
client.connect(broker, port)

# Personalizar la interfaz con CSS
st.markdown("""
<style>
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .reportview-container .main .block-container{
        padding-top: 5rem;
        padding-bottom: 5rem;
    }
    body {
        background-color: #004D40;
    }
</style>
""", unsafe_allow_html=True)

# Título y subtítulo
st.title("Smarthive Home")
st.subheader("Control por Voz")

# Cargar imagen y usar como botón
image = Image.open('voice_icon.png')

# Mostrar imagen como botón
clicked = st.image(image, use_column_width=False, on_click=None, caption='Hablar')

# Inicializar el reconocimiento de voz
stt_button = st.empty()  # Crear un espacio vacío para el botón
stt_button.image(image, width=100, on_click=lambda: streamlit_bokeh_events(
    CustomJS(code="""
    var recognition = new webkitSpeechRecognition();
    recognition.continuous = true;
    recognition.interimResults = true;
    recognition.onresult = function (event) {
        var last = event.results.length - 1;
        var command = event.results[last][0].transcript.trim();
        document.dispatchEvent(new CustomEvent("GET_TEXT", {detail: command}));
    };
    recognition.start();
    """),
    events="GET_TEXT",
    key="listen",
    refresh_on_update=False,
    override_height=75,
    debounce_time=0))

# Procesar comandos de voz
if clicked:
    result = st.session_state['listen']
    if result:
        if "GET_TEXT" in result:
            command = result.get("GET_TEXT")
            st.write(f"Comando recibido: {command}")
            if "prender luz" in command.lower():
                client.publish("home/luz", json.dumps({"command": "encender"}))
            elif "abrir puerta" in command.lower():
                client.publish("home/acceso", json.dumps({"command": "abrir"}))

