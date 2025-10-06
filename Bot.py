import Vars
import time
import schedule
from Function import simpleRoll
from flask import Flask
from threading import Thread

# Configuración del servidor web
app = Flask(__name__)

@app.route('/')
def home():
    return "El bot está vivo y funcionando."

def run_web_server():
    # El servidor se ejecuta en el puerto que Render asigna
    app.run(host='0.0.0.0', port=10000)

# Lógica del bot de Mudae
def run_bot_logic():
    timeString = ':' + Vars.repeatMinute
    schedule.every().hour.at(timeString).do(simpleRoll)
    while True:
        schedule.run_pending()
        time.sleep(1)

# Iniciar ambos procesos
if __name__ == "__main__":
    # Inicia el servidor web en un hilo
    web_thread = Thread(target=run_web_server)
    web_thread.start()
    
    # Inicia la lógica del bot en el hilo principal
    run_bot_logic()