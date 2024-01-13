from flask import Flask, render_template, jsonify, request
from heyoo import WhatsApp
from openai import OpenAI
from dotenv import load_dotenv
import os


# Ruta del directorio actual
dir_actual = os.getcwd()

# Ruta del archivo que se quiere abrir (relativa al directorio actual)
ruta_txt = os.path.join(dir_actual, 'data.txt')

# Cargamos las variables de entorno
load_dotenv()

port = int(os.getenv("PORT")) or 5000
api_key = os.getenv("API_KEY")
token_meta = os.getenv("TOKEN_META")
id_phone = os.getenv("ID_PHONE")
organization = os.getenv("ORGANIZATION")

with open(ruta_txt, "r", encoding="utf-8") as f:
    extra_body = f.read()

# Conexcion a la API de OpenAI
client = OpenAI(api_key=api_key, organization=organization)


def get_response(message):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"Eres un vendedor de viene raices muy amables, no des respuestas tan largas y la siguiente es informacion del inmueble que vas a vender: {extra_body}"},
            {
                "role": "user",
                "content": message
            }
        ],
        temperature=0.2,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response.choices[0].message.content


def send_message(phone_receive, answer, meta_acceso, phone_id):
    # Token de acceso de Meta
    # global token_meta
    # # Identificador de número de teléfono
    # global id_phone

    # Init WhatsApp
    menssage_Whats = WhatsApp(meta_acceso, phone_id)
    phone_receive = phone_receive.replace("521", "52")

    # Enviamos el mensaje
    menssage_Whats.send_message(answer, phone_receive)


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/webhook/", methods=["POST", "GET"])
def webhook_whatsapp():
    # Token de acceso de Meta
    global token_meta

    # Identificador de número de teléfono
    global id_phone

    if request.method == "GET":

        # Verificacion de token
        if request.args.get('hub.verify_token') == "stdyws":
            return request.args.get('hub.challenge')
        else:
            return "Error de autentificacion."

    # Recibimos los datos de la API de Facebook
    data = request.get_json()

    # Telefono del cliente
    phone_number = data['entry'][0]['changes'][0]['value']['messages'][0]['from']

    # Mensaje del cliente
    message = data['entry'][0]['changes'][0]['value']['messages'][0]['text']['body']

    # id del mensaje
    # idWA = data['entry'][0]['changes'][0]['value']['messages'][0]['id']

    # Imformacion de la fecha y hora del mensaje
    # timestamp = data['entry'][0]['changes'][0]['value']['messages'][0]['timestamp']

    if message is not None:

        open_renponse = get_response(message)
        send_message(phone_number, open_renponse, token_meta, id_phone)

        # Retornamos el status de la respuesta
        return jsonify({"status": "success"}, 200)


if __name__ == "__main__":
    app.run(port=port, debug=False)
