import tkinter as tk
import pyautogui
import threading
import time

# Function to start the autoclicking
def start_autoclicker(interval):
    global running
    running = True
    while running:
        pyautogui.click()
        time.sleep(interval)

# Function to stop the autoclicker
def stop_autoclicker():
    global running
    running = False

# Function to handle the start button press
def start_button_pressed():
    try:
        interval = float(entry_interval.get())
        if interval > 0:
            # Start a new thread for autoclicking to avoid blocking the GUI
            threading.Thread(target=start_autoclicker, args=(interval,), daemon=True).start()
            status_label.config(text="Autoclicker is running...", fg="green")
            start_button.config(state=tk.DISABLED)
            stop_button.config(state=tk.NORMAL)
        else:
            status_label.config(text="Interval must be a positive number.", fg="red")
    except ValueError:
        status_label.config(text="Please enter a valid number.", fg="red")

# Function to handle the stop button press
def stop_button_pressed():
    stop_autoclicker()
    status_label.config(text="Autoclicker stopped.", fg="red")
    start_button.config(state=tk.NORMAL)
    stop_button.config(state=tk.DISABLED)

# Setup the GUI
root = tk.Tk()
root.title("Autoclicker")

# Create UI elements
label_interval = tk.Label(root, text="Click Interval (seconds):")
label_interval.pack(pady=10)

entry_interval = tk.Entry(root)
entry_interval.pack(pady=5)

start_button = tk.Button(root, text="Start", command=start_button_pressed)
start_button.pack(pady=10)

stop_button = tk.Button(root, text="Stop", command=stop_button_pressed, state=tk.DISABLED)
stop_button.pack(pady=10)

status_label = tk.Label(root, text="Enter a valid interval and press Start", fg="blue")
status_label.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
