import sys, os                                                             #Se importa esta biblioteca para manejar comandos de terminal linux desde Python

def SEND(chatid,message):                                                  #Se define esta funcion para ingresar como parametros el destinatario y el mensaje a enviar por Telegram
    command = 'echo %s | ./teleSEND.sh %d' %(message,chatid)               #El comando se ingresa como un string parametrizado
    os.system(command)                                                     #Esta linea ejecuta el comando de terminal y, por lo tanto, el ShellScript que enviara el mensaje

SEND(129323720,'Soy un bot que cobra peajes y parqueos.')                  #Se llama a la funcion con los parametros a utilizar
SEND(331057468,'Soy un bot que cobra peajes y parqueos.')
SEND(204802873,'Soy un bot que cobra peajes y parqueos.')
SEND(163482829,'Soy un bot que cobra peajes y parqueos.')
SEND(196505168,'Soy un bot que cobra peajes y parqueos, malparido.')
