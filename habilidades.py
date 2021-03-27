import webbrowser as wb
import pyttsx3
from datetime import datetime
import speech_recognition as sr


def busqueda():
    buscar = pyttsx3.init()
    voices = buscar.getProperty('voices')
    buscar.setProperty('voice', voices[0].id)

    r = sr.Recognizer()
    with sr.Microphone(device_index=15) as source:

        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            buscar.say(f"Dijiste {text}")

            if "date" in text:
                buscar.say(f"la fecha actual es {datetime.now()}")

            if "Facebook" in text:
                wb.open("https://www.facebook.com/")

            if "source code" in text:
                wb.open("https://github.com/MikeCardona076/SrMike")

        except:

            buscar.say("Perdon, no pude escucharte!")

    buscar.runAndWait()