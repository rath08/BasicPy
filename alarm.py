import datetime
from playsound import playsound

alarmHour = int(input("enter hour : "))
alarmMin = int(input("enter min : "))
alarmAM_PM = input("enter am or pm : ")

if alarmAM_PM == "pm":
    alarmHour += 12

while True:
    if (
        alarmHour == datetime.datetime.now().hour
        and alarmMin == datetime.datetime.now().minute
    ):
        print("playing....")
        playsound("punky.mp3")
        break
