import datetime

from speak import speak


def handle_time_commands(command):

    if "time" in command:

        current_time = datetime.datetime.now().strftime("%I:%M %p")

        speak(f"The time is {current_time}")

        return True


    elif "date" in command:

        current_date = datetime.datetime.now().strftime("%d %B %Y")

        speak(f"Today's date is {current_date}")

        return True


    return False