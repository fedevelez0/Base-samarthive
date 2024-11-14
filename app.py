import streamlit as st
from PIL import Image
from streamlit_bokeh_events import streamlit_bokeh_events
from bokeh.models import CustomJS, Button
import paho.mqtt.client as paho
import json

# Establecer cliente MQTT
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
        background-color: transparent;
        border: none;
        color: transparent;
        height: 100px;
        width: 100px;
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
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

# Mostrar imagen de micrófono
image = Image.open('voice_icon.png')
st.image(image, width=100, use_column_width=True)

# Botón invisible para el reconocimiento de voz
stt_button = Button(label="Hablar", width=100)
stt_button.js_on_event("button_click", CustomJS(code="""
    var recognition = new webkitSpeechRecognition();
    recognition.continuous = true;
    recognition.interimResults = true;
    recognition.onresult = function (event) {
        var last = event.results.length - 1;
        var command = event.results[last][0].transcript.trim();
        document.dispatchEvent(new CustomEvent("GET_TEXT", {detail: command}));
    };
    recognition.start();
"""))

# Manejar eventos de voz
result = streamlit_bokeh_events(
    stt_button,
    events="GET_TEXT",
    key="listen",
    refresh_on_update=False,
    override_height=75,
    debounce_time=0)

# Procesar comandos de voz
if result:
    if "GET_TEXT" in result:
        command = result.get("GET_TEXT")
        st.write(f"Comando recibido: {command}")
        if "prender luz" in command.lower():
            client.publish("home/luz", json.dumps({"command": "encender"}))
        elif "abrir puerta" in command.lower():
            client.publish("home/acceso", json.dumps({"command": "abrir"}))
