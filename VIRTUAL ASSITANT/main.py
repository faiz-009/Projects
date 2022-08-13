#Author:- MOHD. FAIZ QURESHI

import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import smtplib
import os
from email import message
from http import server
from importlib.resources import path
from random import seed
from time import time
from unicodedata import name
from winreg import QueryInfoKey



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
        speak("Good Morning sir, I am jarvis.  ")
    elif hour >= 12 and hour < 16:
        speak("Good afternoon sir, I am jarvis.  ")
    else:
        speak("Good evening sir, I am jarvis. ")



#2. intro function will give intro of VA
def intro():
    intro = 'My name is jarvis. I am a virtual assistant, developed by  Mohammad Faaiz .'
    speak(intro)



#3. open something on browser
def open(query):
    try:
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
        if 'vs code' in query:
            filePath = "C:\\Users\\malik\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak('Opening vs code....')
            os.startfile(filePath)
    except:
        speak("Sorry sir, your request can not be fulfilled by me.")
    



#4. Return time or date
def timeAndDate():
    
    try:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak("Sir, The time now is : ")
        speak(strTime)
    except:
        speak("Sorry sir, your request can not be fulfilled by me.")
    


#6. e-mail to a recipent
def email(query):
    
    contacts = {' faiz':'mdfaizqureshi09@gmail.com',
                ' mayur': 'en19cs301197@medicaps.ac.in',
               }
    try:
        if 'send email to' in query:
            print(query)
            query = query.replace('send email to ','')
            print(query)
            if query in contacts:
                to = contacts[query]
                speak('Sir what message should I write in the email ?')
                message = takeCommand()
                server = smtplib.SMTP('smtp.gmail.com',587)
                server.ehlo()
                server.starttls()
                server.login('malikjannat007@gmail.com', 'Faiz54321#')
                server.sendmail('malikjannat007@gmail.com',to, message)
                server.close()
                
            else:
                speak('sir, abc is not in your contact list.')
        else:
            speak('Sir, if you want me to send an email to someone, please give the command as : Jarvis, send email to x.')
        
    except:
        speak("Sorry sir, your request can not be fulfilled by me.")



#7. search something on wikipedia
def wiki(query):
    try:
        speak('Searching wikipedia.......')
        query = query.replace('wikipedia', '')
        results = wikipedia.summary(query, sentences=4)
        speak('According to wikipedia, ')
        speak(results)
    except:
        speak("Sorry sir, your request can not be fulfilled by me.")
    


#exit function will exit our program
def exit():
    speak("Thank you sir, have a good day")



#run function will make our program to run
def run():
    speak("How can I help you sir?")
    command = takeCommand().lower()
    if 'jarvis' in command:
        command = command.replace('jarvis', '')
            
        if 'who are you' in command:
            intro()
        elif 'exit' in command:
            exit()
            return -1
        elif 'wikipedia' in command:
            wiki(command)
        elif 'open' in command:
            open(command)
        elif 'time' in command:
            timeAndDate()
        elif 'email' in command:
            email(command)
    
    else:
        speak("Sir, you need to say my name while giving commands.")
        takeCommand()



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
