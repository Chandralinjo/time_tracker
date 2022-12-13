import tkinter as tk
from datetime import datetime

# Define global variables
start_time = None
update_label = False

def represent_time(td):
    total_seconds = td.total_seconds()

    # Calculate the number of hours, minutes, and seconds
    hours = int(total_seconds // 3600)
    minutes = int((total_seconds % 3600) // 60)
    seconds = int(total_seconds % 60)

    return f'{hours} hours, {minutes} minutes, {seconds} seconds'

def start_timer():
    # Starts the timer and the label updating process
    global start_time
    global update_label
    start_time = datetime.now()
    update_label = True

    # Make sure that task name can't be changed while task is active
    task_name.config(state=tk.DISABLED)
    window.after(1000, update_timer)

def stop_timer():
    # Calculate the elapsed time and record it in the file
    global update_label
    elapsed = datetime.now() - start_time
    elapsed_time.config(text="Elapsed time: " + represent_time(elapsed))
    update_label = False

    # Make sure that task name is modifiable again
    task_name.config(state=tk.NORMAL)

    # Save the elapsed time to a file
    with open("time_tracking.txt", "a") as file:
        file.write(task_name.get() + ": " + represent_time(elapsed) + "\n")

def update_timer():
    # Update label periodically
    if update_label:
        elapsed = datetime.now() - start_time
        elapsed_time.config(text="Elapsed time: " + represent_time(elapsed))
        window.after(1000, update_timer)

# Create the main window
window = tk.Tk()
window.geometry("400x200")

# Create a text box to enter the name of a task
task_name = tk.Entry(window)
task_name.pack()

# Create a button to start the timer
start_button = tk.Button(window, text="Start", command=start_timer)
start_button.pack()

# Create a button to stop the timer
stop_button = tk.Button(window, text="Stop", command=stop_timer)
stop_button.pack()

# Create a label to display the elapsed time
elapsed_time = tk.Label(window, text="Elapsed time:")
elapsed_time.pack()


# Run the main event loop
window.mainloop()
