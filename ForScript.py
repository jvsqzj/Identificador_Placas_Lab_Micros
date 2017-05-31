#!/usr/bin/python
# -*- coding: utf-8 -*- # Para caracteres especiales.

import os # Acceso a terminal.
import random
from Tkinter import * # Para interfaz grafica.
import Main

def show(window):
    window.deiconify()

def hide(window):
    window.withdraw()

def execute(f):
    W0.after(200,f)

def printf(text):
    print text # Imprime un texto

def exe_parking():
    os.system("./Script.sh")
    #print "Script."
    Main.main("parqueo", str(random.randrange(11)))

def exe_toll():
    os.system("./Script.sh")
    #print "Script."
    Main.main("peaje", "0")

W0 = Tk() # Abre ventana.
W0.geometry("500x500")
W0.title("Identificación de Placas Vehiculares")

W1 = Toplevel(W0) # Ventana hija.
W1.protocol("WM_DELETE_WINDOW", "onexit") # Elimina la opción de salir para evitar el error.
W1.geometry("250x250")
W1.title("Sistema de Peaje")

W2 = Toplevel(W0) # Ventana hija.
W2.protocol("WM_DELETE_WINDOW", "onexit") # Elimina la opción de salir para evitar el error.
W2.geometry("250x250")
W2.title("Sistema de Parqueo")

B0 = Button(W0, text="Sistema Peaje", command=lambda: execute(show(W1))).pack()
B1 = Button(W0, text="Sistema Parqueo", command=lambda: execute(show(W2))).pack()
B2 = Button(W0, text="Salir", command=lambda: W0.destroy()).pack()

B3 = Button(W1, text="Fotografiar", command=lambda: exe_toll()).pack()
B4 = Button(W1, text="Cancelar", command=lambda: execute(hide(W1))).pack()

B5 = Button(W2, text="Fotografiar", command=lambda: exe_parking()).pack()
B6 = Button(W2, text="Cancelar", command=lambda: execute(hide(W2))).pack()

W1.withdraw() # Oculta ventana.
W2.withdraw() # Oculta ventana.
W0.mainloop() # Bucle principal.
