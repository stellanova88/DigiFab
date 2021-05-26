import time
from machine import Pin
from rotary_irq_pico import RotaryIRQ

r1 = RotaryIRQ(pin_num_clk=0, 
              pin_num_dt=1, 
              min_val=0, 
              max_val=100, 
              reverse=False, 
              range_mode=RotaryIRQ.RANGE_WRAP,
              pull_up=True)

r2 = RotaryIRQ(pin_num_clk=2, 
              pin_num_dt=3, 
              min_val=0, 
              max_val=100, 
              reverse=False, 
              range_mode=RotaryIRQ.RANGE_WRAP,
              pull_up=True)

r3 = RotaryIRQ(pin_num_clk=6, 
              pin_num_dt=7, 
              min_val=0, 
              max_val=100, 
              reverse=False, 
              range_mode=RotaryIRQ.RANGE_WRAP,
              pull_up=True)

r4 = RotaryIRQ(pin_num_clk=8, 
              pin_num_dt=9, 
              min_val=0, 
              max_val=100, 
              reverse=False, 
              range_mode=RotaryIRQ.RANGE_WRAP,
              pull_up=True)
              
rb4 = Pin(10, Pin.IN, Pin.PULL_UP)
rb1 = Pin(11, Pin.IN, Pin.PULL_UP)
rb2 = Pin(12, Pin.IN, Pin.PULL_UP)
rb3 = Pin(13, Pin.IN, Pin.PULL_UP)

b4 = Pin(14, Pin.IN, Pin.PULL_UP)
b5 = Pin(15, Pin.IN, Pin.PULL_UP)
b6 = Pin(17, Pin.IN, Pin.PULL_UP)
b7 = Pin(20, Pin.IN, Pin.PULL_UP)
b1 = Pin(21, Pin.IN, Pin.PULL_UP)
b2 = Pin(22, Pin.IN, Pin.PULL_UP)
b3 = Pin(26, Pin.IN, Pin.PULL_UP)

print('ready to roll')  
  
val_old1 = r1.value()
val_old2 = r2.value()
val_old3 = r3.value()
val_old4 = r4.value()

while True:
    val_new1 = r1.value()
    val_new2 = r2.value()
    val_new3 = r3.value()
    val_new4 = r4.value()
    
    if val_old1 != val_new1:
        val_old1 = val_new1
        print('RotEnc 1 =', val_new1)
        
    if val_old2 != val_new2:
        val_old2 = val_new2
        print('RotEnc 2 =', val_new2)
        
    if val_old3 != val_new3:
        val_old3 = val_new3
        print('RotEnc 3 =', val_new3)
        
    if val_old4 != val_new4:
        val_old4 = val_new4
        print('RotEnc 4 =', val_new4)
        
    if rb1.value() ==0:
        print("Rotary Button 1 is pressed")
        
    if rb2.value() ==0:
        print("Rotary Button 2 is pressed")
        
    if rb3.value() ==0:
        print("Rotary Button 3 is pressed")
        
    if rb4.value() ==0:
        print("Rotary Button 4 is pressed")
    
    #Button
    if b1.value() ==0:
        print("Button 1 is pressed")
        
    if b2.value() ==0:
        print("Button 2 is pressed")
    
    if b3.value() ==0:
        print("Button 3 is pressed")
    
    if b4.value() ==0:
        print("Button 4 is pressed")
    
    if b5.value() ==0:
        print("Button 5 is pressed")
    
    if b6.value() ==0:
        print("Button 6 is pressed")
    
    if b7.value() ==0:
        print("Button 7 is pressed")
    
        
    time.sleep_ms(30)
    

