from multiprocessing.connection import Listener
import speech_recognition as sr
import pyttsx3
import pywhatkit
listener=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)
#make a function for talking
def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if "alexa"in command:
                command=command.replace("alexa"," ")
                print(command)
    except:
        pass
    return command
#make a function fo run
def run_alexa():
    command=take_command()
    print(command)
    if 'play'in command:
        song=command.replace("play","")
        talk("playing" +song)
        pywhatkit.playonyt(song)
    else:
        talk("please say the command again")
        
while True:
    run_alexa()

            
        