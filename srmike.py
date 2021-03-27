"""Hola a todos!

Este es un asistente virtual, 100% creado con python en donde hacemos uso de varias liberias

Creado por Miguel Angel Cardona Contreras

Cesun universidad

correo: mikecardona076@gmail.com
"""


#Importamos librerias
import tkinter as tk
import pyttsx3
import habilidades
from tkinter import *
######################

##########################################################################################
#La clase de nuestro asistente
class SrMike(tk.Frame):
    def __init__(self, __padre__, *pargs):
        super(SrMike,self).__init__(__padre__, *pargs)

    def __main__(self):
        self.bienvenida()


    def bienvenida(self):
        mike = pyttsx3.init()
        voices = mike.getProperty('voices')
        mike.setProperty('voice', voices[0].id)
        mike.say("Hola Usuario, en que puedo ayudarte?")
        mike.runAndWait()
        self.habilidades()

    def habilidades(self):

        habilidad_3 = tk.Button(self, text="Ordenar", command=habilidades.busqueda)
        habilidad_3.pack()
        habilidad_3.config(font=("Times New Roman", 20))
##########################################################################################



##########################################################################################
#Main de nuestro programa
if __name__ == "__main__":
    screen = tk.Tk()
    screen.geometry("500x500") #Establecemos el tamano de nuestra ventana
    screen.title("Sr Mike")
    screen.configure(bg='black')

    #Aqui traemos a nuestro asistente a nuestra ventana
    mike = SrMike(screen)
    mike.pack()
    mike.__main__()

    #Le ponemos un gift a nuestro asisente
    """Cargar el Gift"""
    framesNum = 30
    archivo = "gallery/mike.gif"

    # Lista de todas las imagenes del gif
    frames = [tk.PhotoImage(file=archivo, format='gif -index %i' % (i)) for i in range(framesNum)]


    def update(ind):
        """ Actualiza la imagen gif """
        frame = frames[ind]
        ind += 1
        if ind == framesNum:
            ind = 0
        canvas.create_image(-90, -90, image=frame, anchor=NW)
        screen.after(40, update, ind)


    screen.after(0, update, 0)
    canvas = tk.Canvas(width=300, height=300)
    canvas.pack()
    screen.mainloop()