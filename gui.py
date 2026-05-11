from appblocker import get_current_process, main

from tkinter import *

import threading
import subprocess
import os

file = "blocked_apps.txt"
wordlist = open(file, "r+")
program_path = 'exe/appblocker.exe'

def program_start():
    if os.path.isfile(program_path):
        if "appblocker.exe" not in get_current_process()[1]:
            subprocess.run([program_path])
    else:
        main(file)
    return None

def start():
    start_thread = threading.Thread(target=program_start)
    start_thread.start()

def confirm():
    ini_wordlist = Textbox.get("1.0", "end-1c")
    with open(file, "w+") as f:
        f.write(ini_wordlist)

def exit_gui():
    root.destroy()

root = Tk()
root.title("Focuser")
root.geometry("326x600")
root.configure(bg="Black")

# Label
text = Label(root, text="Welcome to the Focuser!", font=("Arial", 18), fg="White", bg="Black")
text.grid(row=0, column=2)

# Textbox
Textbox = Text(root, height=30, width=40, bg="White")
Textbox.get("1.0", "end-1c")
Textbox.insert("1.0", wordlist.read())
# Textbox.place(anchor="center")
Textbox.grid(row=1, column=2)

# Confirm Button
ConfirmButton = Button(root, text="Update", command=confirm, width=10)
ConfirmButton.grid(row=2, column=2)

# Start the Focus
StartButton = Button(root, text="Start Focuser", command=start, width=10)
StartButton.grid(row=3, column=2)

# Exit button
ExitButton = Button(root, text="Exit the GUI", command=exit_gui, width=10)
ExitButton.grid(row=4, column=2)

root.mainloop()