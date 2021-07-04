#Importing Libraries
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import requests, json , sys
#PyAudio
#PyWhatKit
#PyJokes
#Wikipedia
#OpenweatherApi

listener = sr.Recognizer()

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[1].id)

def engine_talk(text):
    engine.say(text)
    engine.runAndWait()
    


def user_commands():
    try:
        with sr.Microphone() as source:
            print("Start Speaking!!")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'pooh' in command:
                command = command.replace('pooh', '')
                print(command)
    except:
        pass
    return command
    
    
def run_alexa():
    command = user_commands()
    if 'what is today' in command:
        today = "oops sorry Today is pooh's Birthday"
        print('New Command is - ' +command)
        engine_talk(today)
    if 'do you know me' in command:
        intro = "yes i know you very well. You are the most talented and cute girl out there of B I T 2016. Currently you are developing lots of stress, oh sorry i mean lot of app"
        print('New Command is - ' +command)
        engine_talk(intro)
    if 'who told you i am developing stress' in command:
        stress = "Disclosing this can lead to destruction of someone i have crush upon. Please dont ask this question again else i have to answer"
        print('New Command is - ' +command)
        engine_talk(stress)    
    if 'play' in command:
        song = command.replace('play', '')
        #print('New Command is' +command)
        #print('The bot is telling us: Playing' +command)
        engine_talk('Playing' +song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        engine_talk('The current time is' +time)
    # elif 'who is' in command:
    #     name = command.replace('who is' , '')
    #     info =  wikipedia.summary(name, 1)
    #     print(info)
    #     engine_talk(info)
    elif 'pooh crack a joke for' in command:
        engine_talk(pyjokes.get_joke())
    # elif 'weather' in command:
    #     engine_talk('Please tell the name of the city')
    #     city = user_commands()
    #     #weather_api = weather('Hong Kong')
    #     weather_api = weather(city)
    #     engine_talk(weather_api + 'degree fahreneit' )
    elif 'stop' in command:
        engine_talk("why are you stopping me, dont you love me dear. ")
        sys.exit()
    else:
        engine_talk('Hey pooh,Would you please repeat ................please.... please...please!')
        
        
while True:
    run_alexa()