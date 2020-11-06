import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
from tkinter import filedialog
import os
from PIL import ImageTk, Image
import io
#Rn = Ro + K(W - We)

class Principal():
    def __init__(self) :
        self.ventana = tk.Tk()
        self.ventana.geometry("690x690")
        self.ventana.title("Calculadora de ELO")
        self.ventana['bg'] = '#344266'
        #root.iconbitmap('/path/to/ico/icon.ico')
        self.ventana.tk.call('wm', 'iconphoto', self.ventana._w, tk.PhotoImage(file='img/chess-pieces.png'))
        #Logo
        self.icon = ImageTk.PhotoImage(Image.open('img/logo-fide.png'))
        self.icon_size = Label(self.ventana,image=self.icon, width=288, height=198)
        self.icon_size.image = self.icon  # <== this is were we anchor the img object
        self.icon_size.pack(side=LEFT)
        self.icon_size.place(x=370, y=10)

        content = IntVar()
        vcmd = (self.ventana.register(self.validate),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        #Campos necesarios 
        k_value_label = tk.Label(self.ventana, text='introduce un valor para k', bg='#344266', fg="white")
        k_value_label.place(x=30, y=40)
        self.k_value = tk.Entry(self.ventana, validate = 'key', validatecommand = vcmd)
        self.k_value.place(x=30, y=60)
        ro_label = tk.Label(self.ventana, text='Ranquing actual', bg='#344266', fg="white")
        ro_label.place(x=30, y=100)
        self.ro = tk.Entry(self.ventana, validate = 'key', validatecommand = vcmd)
        self.ro.place(x=30, y=120)
        games_label = tk.Label(self.ventana, text='Número de rondas', bg='#344266', fg="white")
        games_label.place(x=30, y=160)
        self.games = tk.Entry(self.ventana, validate = 'key', validatecommand = vcmd)
        self.games.place(x=30, y=180)
        wined_label = tk.Label(self.ventana, text='Total de puntos', bg='#344266', fg="white")
        wined_label.place(x=30, y=220)
        self.wined = tk.Entry(self.ventana, validate = 'key', validatecommand = vcmd)
        self.wined.place(x=30, y=240)
        average_label = tk.Label(self.ventana, text='Promedio de los rivales', bg='#344266', fg="white")
        average_label.place(x=30, y=280)
        self.average = tk.Entry(self.ventana, validate = 'key', validatecommand = vcmd)
        self.average.place(x=30, y=300)

        #Resultados
        new_ranking = tk.Label(self.ventana, text='Ranquing nuevo:', bg='#344266', fg="white")
        new_ranking.place(x = 380, y=240)
        self.result_new_ranking = tk.Label(self.ventana, text='0.0', bg='#344266', fg="white")
        self.result_new_ranking.place(x = 500, y=240)
        performance = tk.Label(self.ventana, text='Desempeño:', bg='#344266', fg="white")
        performance.place(x = 380, y=280)
        self.result_performance = tk.Label(self.ventana, text='0.0', bg='#344266', fg="white")
        self.result_performance.place(x = 470, y=280)
        diference = tk.Label(self.ventana, text='Diferencia:', bg='#344266', fg="white")
        diference.place(x = 380, y=320)
        self.result_diference = tk.Label(self.ventana, text='0.0', bg='#344266', fg="white")
        self.result_diference.place(x = 460, y=320)
        

        #Botones
        calculate_button = tk.Button(self.ventana, text="Calcular", command = self.calculate, fg='black', bg='white')
        calculate_button.place(x = 230, y = 204)
        clean_button = tk.Button(self.ventana, text="Limpiar", command = self.clean, fg='black', bg='white')
        clean_button.place(x = 230, y = 250)
        exit_button = tk.Button(self.ventana, text="Salir", command = self.ventana.destroy, fg='black', bg='white')
        exit_button.place(x = 230, y = 296)

        #Oponentes
        tite_oponets = tk.Label(self.ventana, text="Ranquing de los oponentes:", bg='#344266', fg="white")
        tite_oponets.place(x = 30, y= 330)

        self.oponent_1 = tk.Entry(self.ventana, validate = 'key', validatecommand = vcmd)
        self.oponent_1.place(x = 50, y=360)
        oponent_1_label = tk.Label(self.ventana, text="1)", bg='#344266', fg="white")
        oponent_1_label.place(x=30, y=360)
        self.oponent_2 = tk.Entry(self.ventana, validate = 'key', validatecommand = vcmd)
        self.oponent_2.place(x = 50, y=400)
        oponent_2_label = tk.Label(self.ventana, text="2)", bg='#344266', fg="white")
        oponent_2_label.place(x=30, y=400)
        self.oponent_3 = tk.Entry(self.ventana, validate = 'key', validatecommand = vcmd)
        self.oponent_3.place(x = 50, y=440)
        oponent_3_label = tk.Label(self.ventana, text="3)", bg='#344266', fg="white")
        oponent_3_label.place(x=30, y=440)
        self.oponent_4 = tk.Entry(self.ventana, validate = 'key', validatecommand = vcmd)
        self.oponent_4.place(x = 50, y=480)
        oponent_4_label = tk.Label(self.ventana, text="4)", bg='#344266', fg="white")
        oponent_4_label.place(x=30, y=480)
        self.oponent_5 = tk.Entry(self.ventana, validate = 'key', validatecommand = vcmd)
        self.oponent_5.place(x = 50, y=520)
        oponent_5_label = tk.Label(self.ventana, text="5)", bg='#344266', fg="white")
        oponent_5_label.place(x=30, y=520)
        self.oponent_6 = tk.Entry(self.ventana, validate = 'key', validatecommand = vcmd)
        self.oponent_6.place(x = 50, y=560)
        oponent_6_label = tk.Label(self.ventana, text="6)", bg='#344266', fg="white")
        oponent_6_label.place(x=30, y=560)
        self.oponent_7 = tk.Entry(self.ventana, validate = 'key', validatecommand = vcmd)
        self.oponent_7.place(x = 50, y=600)
        oponent_7_label = tk.Label(self.ventana, text="7)", bg='#344266', fg="white")
        oponent_7_label.place(x=30, y=600)
        
        self.oponent_8 = tk.Entry(self.ventana, validate = 'key', validatecommand = vcmd)
        self.oponent_8.place(x = 277, y=360)
        oponent_8_label = tk.Label(self.ventana, text="8)", bg='#344266', fg="white")
        oponent_8_label.place(x=253, y=360)
        self.oponent_9 = tk.Entry(self.ventana, validate = 'key', validatecommand = vcmd)
        self.oponent_9.place(x=277, y=400)
        oponent_9_label = tk.Label(self.ventana, text="9)", bg='#344266', fg="white")
        oponent_9_label.place(x=253, y=400)
        self.oponent_10 = tk.Entry(self.ventana, validate = 'key', validatecommand = vcmd)
        self.oponent_10.place(x=277, y=440)
        oponent_10_label = tk.Label(self.ventana, text="10)", bg='#344266', fg="white")
        oponent_10_label.place(x=253,y=440)
        self.oponent_11 = tk.Entry(self.ventana, validate = 'key', validatecommand = vcmd)
        self.oponent_11.place(x=277, y=480)
        oponent_11_label = tk.Label(self.ventana, text="11)", bg='#344266', fg="white")
        oponent_11_label.place(x=253, y=480)
        self.oponent_12 = tk.Entry(self.ventana, validate = 'key', validatecommand = vcmd)
        self.oponent_12.place(x=277, y=520)
        oponent_12_label = tk.Label(self.ventana, text="12)", bg='#344266', fg="white")
        oponent_12_label.place(x=253, y=520)
        self.oponent_13 = tk.Entry(self.ventana, validate = 'key', validatecommand = vcmd)
        self.oponent_13.place(x=277, y=560)
        oponent_13_label = tk.Label(self.ventana, text="13)", bg='#344266', fg="white")
        oponent_13_label.place(x=253, y=560)
        self.oponent_14 = tk.Entry(self.ventana, validate = 'key', validatecommand = vcmd)
        self.oponent_14.place(x=277, y=600)
        oponent_14_label = tk.Label(self.ventana, text="14)", bg='#344266', fg="white")
        oponent_14_label.place(x=253, y=600)

        self.oponent_15 = tk.Entry(self.ventana, validate = 'key', validatecommand = vcmd)
        self.oponent_15.place(x = 505, y=360)
        oponent_15_label = tk.Label(self.ventana, text="15)", bg='#344266', fg="white")
        oponent_15_label.place(x=480, y=360)
        self.oponent_16 = tk.Entry(self.ventana, validate = 'key', validatecommand = vcmd)
        self.oponent_16.place(x=505, y=400)
        oponent_16_label = tk.Label(self.ventana, text="16)", bg='#344266', fg="white")
        oponent_16_label.place(x=480, y=400)
        self.oponent_17 = tk.Entry(self.ventana, validate = 'key', validatecommand = vcmd)
        self.oponent_17.place(x=505, y=440)
        oponent_17_label = tk.Label(self.ventana, text="17)", bg='#344266', fg="white")
        oponent_17_label.place(x=480,y=440)
        self.oponent_18 = tk.Entry(self.ventana, validate = 'key', validatecommand = vcmd)
        self.oponent_18.place(x=505, y=480)
        oponent_18_label = tk.Label(self.ventana, text="18)", bg='#344266', fg="white")
        oponent_18_label.place(x=480, y=480)
        self.oponent_19 = tk.Entry(self.ventana, validate = 'key', validatecommand = vcmd)
        self.oponent_19.place(x=505, y=520)
        oponent_19_label = tk.Label(self.ventana, text="19)", bg='#344266', fg="white")
        oponent_19_label.place(x=480, y=520)
        self.oponent_20 = tk.Entry(self.ventana, validate = 'key', validatecommand = vcmd)
        self.oponent_20.place(x=505, y=560)
        oponent_20_label = tk.Label(self.ventana, text="20)", bg='#344266', fg="white")
        oponent_20_label.place(x=480, y=560)
        self.oponent_21 = tk.Entry(self.ventana, validate = 'key', validatecommand = vcmd)
        self.oponent_21.place(x=505, y=600)
        oponent_21_label = tk.Label(self.ventana, text="21)", bg='#344266', fg="white")
        oponent_21_label.place(x=480, y=600)
        self.expected_vs_difference = self.generator_values_to_dictionary()

    def calculate(self):
        """
        Método principal encargado del cálculo del ranquing ELO
        Siempre y cuando el campo de Promedio de los rivales o al menos alguno de
        el de los contrincantes esté lleno.
        """
        average = 0
        if self.average.get() == '':
            average = self.get_average()
        else:
            average = float(self.average.get())

        if (average == 0) or self.some_imput_empty():
            messagebox.showerror(title="ERROR", message="Por favor verifica que los campos para k, Ranquing actual, Número de rondas, Total de puntos y Promedio de los rivales o al menos un de los campor de los rivales esten llenos")
        else:
            k = float(self.k_value.get())
            ro = float(self.ro.get())
            w = float(self.wined.get())
            we = ro - average
            wef = self.get_raiting_expected(we)
            games = float(self.games.get())
            #wef * games 
            temp1 = (wef * games)
            #w - (wef * games)
            temp2 = w - (wef * games)
            #k * (w - (wef * games)
            temp3 = (k * temp2)
            result = ro - temp3
            new = ro + temp3
            temp3 = format(temp3, '.2f')
            result = format(result, '.2f')
            average = format(average, '.2f')
            self.average.delete(0, END)
            self.average.insert(0, average)
            self.result_new_ranking.config(text=new)
            self.result_performance.config(text=average)
            self.result_diference.config(text=temp3)

    def some_imput_empty(self):
        """
        Método encargado de la verificación de la existencia
        de datos mínimos para el cálculo del ELO
        """
        if self.ro.get == '' or self.k_value.get() == '' or self.games.get() == '' or self.wined.get() == '':
            return True
        return False

    def get_average(self):
        """
        Método que devuelve el promedo de ranquing de la lista 
        de los rivales
        """
        total = 0
        number = 0
        if self.oponent_1.get() != '':
            total += float(self.oponent_1.get())
            number += 1
        if self.oponent_2.get() != '':
            total += float(self.oponent_2.get())
            number += 1
        if self.oponent_3.get() != '':
            total += float(self.oponent_3.get())
            number += 1
        if self.oponent_4.get() != '':
            total += float(self.oponent_4.get())
            number += 1
        if self.oponent_5.get() != '':
            total += float(self.oponent_5.get())
            number += 1
        if self.oponent_6.get() != '':
            total += float(self.oponent_6.get())
            number += 1
        if self.oponent_7.get() != '':
            total += float(self.oponent_7.get())
            number += 1
        if self.oponent_8.get() != '':
            total += float(self.oponent_8.get())
            number += 1
        if self.oponent_9.get() != '':
            total += float(self.oponent_9.get())
            number += 1
        if self.oponent_10.get() != '':
            total += float(self.oponent_10.get())
            number += 1
        if self.oponent_11.get() != '':
            total += float(self.oponent_11.get())
            number += 1
        if self.oponent_12.get() != '':
            total += float(self.oponent_12.get())
            number += 1
        if self.oponent_13.get() != '':
            total += float(self.oponent_13.get())
            number += 1
        if self.oponent_14.get() != '':
            total += float(self.oponent_14.get())
            number += 1
        if self.oponent_15.get() != '':
            total += float(self.oponent_15.get())
            number += 1
        if self.oponent_16.get() != '':
            total += float(self.oponent_16.get())
            number += 1
        if self.oponent_17.get() != '':
            total += float(self.oponent_17.get())
            number += 1
        if self.oponent_18.get() != '':
            total += float(self.oponent_18.get())
            number += 1
        if self.oponent_19.get() != '':
            total += float(self.oponent_19.get())
            number += 1
        if self.oponent_20.get() != '':
            total += float(self.oponent_20.get())
            number += 1
        if self.oponent_21.get() != '':
            total += float(self.oponent_21.get())
            number += 1
        if number != 0:
            return total / number
        return 0
        
    def clean(self):
        """
        Método encargado de limpiar todos los campos
        así como los resultados preciamente optenidos.
        """
        self.k_value.delete(0, END)
        self.ro.delete(0, END)
        self.games.delete(0, END)
        self.wined.delete(0, END)
        self.average.delete(0, END)
        self.oponent_1.delete(0, END)
        self.oponent_2.delete(0, END)
        self.oponent_3.delete(0, END)
        self.oponent_4.delete(0, END)
        self.oponent_5.delete(0, END)
        self.oponent_6.delete(0, END)
        self.oponent_7.delete(0, END)
        self.oponent_8.delete(0, END)
        self.oponent_9.delete(0, END)
        self.oponent_10.delete(0, END)
        self.oponent_11.delete(0, END)
        self.oponent_12.delete(0, END)
        self.oponent_13.delete(0, END)
        self.oponent_14.delete(0, END)
        self.oponent_15.delete(0, END)
        self.oponent_16.delete(0, END)
        self.oponent_17.delete(0, END)
        self.oponent_18.delete(0, END)
        self.oponent_19.delete(0, END)
        self.oponent_20.delete(0, END)
        self.oponent_21.delete(0, END)
        self.result_new_ranking.config(text='0.0')
        self.result_performance.config(text='0.0')
        self.result_diference.config(text='0.0')

    def get_raiting_expected(self, we):
        """
        Método que devuelve el ranquing dado una una
        espectativa de partidas ganadas
        """
        if we >= 677:
            return .99
        
        if we <= -677:
            return -.99

        list = [(k, v) for k, v in self.expected_vs_difference.items()]
        i = 0
        for tupl in list:
            if int(tupl[0]) <= we:
                tupl_temp = list[i-1]
                return float(tupl_temp[1])
            else:
                i += 1
        


    def validate(self, action, index, value_if_allowed, prior_value, text, validation_type, trigger_type, widget_name):
        """
        Método encargado de delimitar los campos a 
        solo valores numéricos
        """
        if value_if_allowed == '':
            return True
        if value_if_allowed:
            try:
                float(value_if_allowed)
                return True
            except ValueError:
                return False
        else:
            return False

    def generator_values_to_dictionary(self):
        """
        Método encargado de optener los valores de 
        la tabla de ranquing dada una espectativa de 
        victorias
        """
        os.chdir("./") 
        fname = "rating_vs_differences.txt"
        fh= open(fname)
        dictionairy = dict()
        for line in fh:
            words = line.rstrip().split()
            dictionairy[words.pop(0)] = words.pop(1)
            words = ""
        
        return dictionairy

if __name__ == "__main__":
    juego  = Principal()
    juego.ventana.mainloop() 
    pass