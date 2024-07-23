import pyttsx3
import speech_recognition 
import requests
import datetime
from bs4 import BeautifulSoup

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
                   
                #exit automations
                elif "sleep jarvis" in query:
                    speak("Ok sir, closing the program now")
                    exit()
 
                elif "finally sleep" in query:
                    speak("Going to sleep sir!")
                    exit()
                    
                    
                                  
                
        
        
