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
    .reportview-container .main .block-container{
        padding-top: 5rem;
        padding-bottom: 5rem;
    }
    body {
        background-color: #004D40;
    }
    .stButton>button {
        color: white;
        border: none;
        border-radius: 50%;
        height: 100px;
        width: 100px;
        font-size: 16px;
        font-weight: bold;
        background-color: #FFA500;  /* Cambiar si es necesario para coincidir con el icono del micrófono */
        background-image: url('data:image/png;base64,<BASE64_IMAGE>'); /* Agrega aquí la imagen del micrófono en formato base64 */
        background-size: cover;
        background-position: center;
    }
</style>
""", unsafe_allow_html=True)

# Título y subtítulo
st.title("Smarthive Home")
st.subheader("Control por Voz")

# Mostrar imagen de micrófono como icono decorativo
image_path = 'voice_icon.png'
image = Image.open(image_path)
st.image(image, width=100, use_column_width=False)

# Botón de hablar personalizado como micrófono
if st.button("", key="mic"):
    st.write("Esperando comando de voz...")
    # Lógica de reconocimiento de voz aquí

# Columnas para otros botones
col1, col2 = st.columns(2)
with col1:
    if st.button("Luz"):
        client.publish("home/luz", json.dumps({"command": "toggle_luz"}))
with col2:
    if st.button("Acceso"):
        client.publish("home/acceso", json.dumps({"command": "toggle_acceso"}))
