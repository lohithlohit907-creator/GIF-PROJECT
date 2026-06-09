import webbrowser
import datetime

from speak import speak


def run_command(command):

    if "youtube" in command:

        speak("Opening YouTube")

        webbrowser.open("https://youtube.com")


    elif "google" in command:

        speak("Opening Google")

        webbrowser.open("https://google.com")


    elif "time" in command:

        current_time = datetime.datetime.now().strftime("%I:%M %p")

        speak(f"The time is {current_time}")


    elif "date" in command:

        current_date = datetime.datetime.now().strftime("%d %B %Y")

        speak(f"Today's date is {current_date}")