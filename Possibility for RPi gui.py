# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 20:18:51 2017

@author: Noah Hamilton
"""

from tkinter import *
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)
GPIO.output(24, GPIO.LOW)

def toggle():
    if GPIO.input(24):
        GPIO.output(24, GPIO.LOW)
        toggleButton["text"] = "Turn LED On"
        
    else:
        GPIO.output(24, GPIO.HIGH)
        toggleButton["text"] = "Turn LED Off"
        
root = Tk()
root.title("toggler")
program_quit = root.destroy
toggleButton = Button(root,
                      text="Turn LED On",
                      command=toggle).pack(LEFT)

quitButton = Button(root,
                    text="QUIT",
                    fg="red",
                    bg="white",
                    command=program_quit)

root.mainloop()