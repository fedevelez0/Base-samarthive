import streamlit as st
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
        color: white;
        border: 2px solid white;
        border-radius: 30px;
        height: 50px;
        width: 150px;
        font-size: 16px;
        font-weight: bold;
        text-transform: uppercase;
        background-color: transparent;
        display: block;
        margin: 10px auto;
    }
</style>
""", unsafe_allow_html=True)

# Título y subtítulo
st.title("Smarthive Home")
st.subheader("Control por Voz")

# Botones para acciones
col1, col2, col3 = st.columns([1, 1, 1])  # Ajuste para centrar los botones
with col1:
    if st.button("Luz"):
        client.publish("home/luz", json.dumps({"command": "toggle_luz"}))
with col2:
    if st.button("Acceso"):
        client.publish("home/acceso", json.dumps({"command": "toggle_acceso"}))

# Botón de "Hablar" con reconocimiento de voz usando JavaScript
st.markdown("""
    <button onclick="startRecognition()" style="
        color: white;
        border: 2px solid white;
        border-radius: 30px;
        height: 50px;
        width: 150px;
        font-size: 16px;
        font-weight: bold;
        text-transform: uppercase;
        background-color: transparent;
        display: block;
        margin: 10px auto;
    ">Hablar</button>

    <script type="text/javascript">
        function startRecognition() {
            var recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
            recognition.lang = 'es-ES';
            recognition.continuous = false;
            recognition.interimResults = false;

            recognition.onresult = function(event) {
                var command = event.results[0][0].transcript;
                console.log("Comando recibido:", command);
                var streamlitEvent = new CustomEvent("streamlit-event", {detail: {command: command}});
                document.dispatchEvent(streamlitEvent);
            };
            recognition.start();
        }
    </script>
""", unsafe_allow_html=True)

# Captura del comando de voz recibido
st.write("Comando recibido:")
command = st.experimental_get_query_params().get("command", [""])[0]
if command:
    st.write(f"Comando: {command}")
    if "prender luz" in command.lower():
        client.publish("home/luz", json.dumps({"command": "encender"}))
    elif "abrir puerta" in command.lower():
        client.publish("home/acceso", json.dumps({"command": "abrir"}))
