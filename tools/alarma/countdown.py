import time, subprocess

timeLeft = 5
while timeLeft > 0:
    print(timeLeft, end=' ', flush=True)
    time.sleep(1)
    timeLeft -= 1

# Windows
subprocess.Popen(['start', 'alarm.wav'], shell=True)

# Mac
#subprocess.Popen(['start', 'alarm.wav'])

# Linux
#subprocess.Popen(['xdg-open', 'alarm.wav'], shell=True)
