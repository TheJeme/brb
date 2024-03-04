from os import environ, system, name
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import datetime
import sys

def main():
  pygame.mixer.init()
  pygame.mixer.music.load("alarm.wav")
  time, message = set_time()

  while datetime.datetime.now().strftime("%H:%M") != time:
    continue

  if message:
    print(message)
  pygame.mixer.music.play()
  system('pause')
  pygame.mixer.music.stop()

def set_time():
  time = sys.argv[1] if len(sys.argv) > 1 else input("Enter time: ")
  message = " ".join(sys.argv[2:]) if len(sys.argv) > 2 else "" if len(sys.argv) > 1 else input("Enter message: ")

  time = validate_time(time.replace(".", ":"))

  system('cls' if name == 'nt' else 'clear')
  print(f"Set alarm for {time}{' with message: ' + message if message else ''}")
  print("Do not close this window\nPress Ctrl+C to exit")
  return time, message

def validate_time(time):
  while True:
    try:
      return datetime.datetime.strptime(time, "%H:%M").strftime("%H:%M")
    except ValueError:
      print(f"Invalid time {time}")
      time = input("Enter time: ")

if __name__ == "__main__":
    main()