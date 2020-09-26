#!/usr/bin/env python

import tkinter as tk

OptionList = [
"Chess Assistant",
"Tilburg",
"TascBase",
"ChessBase",
"Cheq True Type",
"Marroquin"
]

# Definición de ventana
ventana = tk.Tk()

ventana.geometry("800x600")
ventana.title("Diagrama de Ajedrez")

#  Funciones para los botones

def leer_partida():
    print("Aqui va el codigo para cargar archivo")

def salvar_partida():
    print("Aqui va el codigo para salvar archivo")

def nueva_partida():
    print("Aqui va el codigo para crear una nueva partida")

def capturar_imagen():
    print("Aqui va el codigo para capturar imagen")

def diagrama_html():
    print("Aqui va el codigo para diagrama html")

# Definiciones de botones

boton1 = tk.Button(ventana, text="Leer partida", command = leer_partida)
boton1.pack()
boton1.place(x=10, y=10)

boton2 = tk.Button(ventana, text="Salvar partida", command = salvar_partida)
boton2.pack()
boton2.place(x=150, y=10)

tipografias = tk.StringVar(ventana)
tipografias.set(OptionList[0])

opciones = tk.OptionMenu(ventana, tipografias, *OptionList)
opciones.config(font=('Helvetica', 12))
opciones.pack()
opciones.place(x=305, y=10)

boton3 = tk.Button(ventana, text="Nueva partida", command = nueva_partida)
boton3.pack()
boton3.place(x=500, y=10)

boton5 = tk.Button(ventana, text="Capturar imagen", command = capturar_imagen)
boton5.pack()
boton5.place(x=650, y=10)

boton6 = tk.Button(ventana, text="Diagrama html", command = diagrama_html)
boton6.pack()
boton6.place(x=250, y=60)

button = tk.Button(ventana ,text = "Cerrar", command = ventana.destroy)
button.pack()
button.place(x=400, y=60)

#panel = tk.Label(ventana, image = img)
#panel.pack(side = "bottom", fill = "both", expand = "yes")

ventana.mainloop()