from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)  

LED = LED(14)

win = Tk()
win.title("Blinking Morse code")
myFont = tkinter.font.Font(family = 'Times', size = 16, weight = 'bold')
var = IntVar()
Input = StringVar()
    
def BlinkingMorsecode():      
    v = var.get()
    value = Input.get()
    value.upper()
    if v == 1:
        for char in value:
            if (char == 'a'):
                dot()
                dash()
            
            elif (char == 'b'):
                dash()
                dot()
                dot()
                dot()
            
            elif (char == 'c'):
                dash()
                dot()
                dash()
                dot()
                
            elif (char == 'd'):
                dash()
                dot()
                dot()
                
            elif (char == 'e'):
                dot()
                
            elif (char == 'f'):
                dot()
                dot()
                dash()
                dot()
                
            elif (char == 'g'):
                dash()
                dash()
                dot()
                
            elif (char == 'h'):
                dot()
                dot()
                dot()
                dot()
                
            elif (char == 'i'):
                dot()
                dot()
                
            elif (char == 'j'):
                dot()
                dash()
                dash()
                dash()
                
            elif (char == 'k'):
                dash()
                dot()
                dash()
                
            elif (char == 'l'):
                dot()
                dash()
                dot()
                dot()
                
            elif (char == 'm'):
                dash()
                dash()
                
            elif (char == 'n'):
                dash()
                dot()
                
            elif (char == 'o'):
                dash()
                dash()
                dash()
                
            elif (char == 'p'):
                dot()
                dash()
                dash()
                dot()
                
            elif (char == 'q'):
                dash()
                dash()
                dot()
                dash()
                
            elif (char == 'r'):
                dot()
                dash()
                dot()
                
            elif (char == 's'):
                dot()
                dot()
                dot()
                
            elif (char == 't'):
                dash()
                
            elif (char == 'u'):
                dot()
                dot()
                dash()
                
            elif (char == 'v'):
                dot()
                dot()
                dot()
                dash()
            
            elif (char == 'w'):
                dot()
                dash()
                dash()
                
            elif (char == 'x'):
                dash()
                dot()
                dot()
                dash()
                
            elif (char == 'y'):
                dash()
                dot()
                dash()
                dash()
                
            elif (char == 'z'):
                dash()
                dash()
                dot()
                dot()

    if v ==2:
        for char in value:
            if (char == '1'):
                dot()
                dash()
                dash()
                dash()
                dash()
                
            elif (char == '2'):
                dot()
                dot()
                dash()
                dash()
                dash()
                
            elif (char == '3'):
                dot()
                dot()
                dot()
                dash()
                dash()
                
            elif (char == '4'):
                dot()
                dot()
                dot()
                dot()
                dash()
                
            elif (char == '5'):
                dot()
                dot()
                dot()
                dot()
                dot()
                
            elif (char == '6'):
                dash()
                dot()
                dot()
                dot()
                dot()
                
            elif (char == '7'):
                dash()
                dash()
                dot()
                dot()
                dot()
                
            elif (char == '8'):
                dash()
                dash()
                dash()
                dot()
                dot()
                
            elif (char == '9'):
                dash()
                dash()
                dash()
                dash()
                dot()
                
            elif (char == '0'):
                dash()
                dash()
                dash()
                dash()
                dash()
            
def dot():
    LED.on()
    time.sleep(1)
    LED.off()
    time.sleep(1)
    
def dash():
    LED.on()
    time.sleep(3)
    LED.off()
    time.sleep(1)

def function(Input):
    value = Input.get()
    if len(value)>12: Input.set(value[:12])

l1 = Label(win, text='Select an option from below', font=('Arial', 12))
l1.pack()

R1 = Radiobutton(win, text="Alphabets", value=1, variable = var, command=BlinkingMorsecode)
R1.pack()

R2 = Radiobutton(win, text="Numbers", value=2, variable = var, command=BlinkingMorsecode)
R2.pack()

label = Label(win, text='Type Something (not more than 12 characters)', font=('Arial', 12))
label.pack()

Input.trace('w', lambda name, index, mode, Input=Input: function(Input))
text_box = Entry(win, textvariable=Input, width=30, bg='white')
text_box.pack()

print = Button(win, text = 'print', command=BlinkingMorsecode)
print.pack()

def close():
    GPIO.cleanup()
    win.destroy()

exitButton =  Button(win, text = 'exit', command=close)
exitButton.pack()

win.mainloop()