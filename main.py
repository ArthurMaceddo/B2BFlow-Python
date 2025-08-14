import os
from supabase import create_client, Client
from dotenv import load_dotenv
import requests

load_dotenv()

SUPABASE_URL=os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
ZAPI_TOKEN=os.getenv("ZAPI_TOKEN")
ZAPI_API_TOKEN=os.getenv("ZAPI_API_TOKEN")
ZAPI_INSTANCE = os.getenv("ZAPI_INSTANCE")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY) # type: ignore

if not SUPABASE_URL or not SUPABASE_KEY or not ZAPI_TOKEN or not ZAPI_API_TOKEN:
      print("ERROR: Verifique as variaveis de ambiente")
      exit()

def send_message(name, phone_number):
    phone_number = str(phone_number).replace("+", "").replace(" ", "").replace("-", "")
    message = f"Ola {name}, tudo bem com voce?"
    url = f"https://api.z-api.io/instances/{ZAPI_TOKEN}/token/{ZAPI_API_TOKEN}/send-text"
    headers = {
        "Authorization": f"Bearer {ZAPI_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "phone_numer" : phone_number,
        "message" : message
    }

    try:
          print(f"Enviando mensagem para{name} ({phone_number})...")
          response = requests.post(url, json=payload, headers=headers)
          response.raise_for_status()
          print(f"Mensagem enviada com sucesso para {name}")
    except requests.exceptions.RequestException as e:
          print(f"Erro ao enviar mensagem para {name}: {e}")
          print(f"Detalhe da resposta: {response.text if 'response' in locals() else 'N/A'}") # type: ignore
    response = requests.post(url,json=payload, headers = headers)
    return response.json()

def main():
        contacts = supabase.table("contacts").select("name, phone_number").execute()
        for contact in contacts.data[:3]:
            name = contact['name']
            phone_number = contact['phone_number']
            result = send_message(name, phone_number)
            print(f"A mensagem foi enviada para {name}: {result}")

if __name__ == "__main__":
       main()