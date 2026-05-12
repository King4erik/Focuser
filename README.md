# Focuser
<b> I made this program for my IGCSE exams </b>
<br>No external libraries is used

# Features of the program
- It kills the process specified in the blocked_apps.txt
- Logs the program that has been killed into Focuser_log.csv

# How to use this program
- Full the blocked_apps.txt or use the gui script to full it with the title name or the executable name of the application in it
- Use a #executable name or #title name to make it persistent through the session (the program will get killed even if it is removed from the wordlist)

# How to run this program
~~~
python appblocker.py
~~~
~~~
python gui.py
~~~
1. Type in the applications to be blocked in the textbox
2. Click "Start Focuser" button

# To build an exe
Using Nuitka<br>
~~~
nuitka --onefile --windows-console-mode=disable --nofollow-imports --clean-cache=all --output-dir="exe" --remove-output .\src\appblocker.py
~~~
<br>Using Pyinstaller<br>
~~~
pyinstaller --onefile --noconsole --distpath "exe/" .\src\appblocker.py
~~~

# To make the program start whenever the system starts
~~~
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Run" /v Appblocker /t REG_SZ /d "exe\appblocker.exe"
~~~

<h4>Note: if the commands or program didn't work. Try giving the complete file path and put the folder into an exclusion file</h3>

# TODO:
- Make a better GUI
- Create a build script with the command to place it in the startup
- ~~Make the files more organized~~
- Make an option to allow users to use custom scripts for different purposes (some applications while studying or some while working)
