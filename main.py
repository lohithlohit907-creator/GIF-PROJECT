from speak import speak
from listen import listen

from commands.web_commands import handle_web_commands
from commands.time_commands import handle_time_commands
from commands.app_commands import handle_app_commands
# from commands.ai_commands import handle_ai_commands
from commands.memory_commands import handle_memory_commands

speak("Jarvis Activated")


while True:

    command = listen()


    if "exit" in command:

        speak("Goodbye")

        break


    handled = False


    handled = handle_web_commands(command)

    if not handled:

        handled = handle_time_commands(command)


    if not handled:

        handled = handle_app_commands(command)

    # if not handled:

    #     handled=handle_ai_commands(command)

    if not handled:

        handled=handle_memory_commands(command)    

    if not handled:

        speak("Sorry, I don't know that command")    

