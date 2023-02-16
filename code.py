from time import strftime
import speech_recognition as sr
import pyttsx3 
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener =sr.Recognizer()
engine= pyttsx3.init()
voices= engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say('i am your assistant')
engine.say('how may i help you')
engine.runAndWait()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
  try:
    with sr.Microphone() as source:
        print('listening...')
        voice= listener.listen(source)
        command=listener.recognize_google(voice)
        command=command.lower()
        if 'alexa' in command:
         command=command.replace('alexa','')
        print(command)
    
  except:
   pass  
  return command     


def run_alexa():
    command=take_command()
    
    if 'play' in command:
        song=command.replace('play', '')
        talk('playing'+ song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time=datetime.datetime.now().strftime('%H:%M')
        print(time)
        talk('curremt time is'+time)

    elif 'who is' in command:
        command=command.replace('who is','')
        info= wikipedia.summary(command,2)
        print(info)
        talk(info)

    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'stop' in command:
        quit()

    else:
        talk('please say the command again')

while True:        
  run_alexa()
