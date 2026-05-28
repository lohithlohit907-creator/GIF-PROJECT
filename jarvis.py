import pyttsx3
import speech_recognition as sr
import webbrowser


class Jarvis:

    def __init__(self):

        print("Jarvis Activated 😎")

        self.engine = pyttsx3.init()

        self.engine.setProperty("rate",150)

        voices = self.engine.getProperty("voices")

        self.engine.setProperty(
            "voice",
            voices[0].id
        )

    # -------- SPEAK --------

    def speak(self,text):

        print(f"Jarvis: {text}")

        self.engine.say(text)

        self.engine.runAndWait()

    # -------- LISTEN --------

    def listen(self):

        recognizer = sr.Recognizer()

        with sr.Microphone() as source:

            print("Listening...")

            audio = recognizer.listen(source)

            try:

                command = recognizer.recognize_google(audio)

                command = command.lower()

                print(f"You said: {command}")

                return command

            except:

                print("Sorry, I didn't understand")

                return ""

    # -------- COMMANDS --------

    def run_command(self, command):

        print(command)

        if not command:

            return

        if "chrome" in command:

            self.speak("Opening Chrome")

            webbrowser.open("https://google.com")

        elif "youtube" in command:

            self.speak("Opening YouTube")

            webbrowser.open("https://youtube.com")


# -------- OBJECT --------

ai = Jarvis()

command = ai.listen()

ai.run_command(command)