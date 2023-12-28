import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import smtplib
import pyaudio
import os
from tkinter import *
from tkinter import ttk
from ttkthemes import themed_tk as tk
from translate import Translator
import pyjokes
import pyautogui
import sys
import cv2
engine = pyttsx3.init('sapi5')


T=Translator(
from_lang = "English", to_lang = "Hindi"
)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def screenshot():
    pic=pyautogui.screenshot()
    pic.save('C:/Users/shaki/OneDrive/Desktop/Bca Final Project/screenshot.png')

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 6:
        speak("Hey Owl")

    elif hour >= 6 and hour < 12:
        speak("Good Morning")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")

    else:
        speak("Hello There!")

    speak("I'm osky")
    speak("Please tell me how may i help you ?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Say that again please.....")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('shakiprya@gmail.com', 'Ksapksap@123')
    server.sendmail('shakiprya@gmail.co', to, content)
    server.close()

def stop_voice_assistant():
    speak("Stop voice assistant.")
    sys.exit()

def joke():
    speak(pyjokes.get_jokes(language='en',category='all'))

def open_camera():
    cap = cv2.VideoCapture(0)
    speak("Opening laptop camera. Say 'stop camera' to close the camera.")
    
    while True:
        ret, frame = cap.read()
        cv2.imshow('Camera Feed', frame)
        
        key = cv2.waitKey(1)
        if key == ord('q') or 'stop camera' in takeCommand().lower():
            break

    cap.release()
    cv2.destroyAllWindows()
    speak("Closing laptop camera.")


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak('According to wikipedia')
            speak(results)
            print(results)

        elif 'open college website' in query:
            webbrowser.open("https://sawcollege.com/index.php")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open Linkedin' in query:
            webbrowser.open("Linkedin.com")

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")

        elif 'open dashboard' in query:
            webbrowser.open("http://mydy.dypatil.edu/rait/my/")

        elif 'open whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H,%M,%S")
            speak(f"Hey there, the time is {strTime}")
        elif 'open camera' in query:
           open_camera()


        if 'email' in query:
            speak("Whom do you want to send the email to?")
            recipient_name = takeCommand().lower()
            speak(f"What is the email address of {recipient_name}?")
            recipient_email = takeCommand().lower()
            speak(f"What message do you want to send to {recipient_name}?")
            email_content = takeCommand()

            try:
                sendEmail(recipient_email, email_content)
                speak(f"Email has been sent to {recipient_name}!")
            except Exception as e:
                print(e)
                speak(f"Sorry, I am not able to send an email to {recipient_name}")

        elif 'shutdown' in query:
            print("shutting down...")
            speak("shutting down")
            quit()

        elif 'translate' in query:
            query = query.replace('translate', '')
            translation = T.translate(query)
            speak(translation)
            print(translation)
            speak(translation)

        elif 'joke' in query:
            joke()

        elif 'screenshot' in query:
            screenshot()

        elif 'search youtube' in query:
          speak("What do you need to search on YouTube?")
          search_query = takeCommand().lower()
          speak('Here are the search results on YouTube.')
          webbrowser.open('https://www.youtube.com/results?search_query=' + search_query)

        elif 'search google' in query:
          speak("What do you need to search on Google?")
          search_query = takeCommand().lower()
          speak('Here are the search results on Google.')
          webbrowser.open('https://www.google.com/search?q=' + search_query)

        if 'stop' in query or 'exit' in query or 'quit' in query:
          stop_voice_assistant()
    

main()

root_1 = tk.ThemedTk()
root_1.set_theme('radiance')
root_1.title("Voice assistant")
root_1.geometry("400x350")
lbl1=ttk.Label(master=root_1, text="Welcome to voice assistant app\n\n", wraplength=600)
lbl1.pack()
but1 = ttk.Button(root_1, text="Run the assistant🤖🔊", command=main)
but1.config(width=22)
but1.pack(padx=10, pady=10)
quit4 = ttk.Button(root_1, text="EXIT", command=root_1.destroy)
quit4.config(width=22)
quit4.pack(padx=10, pady=20)
root_1.mainloop()
