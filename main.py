import json
import time
from make_server_whatsapp import WhatsappServer

api_key = "" #Aqui vai a chave de API
host = f"http://localhost:3000"
session_name = "" #Aqui vai o nome da sessão desejada

msg = '''*TESTE AUTOMATIZADO WHATSAPP WRAPPER API*'''

nums = [""] #Aqui vão os números desejados para envio da mensagem de WhatsApp
wpp = WhatsappServer(host= host, session_name= session_name, api_key=api_key)

print(wpp.start_session())
print(wpp.get_status())

for num in nums:
    print(wpp.send_message(f'{num}',msg))
    time.sleep(1)
