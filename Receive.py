import socket, dataBase

UDP_IP = "169.254.135.223" # Direccion IP Destino
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, # Internet
                socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print ("MENSAJE:"), data
    if data != None:
        dataS = data.split()
        modo = dataS[0]
        horas = dataS[1]
        placa = dataS[2]

        dataBase.SEND(129323720,data)
