import speech_recognition
import pyttsx3
import pywhatkit
import wikipedia
import webbrowser

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
    
def searchGoogle(query):
    if "google" in query:
        import wikipedia as googlescrap
        query = query.replace("jarvis", "")
        query = query.replace("google search", "")
        query = query.replace("google", "")
        speak("This is what I found on google")
        
        try:
            pywhatkit.search(query)
            result = googlescrap.summary(query, 1)
            speak(result)    
            
        except:
            speak("I am sorry, I didn't find anything on google")
            
def searchYoutube(query):
    if "youtube" in query:
        speak("searching on youtube ")
        query = query.replace("jarvis", "")
        query = query.replace("youtube search", "")
        query = query.replace("youtube", "")
        
        web = "https://www.youtube.com/results?search_query=" + query
        
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("done sir")

def searchWikipedia(query):
    if "wikipedia" in query:
        speak("searching from wikipedia")
        query = query.replace("jarvis", "")
        query = query.replace("wikipedia search", "")
        query = query.replace("wikipedia", "")
        
        results = wikipedia.summary(query, sentences=2)
        speak("According to wikipedia...")
        print(results)
        speak(results)