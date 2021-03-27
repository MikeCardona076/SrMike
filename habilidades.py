import webbrowser as wb
import pyttsx3
from datetime import datetime
import speech_recognition as sr

def decir_hora():
    hora = pyttsx3.init()
    voices = hora.getProperty('voices')
    hora.setProperty('voice', voices[3].id)
    hora.say(f"La hora actual es {datetime.now()}")
    hora.runAndWait()

def busqueda():
    buscar = pyttsx3.init()
    voices = buscar.getProperty('voices')
    buscar.setProperty('voice', voices[3].id)
    buscar.say("Hola, que deseas buscar")

    r = sr.Recognizer()
    with sr.Microphone(device_index=15) as source:


        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            buscar.say(f"Dijiste {text}")
            if "Facebook" in text:
                wb.open("https://www.facebook.com/")
        except:

            buscar.say("Perdon, no pude escucharte!")

    buscar.runAndWait()