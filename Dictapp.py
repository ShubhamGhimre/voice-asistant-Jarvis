import os
import pyautogui
import webbrowser
import pyttsx3
from time import sleep

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
# print(voices[0])
engine.setProperty("rate", 170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
dictapp = {
    "command prompt": "cmd", "chrome": "chrome" , "spotify": "Spotify", "notepad": "notepad", "word": "WINWORD", "vscode": "code", "powerpoint": "powerpnt", "brave": "brave", "EpicGamesLauncher" : "EpicGamesLauncher", "edge": "msedge", "steam" : "steam"
}

def openappweb(query):
    speak("launching")
    if ".com" in query or "com.np" in query or ".org" in query or ".net" in query:
        query = query.replace("open", "")
        query = query.replace("jarvis", "")
        query = query.replace("launch", "")
        query = query.replace(" ", "") 
        
        
        webbrowser.open(f"https://www.{query}")
        
    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"start {dictapp[app]}.exe")
                
def closeappweb(query):
    speak("Terminating")
    
    if "one tab" in query or "1 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        
    elif "2 tab" in query or "two tab" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speak("all tabs closed, sir")
        
    elif "3 tab" in query or "three tab" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speak("all tabs closed, sir")
    elif "4 tab" in query or "four tab" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speak("all tabs closed, sir")
    elif "5 tab" in query or "five tab" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speak("all tabs closed, sir")
        
    else: 
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"taskkill /f /im {dictapp[app]}.exe")