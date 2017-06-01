import socket, dataBase

UDP_IP = "169.254.135.223" #Direccion IP Destino
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
        chatID = dataBase.buscarID(placa)
        mensaje = ''
        precio = 150
        precioHoras = 850*int(horas)
        if modo == 'peaje':
            mensaje = ('Usted tiene un cobro de peaje pendiente por %d colones, al vehículo con placa %s.' %(precio, placa))
        else if modo == 'parqueo':
            mensaje = ('El monto a pagar por %s de parqueo es de %d colones, al vehículo con placa %s.' %(horas, precioHoras, placa))
        dataBase.SEND(chatID,mensaje)
