import speech_recognition as sr
import pyttsx3
import webbrowser
import music_library
import requests

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsApi = "4229796f2163449a8a550b49be50d9c9"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    
    elif c.lower().starswith("play"):
        song = c.lower().split(" ")[1]
        link = music_library.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsApi}")
        if r.status_code == 200:
            data = r.json()

            articles = data.get("article", [])

            for article in articles:
                speak (article["title"])

    else:
        pass


if __name__ == "__main__":
    speak("Initializing Jarvis...")

while True:
    r = sr.Recognizer()

    print("Recognizing...")
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source, timeout=5, phrase_time_limit=10)
            word = r.recognize_google(audio)
        if (word.lower() == "jarvis"):
            speak("Ya")

            with sr.Microphone() as source:
                print("Jarvis Active...")
                audio = r.listen(source)
                command = r.recognize_sphinx(audio)

            processCommand(command)
    
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    
    except Exception as e:
        print("Something went wrong!")

