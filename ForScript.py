#!/usr/bin/python
# -*- coding: utf-8 -*- # Para caracteres especiales.

import os # Acceso a terminal.
import random
from Tkinter import * # Para interfaz grafica.

def show(window):
    window.deiconify()

def hide(window):
    window.withdraw()

def execute(f):
    W0.after(200,f)

def printf(text):
    print text # Imprime un texto

def exe_script():
    os.system("./Script.sh")
    #print "Script."

def filetoll():
    f = open('archivo.txt', 'w')
    f.write('peaje\n0')
    f.close()

def fileparking():
    f2 = open('archivo.txt', 'w')
    a = random.randrange(11)
    b = str(a)
    f2.write('parqueo\n'+b)
    f2.close()

def funcionprueba():
    f3 = open('archivo.txt', 'a')
    f3.write('hola')
    f3.close()

W0 = Tk() # Abre ventana.

W1 = Toplevel(W0) # Ventana hija.
W2 = Toplevel(W0) # Ventana hija.
W1.protocol("WM_DELETE_WINDOW", "onexit") # Elimina la opción de salir para evitar el error.
W2.protocol("WM_DELETE_WINDOW", "onexit") # Elimina la opción de salir para evitar el error.

B0 = Button(W0, text="Sistema Peaje", command=lambda: execute(show(W1))).pack()
B1 = Button(W0, text="Sistema Parqueo", command=lambda: execute(show(W2))).pack()
B2 = Button(W0, text="Salir", command=lambda: W0.destroy()).pack()

B3 = Button(W1, text="Fotografiar", command=lambda: filetoll() or exe_script()).pack()
B4 = Button(W1, text="Cancelar", command=lambda: execute(hide(W1))).pack()

B5 = Button(W2, text="Fotografiar", command=lambda: fileparking() or exe_script()).pack()
B6 = Button(W2, text="Cancelar", command=lambda: execute(hide(W2))).pack()

W1.withdraw() # Oculta ventana.
W2.withdraw() # Oculta ventana.
W0.mainloop() # Bucle principal.
