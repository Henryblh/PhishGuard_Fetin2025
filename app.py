from flask import Flask, request, jsonify

app = Flask(__name__)

# Token que você definiu na criação do webhook no Meta
VERIFY_TOKEN = "Fetinday2025"

# Endpoint para verificação do webhook (usado apenas uma vez)
@app.route("/webhook", methods=["GET"])
def verify():
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("WEBHOOK VERIFICADO COM SUCESSO")
        return challenge, 200
    else:
        return "Falha na verificação", 403

# Endpoint que recebe mensagens do WhatsApp
@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    print("🔔 Mensagem recebida:", data)

    # Verifica se é uma mensagem de texto
    try:
        messages = data["entry"][0]["changes"][0]["value"]["messages"]
        if messages:
            message = messages[0]
            phone_number = message["from"]
            text = message["text"]["body"]
            print(f"📨 De {phone_number}: {text}")

            # Aqui você pode acionar sua API de detecção ou responder direto
            # Exemplo: responder automaticamente
            from send_message import send_message
            send_message(phone_number, f"Você disse: {text}")

    except KeyError:
        print("🟡 Evento sem mensagem de texto.")

    return jsonify(success=True), 200

if __name__ == "__main__":
    app.run(debug=True)
