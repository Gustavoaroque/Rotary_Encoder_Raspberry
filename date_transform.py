from datetime import datetime
from time import sleep

def set_timer(min_input):
    #va a pedir minutos
    #se le va a sumar a la hora actual y que mantenga el formato de hh:mm
    time_list = []
    print("The time is:")
    current_hour = datetime.today().hour
    current_minute = datetime.today().minute
    
    current_time = str(current_hour) +":"+ str(current_minute)
    
    print(current_time)
    #print("Enter the minutes you want to rest/n")
    #minutes_enter = input()
    if int(min_input) >59 or int(min_input) < 0:
        print("Error")
        
    else:
        print("-----------------------------------------")
        print("You want to rest ")
        print(str(min_input))
        print("-----------------------------------------")
        new_alarm_min = current_minute + int(min_input)
    
        print(str(new_alarm_min))
    
    
        if new_alarm_min > 59:
        #Necesito obtener residuo y resultado
            
            factor = new_alarm_min/60
            modulo = new_alarm_min%60
             
            factor_int = int(factor)
            
            
            print("Factor:")
            print(str(factor))
            
            print("Factor int:")
            print(str(factor_int))
        
            print("Modulo:")
            print(str(modulo))
            
            print("-----------------------------------------")
            print("-----------------------------------------")
            
            new_min = modulo
            new_hour = factor_int + current_hour
            
            if new_hour > 23:
                new_hour = new_hour - 24
            
            
            alarm_set_to = str(new_hour) +":"+str(new_min)

            
            
            #print(alarm_set_to)
        else:
            new_min = new_alarm_min
            new_hour = current_hour
            
            alarm_set_to = str(new_hour) +":" +str(new_min)
            print(alarm_set_to)
        
        
        time_list.append(new_hour)
        time_list.append(new_min)
            
        print(time_list)
        return time_list
        