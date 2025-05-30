import requests
import os

ACCESS_TOKEN = os.getenv("META_TOKEN")  # Defina no seu .env ou exporte na máquina
PHONE_NUMBER_ID = os.getenv("META_PHONE_ID")

def send_message(to, message):
    url = f"https://graph.facebook.com/v19.0/{PHONE_NUMBER_ID}/messages"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "text",
        "text": {"body": message}
    }
    response = requests.post(url, headers=headers, json=payload)
    print("📤 Resposta da API:", response.json())
