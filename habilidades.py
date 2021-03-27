import webbrowser as wb
import pyttsx3
from datetime import datetime
import speech_recognition as sr

def abrir_facebook():
    wb.open("https://www.facebook.com/")


def decir_hora():
    hora = pyttsx3.init()
    voices = hora.getProperty('voices')
    hora.setProperty('voice', voices[3].id)
    hora.say(f"La hora actual es {datetime.now()}")
    hora.runAndWait()

def busqueda():
    r = sr.Recognizer()
    with sr.Microphone(device_index=15) as source:
        print("Hola, que deseas buscar")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(f"Dijiste {text}")
        except:
            print("No pude escucharte!")

