# Tanit Python Keylogger
Tanit Keylogger is a simple but powerfull remote python keylogger for MS Windows, Mac OS and Linux OSs. The tool is named after the Phoenician chief goddess of Carthage. The tool sends you a report to your email every specific amount of time. Please change these parameters in main.py.

The tool is part of an Ethical Hacker Educational toolset taught normally in ethical hacking and computer security degrees (please see code of conduct). 

Tanit Keylogger is part of a toolset of Ethical Hacking tools that I will publish gradually on Github.
1. Tanit Keylogger (Language: Python) - current repository.
2. Adonis ARP Spoofer (Language: Python), repository URL (will be added later).
3. Simple MAC Changer (Language: Python), repository URL (will be added later).
4. Anat Network Scanner (Language: Python), repository URL (will be added later).
5. Hadad Keylogger (Language: Python), repository URL (will be added later).
6. Shahar DNS Spoofer (Language: Python), repository URL (will be added later).
7. Sweet Death Virus (Language: Python), repository URL (will be added later).
8. Baal Backdoor (Language: Python), repository URL (will be added later).
9. Website Crawler (Language: Python), repository URL (will be added later).
10. Vulnerability Scanner (Language: Python), repository URL (will be added later).
11. Passwords Harvester (Language: Python & JavaScript), repository URL (will be added later).
12. Code Injector (Language: Python & JavaScript), repository URL (will be added later).


# Code of Conduct
**This tool is written after taking several Ethical Hacking and Security courses. So in other words, the code (which has a generated executable intentionally detectable by antiviruses) can be found in a form or another in ethical hacking books and video courses. I have added enhancements on the tool of course. To reiterate: This is a tool written in the sole purpose of teaching you how remote and local keyloggers work and it really shows you how much it is easy to write an simple effective and yet powerfull keylogger in Python. This tool is for educational purposes only and it is not meant to be used in any harmfull way. Actually I was going to address antiviruses evation in a seperate section in the documentation (since your executable will be immediately detected and deleted by any good antivirus on the market) but I decided not to do so (I might change my mind later). The point I am driving home here is the fact that this tool is meant to be a tool to be studied by white hat hackers and security specialists and is not meant to be deployed against victims.**

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
You need to package the source code as executable for your target Operating System (please see packaging). Please change the time interval and email to suit your needs in main.py. Black hackers normally use trojan horse techniques to masquerade the tool as a legitimate application so that the user will not be suspicious and would click on the file to run the application which could look like a PDF or image or anything really.

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
# Enhancements
## Adding the program to registry
One enhancement is to make the program copy itself to a location not suspicious with a new name and add itself to the registry (on MS Windows - very easy) or to the init deamon configuration files on Linux OSs (very tricky)

## Masquerading the file as legitimate (Trojan Horse Techniques)
Packaging the keylogger with an image or PDF. 
Changing the icon and spoofing the extension of the file. I will write a guide on how to do that soon.

## Avoiding antiviruses
I have to mention the fact that the mere act of writing your own Hacking/Security programs with your own way of coding makes these programs unique in a way and thus undetectable and you will know why when I explain the main techniques used by antiviruses. Source Codes and by consequence executable binaries generated out of them, are always detected when they are either too traditional or have been used by many people. Per instance, the code here has great parts from many sources (a salad of code) and that is intentional actually.

Now the tricks here are really a race with time for different reasons:
- 1st technique: Anti-viruses compares your program to a huge database of signatures of other malware. By huge I mean massive. In lay terms, huge number of signatures (i.e. snippets of logic if you want) sort of database of malware logic.
- 2nd technique: This technique is used in tandem with the first and works as a safe guard if signature is not found. It compares the behaviour of your program in real-time using a sandbox or virtual environment. The comparision involves sometimes some clever machine and deep learning algorithms. Now of course every antivirus give this technique some sort of a brand and fancy name but it boils down to the same concepts. The techniques are numerous, the antivisus try to figure out if  your program is opening suspiciously a network port or downloading things or taking snapshots or capturing keystrokes, or connecting to a remote host vel cetera...

You sould be worried about the second point not the first one becuase you have literally at your disposable a trillion methods to make your program quite unique to fool an antivirus to think it is harmless and thus no signature would be matched in this way. That does not mean the second technique could not be defeated.

Some Source Code tricks (the following is a big field and art in itself so this is just a drop from the ocean):
1. Add useless code before, in-between (if possible) and after the malicious code. Add a lot of padding logic (useless loops, useless mathematical operations etc...)
2. Play with sleep patterns of your Python scripts (pausing the program and resuming it, then pausing and resuming)
3. Play with program threading like spawning threads especially useless ones per example some weird mathematical equation calculation is in a seperate thread (I found this achieves amazing results)
4. Add variables that are gibberish. There are some tools that transform all your variables to shorter names. These types of tools are called obfuscation tools that fool and confuse both humans and antiviruses. Black and grey Hackers usually change the code of the program to the point that the padding or usefull behaviour should be far more sizable in your tool than the actual malicous code which should be scattered in different places.
...

Some Binaries/executable tricks
1. Changing the Binaries and adding padding (this require knowledge in reverse enginneering and changing hex codes). Same things you did in source code but on the level of the executable itself.
2. An easier way: Compressing the binaries executables (like the .exe) via tools like UPX (https://github.com/upx/upx), a tool that compresses exe.

Scan your exe via some tools and online services that scan your tool across different antiviruses (famous and non famous) WITHOUT submitting the results to antiviruses. One service that is quite handy is called NoDistribute (https://nodistribute.com/). 

# License
This program is licensed under GNU GPL v3 License - you are free to distribute, change, enhance and include any of the code of this application in your tools. I only expect adequate attribution of this work. The attribution should include the title of the program, the author and the site or the document where the program is taken from.

