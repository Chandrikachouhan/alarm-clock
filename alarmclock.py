import datetime
import time
import winsound #for sound
def alarm_c( ):
    alarmtime=input("entre alarm time (HH:MM:SS AM/PM) EXAMPLE=08:45:00 AM :")
    hour=alarmtime[0:2]
    min=alarmtime[3:5]
    sec=alarmtime[6:8]
    period=alarmtime[9:12].upper()
    print(f"alarm time {alarmtime}")
    while True:
        now=datetime.datetime.now()
        currenthour=now.strftime("%I")
        currentmin=now.strftime("%M")
        currentsec=now.strftime("%S")
        currentper=now.strftime("%p")
        if hour==currenthour and min==currentmin  and period==currentper:
            print("time to take a break!")
            for i in range(5): #beep 5 times
                winsound.Beep(1000,1000)#frequency 1000Hz ,1 second
            break

        time.sleep(1)
alarm_c( )
