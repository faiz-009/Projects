import pyttsx3
import datetime
import speech_recognition as sr

engine = pyttsx3.init()
voices = engine.getProperty('voices')
# print(voices[0].id)
# print(voices[1].id)
# print(voices[2].id)
# print(voices[3].id)
# print(voices[4].id)
# print(voices[5].id)

engine.setProperty('voice', voices[4].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12 :
        speak("Good Morning Faaiz, I am Alexa. ")
    elif hour >=12 and hour<16:
        speak("Good afternoon Faaiz, I am Alexa. ")
    else:
        speak("Good evening sir, I am Jarvis. ")
    
def intro():
    intro = 'My name is Jarvis. I am an artificial intelligence, developed by  Mohammad Faaiz .'
    speak(intro)

def exit():
    speak("Thank you sir, have a good day")

def runAlexa():
    
    speak("How can I help you ?")
    command = takeCommand()

    if 'youtube'.lower() in command:
        #youTube()
        pass
    elif 'who are you' in command:
        intro()
    elif 'go' in command:
        exit()
        return -1

    

def takeCommand():
    '''It takes audio input from and returns string output'''

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        #r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        #print(e)
        print("Say that again please....")
        return "None"
    return query
        

if __name__ == '__main__':
    #code
    print("Speeking.....")
    wishMe()
    while 1:
        a = runAlexa()
        if a==-1:
            break