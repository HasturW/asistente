import speech_recognition as sr
import pyttsx3
import threading
#import pywhatkit 
import os_ops as oo


r=sr.Recognizer()
voz=pyttsx3.init()
voz.setProperty('rate', 190)


def habla(texto):
    voz.say(texto)
    voz.runAndWait()

def escucha():   

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        #print ("¿Qué quieres que haga por ti?")
        #habla("¿Qué quieres que haga por ti?")
        try:
            r.pause_threshold = 0.8
            audio=r.listen(source)
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
    


    
    
if __name__=='__main__':
    while True:
       print ("¿Qué quieres que haga por ti?")
       peticion=escucha().lower()
       if peticion == "oye raspi":
           habla("Hola, ¿Qué necesitas?")
        # Seccion youtube
       ''' if  'youtube' in peticion:
                    while True:
                        habla('Vale, que quieres ver')
                        video=escucha().lower()
                        print (video)
                        if video == '':
                             print ("No te he entendido")                        
                        elif 'risitas' in video:
                            pywhatkit.playonyt('https://www.youtube.com/watch?v=QT13kk8HDDo')
                            break
                        else:
                             pywhatkit.playonyt(video)
                             break
        '''
        # Servicios de linux
            #Apache

       if ('levanta' in peticion or 'sube' in peticion or 'enciende' in peticion) and ('apache' in peticion or 'web' in peticion):
            print ("Levanto server de apache")
            habla ("Levanto server de apache")
            oo.apacheup()
       if ('tira' in peticion or 'apaga' in peticion) and ('apache' in peticion or 'web' in peticion):
            oo.apachedown()
            print ("Apago server de apache")
            habla ("Apago server de apache")

            #FTP

       if ('levanta' in peticion or 'sube' in peticion or 'enciende' in peticion) and 'ftp' in peticion:
            print ("Levanto server de FTP")
            habla ("Levanto server de FTP")
            oo.ftpup()
       if ('tira' in peticion or 'apaga' in peticion) and 'ftp' in peticion:
            oo.ftpdown()
            print ("Apago server de FTP")
            habla ("Apago server de FTP")

            #SSH

       if ('levanta' in peticion or 'sube' in peticion or 'enciende' in peticion) and 'ssh' in peticion:
            print ("Levanto server de SSH")
            habla ("Levanto server de SSH")
            oo.sshup()
       if ('tira' in peticion or 'apaga' in peticion) and 'ssh' in peticion:
            oo.sshdown()
            print ("Apago server de SSH")
            habla ("Apago server de SSH")

       if 'salir' in peticion or 'adiós' in peticion:
           habla ("Hasta luego")
           break

