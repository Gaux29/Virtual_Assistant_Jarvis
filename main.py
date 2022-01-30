import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime

import wikipedia
# Initializing the listener
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Talk function for Jarvis to talk back
def talk(text):
    engine.say(text)
    engine.runAndWait()


# Taking the commamds from the user by listening
def takecommand():
    try:
        with sr.Microphone() as source:
            print('Listening....')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
                print(command)
    except:
        pass
    return command

# Running the following input
def run_jarvis():
    command = takecommand()
    if 'play' in command:
        print(command)
        song = command.replace('play', '')
        talk(f'Playing {song}')
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk(f'Current time is {time}')
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    else:
        talk('Please say it again ?')

# Running the while loop if the user not speaking then end the loop
while True:
    run_jarvis()
