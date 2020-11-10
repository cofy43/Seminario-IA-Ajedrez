import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
from tkinter import filedialog
import os
from PIL import ImageTk, Image
import io
from db_connector import Db_connector
#Rn = Ro + K(W - We)

class Principal():
    def __init__(self) :
        self.ventana = tk.Tk()
        self.ventana.geometry("690x690")
        self.ventana.title("Targetero")
        self.ventana['bg'] = '#344266'
        self.connector = Db_connector()
        self.connector.connect()

if __name__ == "__main__":
    juego  = Principal()
    juego.ventana.mainloop() 
    pass