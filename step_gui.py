import RPi.GPIO as GPIO
import time
import tkinter as tk
from threading import Thread

# Define pins and other constants
CW_PIN = 38   # CW+ pin
CCW_PIN = 36  # CCW+ pin
DELAY = 0.009

# Set up the GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(CW_PIN, GPIO.OUT)
GPIO.setup(CCW_PIN, GPIO.OUT)

# Function to rotate the motor to the desired angle


def rotate_to_angle(angle, direction_pin):
    steps = int(angle / 0.72)
    for _ in range(steps):
        GPIO.output(direction_pin, GPIO.HIGH)
        time.sleep(DELAY)
        GPIO.output(direction_pin, GPIO.LOW)
        time.sleep(DELAY)

# Function to stop the motor


def stop():
    GPIO.output(CW_PIN, GPIO.LOW)
    GPIO.output(CCW_PIN, GPIO.LOW)

# Function to handle the clockwise button press


def clockwise_press():
    thread = Thread(target=rotate_to_angle, args=(45, CW_PIN))
    thread.start()

# Function to handle the counterclockwise button press


def counterclockwise_press():
    thread = Thread(target=rotate_to_angle, args=(45, CCW_PIN))
    thread.start()

# Function to handle the button release/ stop the motor


def button_release():
    stop()


# Creating the Tkinter GUI
root = tk.Tk()
root.title("Robot Head Control")

# Creating the clockwise button
clockwise_button = tk.Button(
    root, text="Clockwise", command=clockwise_press, width=10, height=5)
clockwise_button.grid(row=0, column=0)

# Creating the counterclockwise button
counterclockwise_button = tk.Button(
    root, text="Counterclockwise", command=counterclockwise_press, width=10, height=5)
counterclockwise_button.grid(row=0, column=1)

# Binding the button release event
root.bind("<ButtonRelease-1>", lambda event: button_release())

# Running Tkinter main loop
root.mainloop()

# Cleaning up GPIO on program exit
GPIO.cleanup()
