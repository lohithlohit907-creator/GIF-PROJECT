import os
from speak import speak

os.makedirs("memory", exist_ok=True)

def handle_memory_commands(command):

    if "take note" in command:

        speak("What should I write?")

        note = input("Enter note: ")

        with open("memory/notes.txt", "a") as file:

            file.write(note + "\n")

        speak("Note saved")

        return True


    elif "show notes" in command:

        with open("memory/notes.txt", "r") as file:

            notes = file.read()

        print(notes)

        speak("Here are your notes")

        return True


    elif "remember" in command:

        memory = command.replace("remember", "")

        with open("memory/memory.txt", "a") as file:

            file.write(memory + "\n")

        speak("I will remember that")

        return True


    elif "what do you remember" in command:

        with open("memory/memory.txt", "r") as file:

            memories = file.read()

        print(memories)

        speak("Here is what I remember")

        return True


    return False