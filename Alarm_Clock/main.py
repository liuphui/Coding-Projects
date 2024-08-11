import time
import datetime
import pygame
import os

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}.")
    script_dir = os.path.dirname(os.path.abspath(__file__))
    sound_file = os.path.join(script_dir, "Take Me Back.mp3")
    
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        
        if current_time == alarm_time:
            print("Wake Up!")
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
            
            while pygame.mixer.music.get_busy():
                time.sleep(1)
                user_input = input("Type \'ok\' to stop: ")
                if user_input.lower() == 'ok':
                    break
                
            break
        time.sleep(1)
        
def check_valid_time(t):
    t_string = t.split(":")
    
    if len(t_string) != 3:
        return False
    
    hours = int(t_string[0])
    minutes = int(t_string[1])
    seconds = int(t_string[2])
    
    if 0 <= hours <= 23:
        if 0 <= minutes <= 59:
            if 0 <= seconds <= 59:
                return True
    return False
    

def main():
    alarm_time = ""
    while not check_valid_time(alarm_time):
        alarm_time = input("Enter the alarm (HH:MM:SS): ")
        
        if not check_valid_time(alarm_time):
            print("Invalid time. Please press a valid time in the specified format.")
        
    set_alarm(alarm_time)
    
if __name__ == "__main__":
    main()