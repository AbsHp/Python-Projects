from datetime import datetime
from playsound import playsound

alarm_time = input("Enter time in 'HH:MM:SS AM/PM' format: ")

def validate_time(alarm_time):
    if len(alarm_time) != 11:
        return "Invalid time format! Please try again..."
    else:
        if int(alarm_time[0:2]) > 12:
            return "Invalid HOUR format! Please try again"
        elif int(alarm_time[3:5]) > 59:
            return "Invalid MINUTE format! Please try again"
        elif int(alarm_time[6:8]) > 59:
            return "Invalid SECOND format! Please try again"
        else:
            return "ok"

print("Alarm Set!")

while True:

    alarm_hour = alarm_time[0:2]
    alarm_min = alarm_time[3:5]
    alarm_sec = alarm_time[6:8]
    alarm_period = alarm_time[9:].upper()

    now = datetime.now()

    current_hour = now.strftime("%I")
    current_min = now.strftime("%M")
    current_sec = now.strftime("%S")
    current_period = now.strftime("%p")

    if(alarm_period == current_period and alarm_hour == current_hour and alarm_min == current_min and alarm_sec == current_sec):
        print("Wake Up!")
        playsound("E:\H Drive (Re-Creational and Extras)\Programming and related\Python-Projects\Alec Benjamin - Let me down slowly ( lyrics ). (320 kbps).wav")
        break