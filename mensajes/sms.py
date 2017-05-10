import sys, os

def SEND(chatid,message):
    command = 'echo %s | ./teleSEND.sh %d' %(message,chatid)
    os.system(command)

SEND(129323720,'Soy un bot que cobra peajes y parqueos.')
