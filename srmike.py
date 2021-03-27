import tkinter as tk
import pyttsx3
import habilidades

class SrMike(tk.Frame):
    def __init__(self, __padre__, *pargs):
        super(SrMike,self).__init__(__padre__, *pargs)

    def __main__(self):
        self.bienvenida()


    def bienvenida(self):
        mike = pyttsx3.init()
        voices = mike.getProperty('voices')
        mike.setProperty('voice', voices[3].id)
        mike.say("Hola Usuario, en que puedo ayudarte?")
        mike.runAndWait()
        self.habilidades()

    def habilidades(self):
        habilidad_1 = tk.Button(self, text="Abrir Facebook", command=habilidades.abrir_facebook)
        habilidad_1.pack()

        habilidad_2 = tk.Button(self, text="Decir la hora", command=habilidades.decir_hora)
        habilidad_2.pack()

        habilidad_2 = tk.Button(self, text="Busqueda", command=habilidades.busqueda)
        habilidad_2.pack()







if __name__ == "__main__":
    screen = tk.Tk()
    screen.geometry("500x500")
    screen.title("Sr Mike")
    screen.configure(bg='black')

    mike = SrMike(screen)
    mike.pack()
    mike.__main__()
    screen.mainloop()