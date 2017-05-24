#Funcion para encontrar el ID correspondiente a una placa


import sys, os
import csv, operator

def buscarID(placa):
    with open('info.csv') as csvarchivo:
        entrada = csv.reader(csvarchivo)
        for register in entrada:
           if register[0] == str(placa):
                print(register[1])

def agregarDatos(placa, ID):
    csvsalida = open('info.csv', 'a', newline='')
    salida = csv.writer(csvsalida)
    salida.writerow([placa, ID])
    del salida
    csvsalida.close()

def SEND(chatid,message):                                                  #Se define esta funcion para ingresar como parametros el destinatario y el mensaje a enviar por Telegram
    command = 'echo %s | ./teleSEND.sh %d' %(message,chatid)               #El comando se ingresa como un string parametrizado
    os.system(command)                                                     #Esta linea ejecuta el comando de terminal y, por lo tanto, el ShellScript que enviara el mensaje
