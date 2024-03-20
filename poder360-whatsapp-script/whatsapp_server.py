import requests
import base64

class WhatsappServer():
    def __init__(self, host, session_name, api_key):
        self.host = host
        self.session_name = session_name
        self.api_key = api_key
        self.headers = {
            'x-api-key': self.api_key,
            'accept': '*/*',
            'Content-Type': 'text/html,application/json,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'
        }

    def get_status(self):
        response = {}
        url = self.host+f"/session/status/{self.session_name}"
        try:
            data = requests.get(url,headers=self.headers).json()
        except Exception as e:
            print(e)
            return {"Erro": str(e)}
        return f'Status: Servidor está conectado - {data}'
    
    def start_session(self):
        response = {}
        url = self.host+f'/session/status/{self.session_name}'

        try:
            data = requests.get(url, headers=self.headers).json()
            response = 'Conexão estabelecida!'
        except Exception as e:
            print(e)
            response = {'Erro: ', str(e)}
        return response
    
    def terminate_session(self):
        response = {}
        url = self.host+f"/session/terminate/{self.session_name}"
        try:
            data = requests.get(url,headers=self.headers).json()
            response = data
        except Exception as e:
            print(e)
            response = {"Erro": str(e)}
        return response

    def get_qr_code(self):
        response = {}
        url = self.host+f"/session/qr/{self.session_name}/image"
        try:
            data = requests.get(url,headers=self.headers)
            response = str(base64.b64encode(data.content).decode("utf-8"))

        except Exception as e:
            print(e)
            response = None
        return response

    def send_message(self, chat_id: str, message: str):
        url = self.host+f"/client/sendMessage/{self.session_name}"
        headers = {
            'x-api-key': self.api_key,
            'accept': '/',
            'Content-Type': 'application/json'
        }
        data = {
            'chatId': chat_id,
            'contentType': 'string',
            'content': message
        }
        sent = True

        try:
            requests.post(url=url, json=data, headers= headers)

        except Exception as e:
            print(f"Erro ao enviar {message} chat ID {chat_id}: {e}")
            sent = False
        
        if sent:
            return f'Mensagem enviada com sucesso para {chat_id}'
            
        return sent