import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI
recognizer = sr. Recognizer()
engine = pyttsx3.init()
newsapi="9f2a003bd14f4e5f8841e583604b8c5f"


# def processcommand():


def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiprocess(command):
    client = OpenAI(
    api_key="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",)
    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a Virtual  assistant names jarvis skilled in general task like alexa and Google cloud"},
        {
            "role": "user",
            "content": command
        }
    ]
)

    return completion.choices[0].message.content


def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    
    elif "news" in c.lower():
        r = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            data = r. jason()

            articles = data.get('articles', [])

            for article in articles:
                speak(article['title'])
    else:
        #let open ai handle the situation
        output = aiprocess(c)
        speak(output)
        pass




if __name__ == "__main__" :
    speak("Initializing jarvis....")
    while True:    
        r = sr.Recognizer()
        print("Recognizing...")
        

    # recognize speech using Sphinx
        try:
            with sr.Microphone() as source:
                print("Listening>>")
                audio = r.listen(source,timeout=2,phrase_time_limit=1)

            word = r.recognize_google(audio)
            if(word.lower() == "jarvis" ):
                speak("Ya Farhan")

                #listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processcommand(command)

        except Exception as e:
            print("Error; {0}".format(e))

