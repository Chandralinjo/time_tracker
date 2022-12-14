import tkinter as tk
from tkinter import messagebox
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

def reset_file():
    # Show the pop-up window with the Yes/No buttons
    result = tk.messagebox.askyesno("Confirm", "Are you sure you want to clear history?")

    # If the user clicks Yes, show a message
    if result:
        tk.messagebox.showinfo("Success", "The action was completed successfully.")

def tidy_up():
    ## TODO write this function
    return

def update_timer():
    # Update label periodically
    if update_label:
        elapsed = datetime.now() - start_time
        elapsed_time.config(text="Elapsed time: " + represent_time(elapsed))
        window.after(1000, update_timer)

# Create the main window
window = tk.Tk()
window.geometry("300x200")
grid = tk.Frame(window)

# Create a text box to enter the name of a task
task_name = tk.Entry(window)
task_name.grid(row=0, columnspan=2)

# Create a button to start the timer
start_button = tk.Button(window, text="Start", command=start_timer)
start_button.grid(row=1, column=0)

# Create a button to stop the timer
stop_button = tk.Button(window, text="Stop", command=stop_timer)
stop_button.grid(row=1, column=1)

# Create a label to display the elapsed time
elapsed_time = tk.Label(window, text="Elapsed time:")
elapsed_time.grid(row=2, columnspan=2)

# Add two more buttons. One button should perform rounding and scaling for the current week.
# The second button should format the time_tracking file.
tidy_button = tk.Button(window, text="Tidy", command=tidy_up)
tidy_button.grid(row=3, column=0)

clear_button = tk.Button(window, text="Clear history", command=reset_file)
clear_button.grid(row=3, column=1)

grid.columnconfigure(0, minsize=150)
grid.columnconfigure(1, minsize=150)


# Run the main event loop
window.mainloop()
