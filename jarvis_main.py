import pyttsx3
import speech_recognition 
import requests
import datetime
from bs4 import BeautifulSoup
import os
import pyautogui

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
# print(voices[0])
engine.setProperty("rate", 170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        
        audio = r.listen(source,0,4)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en")
        print(f"You said: {query}")
        # speak(f"You said: {query}")
        
    except Exception as e:
        # print(e)
        print("sorry sir, I didn't get it! can you please say that again ?")
        # speak("sorry sir, I didn't get it! can you please say that again ?")
        
        return "None"
    return query

def alarm(query):
    timehere = open("AlarmText.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")
    
if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()
            while True:
                query = takeCommand().lower()
                
                if "go to sleep" in query:
                    speak("Ok sir, you can call me anytime")
                    break
                   
                #greet automations 
                elif "hello" in query:
                    speak("Hello sir, how are you ?")
                
                elif "i am fine" in query:
                    speak("That's great sir")
                
                elif "how are you " in query:
                    speak("Perfect sir")  
                
                elif "thank you" in query:
                    speak("You're welcome sir") 
                    
                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")

                elif "volume up" in query:
                    from keyboard import volumeup
                    speak("Turning volume up,sir")
                    volumeup()
                elif "volume down" in query:
                    from keyboard import volumedown
                    speak("Turning volume down, sir")
                    volumedown()
                
                #open close automations
                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)
                     
                  
                #search automations
                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                    
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)
                    
                #temperature automations 
                elif "temperature" in query:
                    search = "temperature in kathmandu"   
                    url = f"https://www.google.com/search?q={search}" 
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_ ="BNeawe").text
                    speak(f"current {search} is {temp}")
                elif "weather" in query:
                    search = "weather in kathmandu"   
                    url = f"https://www.google.com/search?q={search}" 
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_ ="BNeawe").text
                    speak(f"current {search} is {temp}")
                    
                elif "the time" in query:
                    currentTime = datetime.datetime.now()
                    strTime = currentTime.strftime("%I %M:%p")
                    speak(f"Sir, the time is {strTime}")
                
                #alarm automations
                elif "set an alarm" in query:
                    print("Please tell me the time to set the alarm example : 10 and 10 and 10")
                    speak("set the time")
                    a = input("Enter the time :-  ")
                    alarm(a)
                    speak("Alarm set successfully")   
                  
                   
                #exit automations
                elif "sleep jarvis" in query:
                    speak("Ok sir, closing the program now")
                    exit()
 
                elif "finally sleep" in query:
                    speak("Going to sleep sir!")
                    exit()
                    
                elif "remember that" in query:
                    rememberMessage = query.replace("remember that"," ")
                    rememberMessage = query.replace("jarvis"," ")
                    speak("You asked me to "+rememberMessage)
                    # print(rememberMessage)
                    remember = open("Remember.txt","w")
                    remember.write(rememberMessage)
                    remember.close()
                elif "what do you remember " in query:
                    remember = open("Remember.txt","r")
                    # print(remember.read())
                    speak("You asked me to"+remember.read())
                
                    
                    
                    
                    
                                  
                
        
        
