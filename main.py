import pyttsx3  #text to speech 
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

MASTER = "Shubham"
engine = pyttsx3.init('sapi5')
voices =  engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

#Speak function will pronounce the string whatever it is passed
def speak(text):
    engine.say(text)
    engine.runAndWait()
# These function will wu=ish u as per the given time
def WishMe():
    hour =  int(datetime.datetime.now().hour)
    print(hour)

    if hour>= 0 and hour <12:
        speak("Good Morning"+ MASTER)
    elif hour >=12 and hour <18:
        speak("Good Afternoon" + MASTER)
    else:
        speak("Good Evening" + MASTER)
    speak("I am Jarvis. How may i help you ?")



# These function will take command from te microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source: 
        print("Listening...")
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language = "en-in")
        print(f"user said : {query}\n")
    except Exception as e:
        print("Say that again please..")
        query = None

    return query


def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('yourmailid@gmail.com','password')
    server.sendmail("shubham@gmail.com",to,content)

#main program start from here
def main():
    speak('Initializing Jarvis.....')
    WishMe()
    query =  takeCommand()

    #Logic for executing task as per the query
    if 'wikipedia' in query.lower():
        speak("Searching wikipidea...")
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query, sentences = 2)
        print(results)
        speak(results)
    elif 'open youtube' in query.lower():
        url = "youtube.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'play music' in query.lower():
        songs_dir = "D:\\songs\\songs1"
        songs = os.listdir(songs_dir)
        print(songs)
        os.startfile(os.path.join(songs_dir,songs[0]))

    elif 'the time' in query.lower():
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"{MASTER} the time is {strTime}")

    elif 'open visual studio code' in query.lower():
        codepath = "C:\\Users\\Shubham Buchunde\\AppData\Local\\Programs\\Microsoft VS Code\\code.exe"
        os.startfile(codepath)

    elif 'email to shubham' in query.lower():
        try:
            speak("What should i send..")
            content = takeCommand()
            to = "shubham@gmail.com"
            sendEmail(to,content)
            speak("Email has been sent successfully")
        except Exception as e:
            print(e)


main() 