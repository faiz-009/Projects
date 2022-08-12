#Author:- MOHD. FAIZ QURESHI

from unittest import result
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser



#to select what voice VA will have
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[4].id)



#speak function to make our VA to speak what is passed to it
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()



#1. wish me function will wish the user according to time 
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning sir, I am Jarvis.  ")
    elif hour >= 12 and hour < 16:
        speak("Good afternoon sir, I am Jarvis.  ")
    else:
        speak("Good evening sir, I am Jarvis. ")



#2. intro function will give intro of VA
def intro():
    intro = 'My name is Jarvis. I am an artificial intelligence, developed by  Mohammad Faaiz .'
    speak(intro)



#3. open something on browser
def open(query):
    if 'google' in query:
        speak('Opening google....')
        webbrowser.open('google.com')
    if 'youtube' in query:
        speak('Opening youtube....')
        webbrowser.open('youtube.com')
    if 'spotify' in query:
        speak('Opening spotify....')
        webbrowser.open('spotify.com')
    if 'instagram' in query:
        speak('Opening instagram....')
        webbrowser.open('instagram.com')



#4. Return time or date
def timeAndDate():
    pass



#5. play on youtube
def youtube():
    pass



#6. e-mail to a recipent
def email():
    pass



#7. search something on wikipedia
def wiki(query):
    speak('Searching wikipedia.......')
    query = query.replace('wikipedia', '')
    results = wikipedia.summary(query, sentences=4)
    speak('According to wikipedia, ')
    speak(results)


#exit function will exit our program
def exit():
    speak("Thank you sir, have a good day")



#run function will make our program to run
def run():
    speak("How can I help you sir?")
    command = takeCommand().lower()
    if 'youtube' in command:
        # youTube()
        #speak('Youtube')
        pass
        
    elif 'who are you'  in command:
        intro()
    elif 'get lost'  in command:
        exit()
        return -1
    elif 'wikipedia' in command:
        wiki(command)
    elif 'open' in command:
        open(command)



#take command function will take audio commands from user
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.energy_threshold = 300
        r.pause_threshold = 0.8
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)
        speak("Say that again, please....")
        return "None"
    return query



#driver code
if __name__ == '__main__':
    print("Speaking.....")
    wishMe()
    while 1:
        a = run()
        if a == -1:
            break
