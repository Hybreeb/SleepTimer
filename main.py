import tkinter as tk
from tkinter import ttk
import os
import time

class ShutdownTimer:
    def __init__(self, master):
        self.master = master
        master.title("Windows Shutdown Timer")

        # Create the GUI elements
        self.shutdown_time_label = ttk.Label(master, text="Shutdown in:")
        self.shutdown_time_label.grid(row=0, column=0, padx=10, pady=10)

        self.shutdown_time_options = ["0.5 hours", "1 hour", "1.5 hours", "2 hours", "2.5 hours", "3 hours", "3.5 hours", "4 hours"]
        self.shutdown_time_var = tk.StringVar()
        self.shutdown_time_var.set(self.shutdown_time_options[0])
        self.shutdown_time_dropdown = ttk.Combobox(master, textvariable=self.shutdown_time_var, values=self.shutdown_time_options)
        self.shutdown_time_dropdown.grid(row=0, column=1, padx=10, pady=10)

        self.cancel_button = ttk.Button(master, text="Cancel Shutdown", command=self.cancel_shutdown)
        self.cancel_button.grid(row=1, column=0, padx=10, pady=10)

        self.remaining_time_label = ttk.Label(master, text="Remaining time:")
        self.remaining_time_label.grid(row=1, column=1, padx=10, pady=10)

        self.remaining_time_display = ttk.Label(master, text="")
        self.remaining_time_display.grid(row=2, column=1, padx=10, pady=10)

        self.start_button = ttk.Button(master, text="Shutdown", command=self.initiate_shutdown)
        self.start_button.grid(row=2, column=0, padx=10, pady=10)

        self.shutdown_process = None
        self.timer_running = False

    def initiate_shutdown(self):
        shutdown_time = float(self.shutdown_time_var.get().split(" ")[0]) * 3600  # Convert time to seconds
        self.shutdown_process = os.popen(f"shutdown /s /t {int(shutdown_time)}")
        self.timer_running = True
        self.update_remaining_time(shutdown_time)

    def cancel_shutdown(self):
        if self.shutdown_process:
            os.popen("shutdown /a")
            self.shutdown_process = None
            self.timer_running = False
            self.remaining_time_display.config(text="")

    def update_remaining_time(self, remaining_time):
        if self.timer_running:
            minutes, seconds = divmod(remaining_time, 60)
            hours, minutes = divmod(minutes, 60)
            self.remaining_time_display.config(text=f"{int(hours)}:{int(minutes):02d}:{int(seconds):02d}")
            if remaining_time > 0:
                self.master.after(1000, lambda: self.update_remaining_time(remaining_time - 1))
            else:
                self.timer_running = False
                self.shutdown_process = None

root = tk.Tk()
app = ShutdownTimer(root)
root.mainloop()
