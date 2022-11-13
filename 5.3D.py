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
var = IntVar()                                      #holds an integer
Input = StringVar()                                 #holds a string
    
def BlinkingMorsecode():      
    v = var.get()                                  #getting the integer input from the user
    value = Input.get()                            #getting the string input from the user
    value.upper()                                  #accepting the upper case string as well
    if v == 1:
        for char in value:
            if (char == 'a'):                      #morse code for a
                dot()
                dash()
            
            elif (char == 'b'):                    #morse code for b
                dash()
                dot()
                dot()
                dot()
            
            elif (char == 'c'):                     #morse code for c
                dash()
                dot()
                dash()
                dot()
                
            elif (char == 'd'):                     #morse code for d
                dash()
                dot()
                dot()
                
            elif (char == 'e'):                     #morse code for e
                dot()
                
            elif (char == 'f'):                     #morse code for f  
                dot()
                dot()
                dash()
                dot()
                
            elif (char == 'g'):                     #morse code for g
                dash()
                dash()
                dot()
                
            elif (char == 'h'):                     #morse code for h
                dot()
                dot()
                dot()
                dot()
                
            elif (char == 'i'):                      #morse code for i
                dot()
                dot()
                
            elif (char == 'j'):                      #morse code for j
                dot()
                dash()
                dash()
                dash()
                
            elif (char == 'k'):                      #morse code for k
                dash()
                dot()
                dash()
                
            elif (char == 'l'):                      #morse code for l
                dot()
                dash()
                dot()
                dot()
                
            elif (char == 'm'):                      #morse code for m
                dash()
                dash()
                
            elif (char == 'n'):                      #morse code for n
                dash()
                dot()
                
            elif (char == 'o'):                      #morse code for o
                dash()
                dash()
                dash()
                
            elif (char == 'p'):                      #morse code for p
                dot()
                dash()
                dash()
                dot()
                
            elif (char == 'q'):                      #morse code for q
                dash()
                dash()
                dot()
                dash()
                
            elif (char == 'r'):                      #morse code for r
                dot()
                dash()
                dot()
                
            elif (char == 's'):                       #morse code for s
                dot()
                dot()
                dot()
                
            elif (char == 't'):                       #morse code for t 
                dash()
                
            elif (char == 'u'):                       #morse code for u
                dot()
                dot()
                dash()
                
            elif (char == 'v'):                       #morse code for v
                dot()
                dot()
                dot()
                dash()
            
            elif (char == 'w'):                       #morse code for w
                dot()
                dash()
                dash()
                
            elif (char == 'x'):                       #morse code for x
                dash()
                dot()
                dot()
                dash()
                
            elif (char == 'y'):                       #morse code for y
                dash()
                dot()
                dash()
                dash()
                
            elif (char == 'z'):                        #morse code for z
                dash()
                dash()
                dot()
                dot()

    if v ==2:
        for char in value:
            if (char == '1'):                          #morse code for number 1
                dot()
                dash()
                dash()
                dash()
                dash()
                
            elif (char == '2'):                        #morse code for number 2
                dot()
                dot()
                dash()
                dash()
                dash()
                
            elif (char == '3'):                         #morse code for number 3
                dot()
                dot()
                dot()
                dash()
                dash()
                
            elif (char == '4'):                          #morse code for number 4
                dot()
                dot()
                dot()
                dot()
                dash()
                
            elif (char == '5'):                          #morse code for number 5
                dot()
                dot()
                dot()
                dot()
                dot()
                
            elif (char == '6'):                          #morse code for number 6
                dash()
                dot()
                dot()
                dot()
                dot()
                
            elif (char == '7'):                           #morse code for number 7
                dash()
                dash()
                dot()
                dot()
                dot()
                
            elif (char == '8'):                            #morse code for number 8
                dash()
                dash()
                dash()
                dot()
                dot()
                
            elif (char == '9'):                            #morse code for number 9
                dash()
                dash()
                dash()
                dash()
                dot()
                
            elif (char == '0'):                             #morse code for number 0
                dash()
                dash()
                dash()
                dash()
                dash()
            
def dot():
    LED.on()                                                #declaring the dot function and setting the time delay of 1 sec for both led on and off
    time.sleep(1)
    LED.off()
    time.sleep(1)
    
def dash():
    LED.on()
    time.sleep(3)                                           #declaring the dash function and setting the time delay of 3 sec for led on and 1 sec for led of
    LED.off()
    time.sleep(1)

def function(Input):
    value = Input.get()
    if len(value)>12: Input.set(value[:12])                 

l1 = Label(win, text='Select an option from below', font=('Arial', 12))
l1.pack()                                                    #pack() is used so that the text appears in a packed box

R1 = Radiobutton(win, text="Alphabets", value=1, variable = var, command=BlinkingMorsecode)    
R1.pack()                                                    #creating the radiobutton1

R2 = Radiobutton(win, text="Numbers", value=2, variable = var, command=BlinkingMorsecode)
R2.pack()                                                     #creating radiobutton2

label = Label(win, text='Type Something (not more than 12 characters)', font=('Arial', 12))
label.pack()

Input.trace('w', lambda name, index, mode, Input=Input: function(Input))    
text_box = Entry(win, textvariable=Input, width=30, bg='white')    #creating a text box where the input will be taken from the user
text_box.pack()

print = Button(win, text = 'print', command=BlinkingMorsecode)   #creating a print button
print.pack()

def close():
    GPIO.cleanup()
    win.destroy()

exitButton =  Button(win, text = 'exit', command=close)         #creating an exit button
exitButton.pack()

win.mainloop()
