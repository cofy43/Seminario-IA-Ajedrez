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

def leer_partida():
    print("Aqui va el codigo para cargar archivo")

boton1 = tk.Button(ventana, text="Leer partida", command = leer_partida)
boton1.pack()

def salvar_partida():
    print("Aqui va el codigo para salvar archivo")

boton2 = tk.Button(ventana, text="Salvar partida", command = salvar_partida)
boton2.pack()

tipografias = tk.StringVar(ventana)
tipografias.set(OptionList[0])

opciones = tk.OptionMenu(ventana, tipografias, *OptionList)
opciones.config(font=('Helvetica', 12))
opciones.pack()

def nueva_partida():
    print("Aqui va el codigo para crear una nueva partida")

boton3 = tk.Button(ventana, text="Nueva partida", command = nueva_partida)
boton3.pack()

def capturar_imagen():
    print("Aqui va el codigo para capturar imagen")

boton5 = tk.Button(ventana, text="Capturar imagen", command = capturar_imagen)
boton5.pack()

def diagrama_html():
    print("Aqui va el codigo para diagrama html")

boton6 = tk.Button(ventana, text="Diagrama html", command = diagrama_html)
boton6.pack()

button = tk.Button(ventana ,text = "Cerrar", command = ventana.destroy)
button.pack()

ventana.mainloop()