import pywhatkit
import keyboard
import time
from datetime import datetime

contatos =['+5511947706214']
while len(contatos)>=1:
    pywhatkit.sendwhatmsg(contatos[0],'Teste',datetime.now().hour,datetime.now().minute+2)
    del contatos[0]
    time.sleep(15)
    keyboard.press_and_release('ctrl +w')