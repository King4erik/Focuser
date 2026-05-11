# Focuser
<b> I made this program for my IGCSE exams </b>

# Features of the program
- It kills the process specified in the blocked_apps.txt
- Logs the program that has been killed into Focuser_log.csv

# How to use this program
- Full the blocked_apps.txt or use the gui script to full it with the title name or the executable name of the application in it
- Use a #executable name or #title name to make it persistent through the session (the program will killed even after it is removed from the wordlist)

# To make it into an exe
Using Nuitka<br>
```nuitka --onefile --windows-console-mode=disable --nofollow-imports --clean-cache=all --output-dir="exe" --remove-output .\appblocker.py```
<br>Using Pyinstaller<br>
```pyinstaller --onefile --noconsole --distpath "exe/" appblocker.py```

# To make the program start whenever the system starts
```reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Run" /v Appblocker /t REG_SZ /d "exe\appblocker.exe"```

<h4>Note: if the commands didn't work. Try giving the complete file path and put the folder into an exclusion file</h3>

# TODO:
- Make a better GUI