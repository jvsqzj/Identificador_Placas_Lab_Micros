#!/usr/bin/python
# -*- coding: utf-8 -*- # Para caracteres especiales.

import os # Acceso a terminal.
import random # Para números random.
from Tkinter import * # Para interfaz gráfica.
import Main

def show(window): # Mostrar ventana.
    window.deiconify()

def hide(window): # Ocultar ventana.
    window.withdraw()

def execute(f): # Ejecutar función después de 2ms.
    W0.after(200,f)

def printf(text): # Imprime un texto
    print text

def exe_parking(): # Función para fotografiar en parqueo.
    print "Se tomará una fotografía.\n"
    os.system("sleep 1s")
    os.system("fswebcam --no-banner foto.png")  # Toma foto con web cam.
    print "\nLa fotografía fue tomada."
    os.system("sleep 1s")
    print "Por favor espere mientras se procesa la fotografía."
    Main.main("parqueo", str(random.randrange(11))) # Le envía a main strings con el dato de que es parqueo y tiempo aleatorio.
    print "\nSistema de Parqueo\n--------------------*"

def exe_toll(): # Función para fotografiar en peaje.
    print "Se tomará una fotografía.\n"
    os.system("sleep 1s")
    os.system("fswebcam --no-banner foto.png") # Toma foto con web cam.
    print "\nLa fotografía fue tomada."
    os.system("sleep 1s")
    print "Por favor espere mientras se procesa la fotografía."
    Main.main("peaje", "0")  # Le envía a main strings con el dato de que es peaje y tiempo 0 pues no aplica.
    print "\nSistema de Peaje\n--------------------*"

W0 = Tk() # Abre ventana principal.
W0.geometry("350x225") # Tamaño de ventana.
W0.title("Identificación de Placas Vehiculares") # Título de ventana.
W0.config(bg = "gray70")
print "\nBienvenido al Programa de Identificación de Placas Vehiculares.\n\nSistema Principal.\n--------------------*"


W1 = Toplevel(W0) # Ventana hija 1.
W1.protocol("WM_DELETE_WINDOW", "onexit") # Elimina la opción de salir para evitar el error.
W1.geometry("230x150")
W1.title("Sistema de Peaje")
W1.config(bg = "gray75")


W2 = Toplevel(W0) # Ventana hija 2.
W2.protocol("WM_DELETE_WINDOW", "onexit") # Elimina la opción de salir para evitar el error.
W2.geometry("230x150")
W2.title("Sistema de Parqueo")
W2.config(bg = "gray75")

# Botones.
B0 = Button(W0, text="Sistema Peaje", cursor="hand1", background="gray80", borderwidth=5, command = lambda: printf("\nSistema de Peaje.\n--------------------*") or execute(hide(W2)) or execute(show(W1))).pack(fill=BOTH, expand=1)
B1 = Button(W0, text="Sistema Parqueo", cursor="hand2", background="gray80", borderwidth=5, command = lambda: printf("\nSistema de Parqueo\n--------------------*") or execute(hide(W1)) or execute(show(W2))).pack(fill=BOTH, expand=1)
B2 = Button(W0, text="Salir", background="gray80", borderwidth=3, command = lambda: printf("\nFin del programa.\n") or W0.destroy()).pack(fill=BOTH, expand=1)

B3 = Button(W1, text="Fotografiar", background="gray80", borderwidth=5, command = lambda: exe_toll()).pack(fill=BOTH, expand=1)
B4 = Button(W1, text="Volver", background="gray80", borderwidth=3, command = lambda: printf("\nSistema Principal.\n--------------------*") or execute(hide(W1))).pack(fill=BOTH, expand=1)

B5 = Button(W2, text="Fotografiar", background="gray80", borderwidth=5, command = lambda: exe_parking()).pack(fill=BOTH, expand=1)
B6 = Button(W2, text="Volver", background="gray80", borderwidth=3, command = lambda: printf("\nSistema Principal.\n--------------------*") or execute(hide(W2))).pack(fill=BOTH, expand=1)

hide(W1)
hide(W2)
W0.mainloop() # Bucle principal.
