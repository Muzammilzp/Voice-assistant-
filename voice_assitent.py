import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I did not understand that.")
        return ""
    except sr.RequestError:
        speak("Speech service is unavailable.")
        return ""

def tell_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%I:%M %p")
    speak(f"The current time is {current_time}")

def tell_date():
    today = datetime.datetime.now()
    current_date = today.strftime("%B %d, %Y")
    speak(f"Today's date is {current_date}")

def search_web(query):
    speak(f"Searching for {query}")
    webbrowser.open(f"https://www.google.com/search?q={query}")

def main():
    speak("Voice assistant started. How can I help you?")

    while True:
        command = listen()

        if "hello" in command:
            speak("Hello! How can I assist you today?")

        elif "time" in command:
            tell_time()

        elif "date" in command:
            tell_date()

        elif "search" in command:
            speak("What should I search for?")
            query = listen()
            if query:
                search_web(query)

        elif "exit" in command or "stop" in command:
            speak("Goodbye!")
            break

if __name__ == "__main__":
    main()
