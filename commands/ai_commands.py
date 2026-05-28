from speak import speak


def handle_ai_commands(command):

    if "python" in command:

        answer = "Python is a programming language"

    elif "your name" in command:

        answer = "I am Jarvis"

    else:

        answer = "I am still learning"

    print(answer)

    speak(answer)

    return True
