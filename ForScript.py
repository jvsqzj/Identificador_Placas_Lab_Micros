#!/usr/bin/python
# -*- coding: utf-8 -*- # Para caracteres especiales.

import os # Acceso a terminal.
from Tkinter import * # Para interfaz grafica.

def execute(f):
    W0.after(200,f)

def printf(text):
    print text # Imprime un texto

def exe_script():
    os.system("./Script.sh")

W0 = Tk() # Abre ventana.

B1 = Button(W0, text="Tomar foto y procesar", command=lambda: exe_script()).pack()

B2 = Button(W0, text="Salir", command=lambda: W0.destroy()).pack()

W0.mainloop() # Bucle principal.
