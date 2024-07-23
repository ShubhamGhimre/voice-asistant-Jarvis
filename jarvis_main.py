import pyttsx3
import speech_recognition 

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
            
                
                elif "hello" in query:
                    speak("Hello sir, how are you ?")
                
                elif "i am fine" in query:
                    speak("That's great sir")
                
                elif "how are you " in query:
                    speak("Perfect sir")  
                
                elif "thank you" in query:
                    speak("You're welcome sir")  
                  
                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                    
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)
                
        
        
