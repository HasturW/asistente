import speech_recognition as sr
import pyttsx3
import threading

r=sr.Recognizer()
voz=pyttsx3.init()

def habla(texto):
    voz.say(texto)
    voz.runAndWait()

def escucha():   
    '''def detener_escucha():
        r.stop_listening() '''

    with sr.Microphone() as source:
        print ("¿Qué quieres que haga por ti?")
        #habla("¿Qué quieres que haga por ti?")
        try:
            audio=r.listen(source, timeout=5)
        except sr.WaitTimeoutError:
            return ''
        


    try:
        query = r.recognize_google(audio, language='es-ES')
        print (f'Has dicho: {query}')
        return query
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return ''
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return ''
    
    

while True:
   peticion=escucha().lower()
   if peticion == "oye raspi":
       habla("Hola, ¿Qué necesitas?")
   if peticion =="salir":
       habla ("Hasta luego")
       break
