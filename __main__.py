from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import datetime
import sys
import os

def main():
  time, message = set_time()
  pygame.mixer.init()
  pygame.mixer.music.load("alarm.wav")

  while True:
    if (time == datetime.datetime.now().strftime("%H:%M")):
      if (message != ""):
        print(message)
      pygame.mixer.music.play()
      os.system('pause')
      pygame.mixer.music.stop()
      break

def set_time():
  time = ""
  message = ""
  try_arg_time = True
  while True:
    if (len(sys.argv) < 2 or try_arg_time == False):
      time = input("Enter time: ")
      message = input("Enter message: ")
      if (time == "exit" or time == "quit" or time == "q"):
        sys.exit(0)
    else:
      time = sys.argv[1]
    if (len(sys.argv) > 2):
      message = " ".join(sys.argv[2:])
      try_arg_time = False
    time = time.replace(".", ":")
    try:
      time = datetime.datetime.strptime(time, "%H:%M").strftime("%H:%M")
      break
    except Exception:
      print(f"Invalid time {time}")
  os.system('cls' if os.name == 'nt' else 'clear')
  if (message != ""):
    print(f"Set alarm for {time} with message: {message}")
  else:
    print(f"Set alarm for {time}")
  print("Do not close this window")
  print("Press Ctrl+C to exit")
  return time, message

if __name__ == "__main__":
  main()



