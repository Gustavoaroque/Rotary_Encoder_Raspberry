from rotary_encoder import *
from datetime import datetime
from time import sleep
import drivers
from date_transform import *

import RPi.GPIO as GPIO


display = drivers.Lcd()

minutes = 0
def init():
    display.lcd_clear()
    display.lcd_display_string("Welcome",1)
    sleep(3)
    display.lcd_clear()
    
def Date_print():
    
    display.lcd_display_string("The time is: ",1)
    current_time = str(datetime.today().hour) +":"+ str(datetime.today().minute)
    current_time = current_time.center(16," ")
    display.lcd_display_string(current_time,2)
  
def set_time_by_encoder():
    
    display.lcd_display_string("Select the time",1)
    sleep(1)

    minutes = set_encoder()
    display.lcd_clear()
    
    minutes_str = "in " + str(minutes) + " minutes"
    
    display.lcd_display_string("Alarm will sound",1)
    display.lcd_display_string(minutes_str, 2)
    
    time_list_data = set_timer(minutes)
    
    sleep(3)
    display.lcd_clear()
    
    countdown(time_list_data[0],time_list_data[1])
    
    
    


    

def main():
    boolean_pom = False
    init()
    pom_min = 0
    while True:
        Date_print()
        if GPIO.input(25) == 0:
            display.lcd_clear()
            set_time_by_encoder()
            sleep(0.5)
        
            
def countdown(h,m):
    print(h)
    print(m)
    while True:
        display.lcd_backlight(0)
        if h == datetime.today().hour:
            if m == datetime.today().minute:
                display.lcd_backlight(0)
                display.lcd_clear()
                display.lcd_display_string("Pomodoro \nFinished",1)
                sleep(5)
                break
        
        
        
       
        
main()
