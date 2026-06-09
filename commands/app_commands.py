import os
from speak import speak

def handle_app_commands(command):

    if "notepad" in command:

        speak("opening notepad")

        os.system("notepad")

        return True
    
    return False