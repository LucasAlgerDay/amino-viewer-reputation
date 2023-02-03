import aminofix
from os import path
import json
from time import sleep
from pyfiglet import figlet_format
from colored import fore, style

print(
    f"""{fore.CADET_BLUE_1 + style.BOLD}
    Chat reputation
Script by Lucas Day
Github : https://github.com/LucasAlgerDay"""
)
print(figlet_format("Chat reputation", font="fourtops"))



THIS_FOLDER=path.dirname(path.abspath(__file__))
emailfile=path.join(THIS_FOLDER,'accounts.json')
dictlist=[]
chatlink = input("Chat link: ")
cooldown = int(input("Cooldown por cuenta: "))
with open(emailfile)as f:dictlist=json.load(f)


print(f"{len(dictlist)} cuentas cargadas")

for acc in dictlist:
    email = acc['email']
    password =  acc['password']
    device = acc['device']
    client = aminofix.Client(deviceId = device)
    try:
        client.login(email=email, password=password)
        chat_info = client.get_from_code(chatlink)
        chat_id = chat_info.objectId
        community_id = chat_info.path[1:chat_info.path.index('/')]
        client.join_community(community_id)
        sub_client = aminofix.SubClient(comId=community_id, profile=client.profile)
        sub_client.join_chat(chat_id)
        client.join_video_chat_as_viewer(comId=community_id, chatId=chat_id)
        print(f"{email} Ingresado en el chat, esperando {cooldown} para la siguiente cuenta")
        sleep(cooldown)
    except Exception as e:
        print(f"Error en la siguiente cuenta {email}: {e} \n\n\n Esperando {cooldown} para la siguiente cuenta.")
        sleep(cooldown)
        pass