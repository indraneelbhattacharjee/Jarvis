import keyword
from pyautogui import KEYBOARD_KEYS
import pyttsx3
from datetime import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import wnapps_path as wap
from Py_Weather import get_weather
import requests
from bs4 import BeautifulSoup
    
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()

def get_weather(place):
    url = 'https://www.google.com/search?&q=weather in ' + place
    req = requests.get(url)
    scrap = BeautifulSoup(req.text, 'html.parser')
    tmp = scrap.find("div", class_="BNeawe").text
    tm = scrap.find("div", class_="BNeawe tAd8D AP7Wnd").text
    tm = tm.replace('\n', ' ').split(' ')
    print('Date & Time is: ' + tm[0] + ' ' + tm[1] + ':' + str(tm[2]).upper())
    print('Weather is: ' + tm[3])
    print('Temperature is: '+tmp)
    speak('Date & Time is: ' + tm[0] + ' ' + tm[1] + ':' + str(tm[2]).upper())
    speak('Weather is: ' + tm[3])
    speak('Temperature is: '+tmp)

def greet():
    hour = int(datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning! ")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon! ")

    else:
        speak("Good Evening! ")
    
    speak("How may Jarvis assist you today your majesty ? ")

def command():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"You said: {query}\n")

    except Exception as e:
        #print(e)
        speak("Say that again please...")
        print("Say that again please...")
        return "None"
    return query

def send_email():
    speak("Who is the recipient? Please enter the email address.")
    recipient = input("Enter your email address : ")
    speak("What should be the subject of the email?")
    subject = input("Subject: ")
    speak("What should be the message body of the email?")
    body = input("Body: ")

    try:
     server = smtplib.SMTP('smtp.gmail.com', 587) or smtplib.SMTP('smtp-mail.outlook.com', 587)
     server.starttls()
     email = "enter your email address here"
     speak("Your email address is ") , speak(email)
     speak("I wont say your password, hahaha !! ")
     password = "rvqxdftaxorvnlse"
     server.login(email, password)
     message = f'Subject: {subject}\n\n{body}'
     server.sendmail(email, recipient, message)
     speak("Email has been sent successfully.")
     server.quit()
    except Exception as e:
        speak("Sorry, I am unable to send the email at the moment. Please try again later.")
        print(e)


if __name__ == "__main__":
    weather = get_weather('Sacramento')
    speak(weather)
    greet()
    while True:
        query = command().lower()

        if 'email' in query:
            send_email()
        
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'spotify' in query:
            if os.path.exists(wap.spotify_path):
             os.startfile(wap.spotify_path)
            else:
                speak("Spotify is not installed on this machine.")
        
        elif 'open calculator' in query:
            app_path = wap.calculator
            try:
                os.startfile(app_path)
            except FileNotFoundError:
                speak("Sorry, I couldn't find the Calculator app on your computer.")
                print("Sorry, I couldn't find the Calculator app on your computer.")

        elif 'open notepad' in query:
            app_path = wap.notepad
            try:
                os.startfile(app_path)
            except FileNotFoundError:
                speak("Sorry, I couldn't find the Notepad app on your computer.")
                print("Sorry, I couldn't find the Notepad app on your computer.")

        elif 'open word' in query:
            app_path = wap.word
            try:
                os.startfile(app_path)
            except FileNotFoundError:
                speak("Sorry, I couldn't find the Word app on your computer.")
                print("Sorry, I couldn't find the Word app on your computer.")

        elif 'open excel' in query:
            app_path = wap.excel
            try:
                os.startfile(app_path)
            except FileNotFoundError:
                speak("Sorry, I couldn't find the Excel app on your computer.")
                print("Sorry, I couldn't find the Excel app on your computer.")
        
        elif 'whatsapp' in query:
            app_path = wap.whatsapp
            try:
                os.startfile(app_path)
            except FileNotFoundError:
                speak("Sorry, I couldn't find the WhatsApp app on your computer.")
                print("Sorry, I couldn't find the WhatsApp app on your computer.")


        elif 'open' in query :
            url = query.replace('open', '').strip()
            url = url.replace(' ', '+')
            url += '.com'
            webbrowser.open(url)

        elif 'exit' or 'thanks' or 'thank you' in query:
            speak("Goodbye!")
            exit()
