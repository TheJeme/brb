from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import datetime
import sys
import os

def main():
  time = set_time()
  pygame.mixer.init()
  pygame.mixer.music.load("alarm.wav")

  while True:
    if (time == datetime.datetime.now().strftime("%H:%M")):
      pygame.mixer.music.play()
      os.system('pause')
      pygame.mixer.music.stop()
      break

def set_time():
  time = ""
  try_arg_time = True
  while True:
    if (len(sys.argv) < 2 or try_arg_time == False):
      time = input("Enter time: ")
      if (time == "exit" or time == "quit" or time == "q"):
        sys.exit(0)
    else:
      time = sys.argv[1]
      try_arg_time = False
    time = time.replace(".", ":")
    try:
      time = datetime.datetime.strptime(time, "%H:%M").strftime("%H:%M")
      break
    except Exception:
      print(f"Invalid time {time}")
  print(f"Set alarm for {time}")
  return time

if __name__ == "__main__":
  main()



