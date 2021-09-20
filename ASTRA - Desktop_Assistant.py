import pyttsx3
#pyttsx3 is a text-to-speech conversion library in Python.
import datetime
#The datetime module supplies classes for manipulating dates and times.
import speech_recognition as sr
#Speech recognition helps us to save time by speaking instead of typing
import pyaudio
#PyAudio is required when you want to use microphone input.
import wikipedia

import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishuser():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good morning")
    elif hour >= 12 and hour < 18:
        speak("good afternoon")
    else:
        speak("good evening")

def takecommand():
    recognize = sr.Recognizer()
    with sr.Microphone() as source:
        print("LISTENING.............")
        recognize.pause_threshold = 1
        audio = recognize.listen(source)

    try:
        print("RECOGNIZING...........")
        command = recognize.recognize_google(audio, language ='en-in')
        print(f"You said : {command}\n")


    except Exception as e:
        speak("Say that again please")
        return"None"
    return command


if __name__ == "__main__":
    wishuser()
    speak("i am astra, how may i help you")
    while True:
        command = takecommand().lower()

        if "wikipedia" in command:
            try: 
                speak("Searching wikipedia...")
                command = command.replace("wikipedia", "")
                result = wikipedia.summary(command, sentences = 1)
                print(result)
                speak(result)
            except Exception as e:
                speak("try something different")

        elif "search" in command:
            command = command.replace("search", "")
            webbrowser.open(f"www.bing.com/search?q={command}")

        elif "youtube" in command:
            webbrowser.open("youtube.com")

        elif "stack overflow" in command:
            webbrowser.open("stackoverflow.com")

        elif "time" in command:
            cur_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak("the time is")
            speak(cur_time)

        elif "open google" in command:
            webbrowser.open("google.com")


        elif "set alarm" in command:
            speak("please enter the time in the below format")
            alarm_time = input("Enter the time of alarm to be set in HH:MM:SS format \n")
            alarm_hour=alarm_time[0:2]
            alarm_minute=alarm_time[3:5]
            alarm_seconds=alarm_time[6:8]

            speak("Setting up alarm..")
            try:
                while True:
                    now = datetime.now()
                    current_hour = now.strftime("%I")
                    current_minute = now.strftime("%M")
                    current_seconds = now.strftime("%S")
                    if(alarm_hour==current_hour):
                          if(alarm_minute==current_minute):
                                if(alarm_seconds==current_seconds):
                                    speak("WAKE UP")
                                    speak("it is time to wake up")
                    
                                    break
            except Exception as e:
                speak("try again with correct format")