import time
import pygame

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("./alarm/alarm.mp3")

myTime = int(input("Enter the time in seconds: "))

for x in reversed(range(0, myTime)):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours}:{minutes}:{seconds:02}")
    time.sleep(1)

pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
