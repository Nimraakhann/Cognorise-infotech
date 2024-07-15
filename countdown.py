import tkinter as tk
import time

def countdown_timer():
    try:
        seconds = int(entry.get())
    except ValueError:
        label.config(text="Please enter a valid integer!")
        return

    while seconds >= 0:
        label.config(text=f"Time left: {seconds} seconds")
        root.update()
        time.sleep(1)
        seconds -= 1

    label.config(text="Time's up!")

# Creating the main tkinter window
root = tk.Tk()
root.title("Countdown Timer")

# Label for instructions
label = tk.Label(root, text="Enter time (in seconds):")
label.pack()

# Entry field for user input
entry = tk.Entry(root)
entry.pack()

# Start button to initiate countdown
button = tk.Button(root, text="Start", command=countdown_timer)
button.pack()

# Start the tkinter event loop
root.mainloop()
