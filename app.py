import streamlit as st
from streamlit_bokeh_events import streamlit_bokeh_events
from bokeh.models import CustomJS, Button
from PIL import Image
import paho.mqtt.client as paho
import json

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

# Cargar y mostrar la imagen
image = Image.open('voice_icon.png')
st.image(image, width=100, use_column_width=False)

# Botón para activar el reconocimiento de voz
if st.button("Hablar"):
    st.write("Esperando comando de voz...")
    result = streamlit_bokeh_events(
        Button(label="Hablar", width=100),
        events="GET_TEXT",
        key="listen",
        refresh_on_update=False,
        override_height=75,
        debounce_time=0,
        js_code="""
        var recognition = new webkitSpeechRecognition();
        recognition.continuous = true;
        recognition.interimResults = true;
        recognition.onresult = function (event) {
            var last = event.results.length - 1;
            var command = event.results[last][0].transcript.trim();
            document.dispatchEvent(new CustomEvent("GET_TEXT", {detail: command}));
        };
        recognition.start();
        """
    )

    # Procesar el comando de voz
    if result and "GET_TEXT" in result:
        command = result["GET_TEXT"]
        st.write(f"Comando recibido: {command}")
        if "prender luz" in command.lower():
            client.publish("home/luz", json.dumps({"command": "encender"}))
        elif "abrir puerta" in command.lower():
            client.publish("home/acceso", json.dumps({"command": "abrir"}))
