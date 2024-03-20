import json
import time
from whatsapp_server import WhatsappServer

api_key = "P360#wsd"
host = f"http://localhost:3000"
session_name = "poder360"

msg = '''*TESTE AUTOMATIZADO WHATSAPP WRAPPER API*

🌞 Oi, eis a 2ª edição do Drive/Poder360 📲 Caixa espera R$ 18 bi com bets

https://poder.cc/lmoTy2
Caso o link não esteja clicável, mande um ok ou salve o nosso número.

O acesso ao Drive é via Poder Monitor.
se você ainda não tem senha, é fácil:
o e-mail de login é o mesmo pelo qual você recebe o Drive e a senha é: monitor@123

Pronto. É um procedimento único e simples. Depois, não precisa mais repetir.

*É recomendado alterar a senha depois do primeiro acesso*'''

nums = ["556193008378@c.us","556183773136@c.us","556192022662@c.us", "556181512236@c.us", "556198557131@c.us"]
wpp = WhatsappServer(host= host, session_name= session_name, api_key=api_key)

print(wpp.start_session())
print(wpp.get_status())

print(wpp.send_message('556183773136@c.us', msg))

# for num in nums:
#     print(wpp.send_message(f'{num}',msg))
#     time.sleep(1)
