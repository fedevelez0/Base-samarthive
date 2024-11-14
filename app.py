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
    .stButton>button {
        visibility: hidden;  /* Hace el botón completamente invisible */
        height: 100%;
        width: 100%;
    }
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

# Mostrar imagen de micrófono como botón
image = Image.open('voice_icon.png')
if st.button("", key="speak"):
    st.write("Esperando comando de voz...")

# Inicializar el reconocimiento de voz usando Bokeh para manejar eventos JS
from bokeh.models import CustomJS
stt_button = CustomJS(code="""
    var recognition = new webkitSpeechRecognition();
    recognition.continuous = true;
    recognition.interimResults = true;
    recognition.onresult = function (event) {
        var last = event.results.length - 1;
        var command = event.results[last][0].transcript.trim();
        document.dispatchEvent(new CustomEvent("GET_TEXT", {detail: command}));
    };
    recognition.start();
""")

# Mostrar el botón invisible y manejar eventos de voz
if st.button("Hablar", key="listen", on_click=stt_button):
    pass  # El botón es invisible y se activa el JS para el reconocimiento de voz

# Procesar comandos de voz
if "GET_TEXT" in st.session_state:
    command = st.session_state["GET_TEXT"]
    st.write(f"Comando recibido: {command}")
    if "prender luz" in command.lower():
        client.publish("home/luz", json.dumps({"command": "encender"}))
    elif "abrir puerta" in command.lower():
        client.publish("home/acceso", json.dumps({"command": "abrir"}))
