import tkinter as tk
import tkinter.font as tkFont
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox

from diagramador import Diagramador

class New_card(tk.Frame):
    def __init__(self, conector, ventana, last_id, *args, **kwargs):
        self.ventana = ventana
        self.conector = conector
        self.otra_ventana = tk.Toplevel(ventana)
        self.otra_ventana.geometry("900x500")
        self.otra_ventana.title("Crear tarjeta")
        self.otra_ventana['bg'] = '#9575cd'
        self.last_id = last_id

        #self.button1 = tk.Button(self.otra_ventana, text="Copiar partida", fg='white', bg='#65499c')
        #self.button1.place(x=740, y=20)
        #self.button2 = tk.Button(self.otra_ventana, text="Copiar diagrama", fg='white', bg='#65499c')
        #self.button2.place(x=740, y=60)
        self.button3 = tk.Button(self.otra_ventana, text="Crear diagrama", fg='black', bg='#c7a4ff', command=self.crea_diagrama)
        self.button3.place(x=740, y=100)
        self.button4 = tk.Button(self.otra_ventana, text="Limpiar tarjeta", fg='black', bg='#c7a4ff')
        self.button4.place(x=740, y=140)
        self.button5 = tk.Button(self.otra_ventana, text="Limpiar posición", fg='black', bg='#c7a4ff')
        self.button5.place(x=740, y=180)
        self.button6 = tk.Button(self.otra_ventana, text="Limpiar tema", fg='black', bg='#c7a4ff')
        self.button6.place(x=740, y=220)
        self.button7 = tk.Button(self.otra_ventana, text="Limpiar todo", fg='black', bg='#c7a4ff')
        self.button7.place(x=740, y=260)
        self.button8 = tk.Button(self.otra_ventana, text="Añadir tarjeta", fg='black', bg='#c7a4ff', command = self.crea_tarjeta)
        self.button8.place(x=740, y=300)
        self.button9 = tk.Button(self.otra_ventana, text="Cancelar", fg='black', bg='#c7a4ff', command = self.otra_ventana.destroy)
        self.button9.place(x=740, y=360)

        nombre_label = tk.Label(self.otra_ventana, text='Nombre', bg='#9575cd', fg="black")
        nombre_label.place(x=30, y=20)
        self.nombre = tk.Entry(self.otra_ventana)
        self.nombre.place(x=30, y=40)
        titulo_label = tk.Label(self.otra_ventana, text='Tema', bg='#9575cd', fg="black")
        titulo_label.place(x=30, y=80)
        self.titulo = tk.Entry(self.otra_ventana)
        self.titulo.place(x=30, y=100)
        
        tajeta_label = tk.Label(self.otra_ventana, text='Tarjeta: ', bg='#9575cd', fg="black")
        tajeta_label.place(x=20, y = 150)
        self.tarjeta = tk.Text(self.otra_ventana, width=40, height=18)
        self.tarjeta.place(x=20, y=170)
        posicion_label = tk.Label(self.otra_ventana, text='Posición: ', bg='#9575cd', fg="black")
        posicion_label.place(x=390, y=150)
        self.font = tkFont.Font(family="Chess Cases", size=23)
        self.posicion = tk.Text(self.otra_ventana, width=16, height=9.5, font=self.font)
        self.posicion.place(x=390, y=170)

    def leer_partida(self):
        self.tabla = None
        self.list_game = []
        try:
            path = filedialog.askopenfilename(title="Abrir partida", initialdir="./", filetypes=[("Text files","*.pgn"), ("All file", "*.*")])
            archivo = open(path,'r', encoding='utf-8', errors='ignore')
            first_game = chess.pgn.read_game(archivo)
            board = first_game.board()
            #print(board)

            #self.game = pgn.loads(lista)
            archivo.close()  # cierra archivo
        except FileNotFoundError as e:
            messagebox.showerror(title="ERROR", message="No se encontró el archivo, por favor validalo e intentalo de nuevo")
        except TypeError as e:
            messagebox.showerror(title="ERROR", message="El formato del archivo no es válido o no se seleccionó uno, por favor validalo e intentalo de nuevo")

    def campos_validos(self):
        if self.nombre.get() != '' and self.titulo.get() != '' and self.tarjeta.get("1.0", "end-1c") != '' and self.posicion.get("1.0", "end-1c") != '':
            return True
        return False

    def crea_tarjeta(self):
        if self.campos_validos():
            #print(self.last_id)
            #print(self.nombre.get())
            #print(self.titulo.get())
            #print(self.tarjeta.get("1.0", "end-1c"))
            #print(self.posicion.get("1.0", "end-1c"))
            nombre = self.nombre.get()
            titulo = self.titulo.get()
            tarjeta = self.tarjeta.get("1.0", "end-1c")
            posicion = self.posicion.get("1.0", "end-1c")
            completo = self.conector.insertar(self.last_id, nombre, titulo, tarjeta, posicion)
            self.otra_ventana.destroy()
        else:
            messagebox.showerror(title="ERROR", message="Alguno de los campos está vacío, por favor validalo e intentalo de nuevo")

    def crea_diagrama(self):
        diagrama = Diagramador(self.otra_ventana, self.posicion)
