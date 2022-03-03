import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)

import drivers
CLK = 23
DT = 24
SW = 25

GPIO.setup(CLK,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(DT,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)


display = drivers.Lcd()
        
def set_encoder():
    
    pinCLK_last_state = GPIO.input(CLK)
    print("Iniciando")
    position = 0
    clockwise = True
    
    while True:
        current_value = GPIO.input(CLK)
        if current_value != pinCLK_last_state:
            if GPIO.input(DT) != current_value:
                position = position + 1
                clockwise = True
            else:
                clockwise = False
                position = position - 1
                
            if clockwise:
                print("Rotate ClockWise")
            else:
                print("Rotate CounterClockwise")
            print("Encoder Count: ")
            print(position)
            str_pos = str(position) + " Min"
            display.lcd_clear()
            display.lcd_display_string(str_pos,1)
            
        if GPIO.input(SW) == 0:
            print("Button Pressed")
            return position
        
        
            
            
        pinCLK_last_state = current_value
