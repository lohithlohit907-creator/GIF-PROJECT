import webbrowser
from speak import speak

def handle_web_commands(command):
    if "youtube" in command:

        speak("opening youtube")

        webbrowser.open("https://youtube.com")

    elif "google" in command:

        speak("opening gooogle ")   

        webbrowser.open("https://google.com")

        return True

    elif "chrome" in command:

        speak("opening chrome")   

        webbrowser.open("https://chrome.py")

        return True
    
    return False
