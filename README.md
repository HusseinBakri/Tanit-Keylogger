# Tanit Python Keylogger
Tanit Keylogger is a simple but powerfull remote python keylogger for MS Windows, Mac OS and Linux OSs. The tool is named after the Phoenician chief goddess of Carthage. The tool sends you a report to your email every specific amount of time. Please change these parameters in main.py.

The tool is part of an Ethical Hacker Educational toolset taught normally in ethical hacking and computer security degrees/courses (please see code of conduct). 

Tanit Keylogger is part of a toolset of Ethical Hacking tools that I will publish gradually on Github.
1. Tanit Keylogger (Language: Python) - ***current repository***.
2. Adonis ARP Spoofer (Language: Python) - Go to [repository URL](https://github.com/HusseinBakri/Adonis-ARP-Spoofer "Adonis ARP Spoofer").
3. Simple MAC Changer (Language: Python), repository URL (will be added later).
4. Anat Network Discoverer and Port Scanner (Language: Python) - Go to [repository URL](https://github.com/HusseinBakri/Anat-Network-Discoverer-and-Port-Scanner "Anat Network Discoverer and Port Scanner").
5. Hadad Packet Sniffer (Language: Python), repository URL (will be added later).
6. Shahar DNS Spoofer (Language: Python), repository URL (will be added later).
7. Sweet Death Virus (Language: Python), repository URL (will be added later).
8. Baal Backdoor (Language: Python), repository URL (will be added later).
9. Vulnerability Scanner (Language: Python), repository URL (will be added later).


# Code of Conduct
**Launching this tool against unauthorised and unwilling users is immoral and illegal. As a white hat hacker or security specialist, your job after taking permission, is to discover vulnerabilities in programs, systems and networks (white hat hacking) or help in discovering any gullibility in users (by social engineering). Thus, you can only launch Tanit or any other tool I will publish later in this series when you are given permission by the company that hires you or you only launch it against your own servers or networks. This tool is written after taking several Ethical Hacking and Security courses. So, in other words, the code (which has a generated executable intentionally detectable by antiviruses) can be found in a form or another in ethical hacking books and courses. I have added enhancements on the tool of course. To reiterate: This is a tool written in the sole purpose of teaching you how remote and local keyloggers work and it really shows you how much it is easy to write a simple, effective and yet powerful keylogger in Python. This tool is for educational purposes only and it is not meant to be used in any harmful way. To reiterate, this tool is meant to be a tool to be studied by white hat hackers and security specialists and is not meant to be deployed against users that do not give you explicit permission.**

# Description
A python Remote keylogger that logs all keystrokes that have been typed by a user and then sends a report to an email every specific amount of time. You can package it as an executable for MS Windows, Linux OSs, and Mac OS. Please refer to the section called Packaging where I explain how to do that in detail. Enjoy!

# Requirements
You need to install pynput Python module. You can install it by pip or any other method you that you are confortable with:
```
pip install pynput
```

# Usage 
## Irrealistic usage (educational)

```
python main.py 
```
## Deployment Usage
You need to package the source code as executable for your target Operating System (please see packaging). Please change the time interval and email to suit your needs in main.py. Black and grey hat hackers normally use trojan horse techniques to masquerade the tool as a legitimate application so that the user will not be suspicious and would click on the file to run the application which could look like a PDF or image or anything really.

# Packaging
You need the pyinstaller. You can install it via pip or pip3 or via apt package manager vel cetera
```
pip install pyinstaller
```

A program called pyinstaller is installed in the Python directory. On Windows it would be an executable: pyinstaller.exe

## Notez Bien - Antivirus won't be happy!!!

Please turn off any antivirus on the target system since the executable will be detected and the antivirus will try to delete or quarantine it. Antivirus evasion is addressed in the section titled 'Avoiding antiviruses'.

```
pyinstaller main.py --onefile
```
--onefile means  pyinstaller will package all the python files into a single executable

## How to package and run the excutable silently (without showing a terminal to the user)
If you do not want the user to see a command prompt after the .exe is run. You can add another argument called
--noconsole

```
pyinstaller main.py --onefile --noconsole
```

This can work in almost all instances except when your Python code deals with standard input/output/error. 

You have to explicitly deal with standard error and standard input so per example if we have something like (just an example)
```
result = subprocess.check_output(command, shell=True)
```

You need to handle the 'stderr' and 'stdin' by throwing them in the Abyss!

### For Python 3
```
result = subprocess.check_output(command, shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL )
```
### For Python 2 (you need to import the os module)
```
DEVNULL = open(os.devnull, 'wb')
result = subprocess.check_output(command, shell=True, stderr=DEVNULL, stdin=DEVNULL )
```

## Create a Windows .exe executable out of a python project from a Linux OS
As you know to run a Windows .exe or .msi or anything similar on a Linux OS (even on Mac OS) you need a lovely program called  [wine](https://www.winehq.org/). I would assume you have installed wine on Linux. Go to the official Python Website and download the right Python 2.7.x msi installation file. Navigate on your Linux to the directory of the download directory of this file and then run the following command: (/i is for installing):
```
wine msiexec /i python-2.7.14.msi
```
You will get a normal installation process as you would have on any MS Windows OS, please follow the instruction to install the Python interpreter. All Programs are usually installed in wine in a hidden folder called '.wine' in the Home Folder of the user. So probably your Windows Python will be 
installed in ~/.wine/drive_c/Python27/ and in there all the cool executable that normally are installed like Python.exe .... Naviagate to this folder and run via wine the Python interpreter invoking pip in order for you to install as above the 'pyinstaller' module.

PS: wine does not access the pip modules of the Linux so this why you need to do this.
```
cd ~/.wine/drive_c/Python27/
wine python.exe -m pip install pyinstaller
```
After the installation of the module successively terminates, you will find the pyinstalller.exe in the Scripts directory.
To install pynput (why? as mentioned above, you need to do that as even this module is installed on Linux OS, the Windows Python interpreter needs this)

```
wine python.exe -m pip install pynput
```

You can then package Tanit Keylogger into a single executable:

```
wine /root/.wine/drive_c/Python27/Scripts/pyinstaller.exe main.py --onefile --noconsole
```
The binary will be stored in the dist folder.

## Creating a Mac OS executable of Tanit
If you are on a Mac OS, the process is the same for installing 'pyinstaller'. First install pyinstaller through latest pip - with sudo privileges. NB: it is better to get the latest pip so to avoid errors. 

```
sudo pip install pyinstaller
```

Then run pyinstaller on main.py

```
pyinstaller main.py --onefile --noconsole
```
The binary will be stored in the dist folder.

## Creating a Linux OS executable of Tanit
The process is exactly similar. The good thing in Linux is that binaries in Linux don't get executed by just making the target user double click them, they need to be run from the terminal after chmod +x makes them executable. This is why Linux rocks, the good thing it is very difficult a experience Linux users (in social enginering, a white hat hacker is hired by many companies these days to test not only the security of networks and systems but also in similar vein to test the gullibility of the company's clerks by the white hat hacker pretending to be from the IT department! 

# Enhancements
## Adding the program to MS Windows registry to preserve persistance (after reboot)
One enhancement (keylogger_persistance_windows.py) is made to make the program copy itself to a location not suspicious with a new name and add itself to the registry of MS Windows - very easy. On Mac OS and Linux OS, this can be done but can be a little bit tricky (I will add this feature in later versions).

## Masquerading the file as legitimate (a.k.a Trojan Horse Techniques)
Packaging the keylogger with an image or PDF and changing the icon and spoofing the extension of the file. I will write a guide on how to do that soon.

## Avoiding antiviruses
I have to mention the fact that the mere act of writing your own Hacking/Security programs with your own way of coding makes these programs unique in a way and thus undetectable and you will know why when I explain the main techniques used by antiviruses. Source Codes and by consequence executable binaries generated out of them, are always detected when they are either too traditional or have been used by many people (so they ended up as a signature in Antiviruses databases). Per instance, the code here has great parts from many sources (a salad of code) and that is intentional.

Now the tricks here are really a race with time for different reasons:
- 1st technique: Anti-viruses compares your program to a huge database of signatures of other malware. By huge, I mean massive. In lay terms, huge number of signatures (i.e. snippets of logic if you want) sort of database of malware logic.
- 2nd technique: This technique is used in tandem with the first technique and works as a safe guard if the signature is not found. It compares the behaviour of your program in real-time using a sandbox or virtual environment. The comparision involves sometimes some clever machine and deep learning algorithms. Now of course every antivirus gives this technique some sort of a brand and fancy name but it boils down to the same concepts. In nutshel, the antivisus try to figure out if your program is doing something suspicious like opening a network port or downloading things or taking snapshots or capturing keystrokes, or connecting to a remote host vel cetera...

You sould be worried about the second technique when you want to evade antivirus more than the first one, becuase you have literally at your disposable a trillion methods to make your program quite unique to fool an antivirus to think it is harmless and thus no signature would be matched in this way. That does not mean the second technique could not be defeated.

Some Source Code tricks (which is a big field and an art in itself so this is just a drop from the ocean):
1. Add useless code before, in-between (if possible) and after the malicious code. Add a lot of padding logic (useless loops, useless mathematical operations etc...)
2. Play with sleep patterns of your Python scripts (pausing the program and resuming it, then pausing and resuming)
3. Play with program threading like spawning threads especially useless ones per example some weird mathematical equation calculation  in a seperate thread (this achieves amazing results)
4. Add variables that are gibberish. There are some tools that transform all your variables to shorter names or gibberish. These types of tools are called 'obfuscation tools' that fool and confuse both humans and antiviruses. Black and grey hat Hackers usually change the code of the program to the point that the padding or usefull behaviour should be far more sizable in your tool than the actual malicous code which should is notmally scattered in different places of your program.
...

Some Binaries/executable tricks:
1. Changing the binaries and adding padding. This requires knowledge in reverse enginneering and changing hex codes. Same things you did in the source code but this time on the level of the executable itself. Changing the hex code of the .exe files per example is usually done by opening the executable in a hex editor and changing very carefully some or all of the readable sentences into something else while avoiding overwriting any usable hex code (otherwise the executable will not work). This usually makes the executable bypass all known anti-viruses.
2. Another easier way: Compressing the binaries or executables (like compressing the .exe) via tools like UPX (https://github.com/upx/upx), a tool that compresses exe files.

Scan your .exe via tools and online services that scan your tool across different antiviruses (famous and non famous) **WITHOUT** submitting the results to antiviruses. One service that is quite handy is called NoDistribute (https://nodistribute.com/).

Please after you are successfull in running your hacking tool evading antiviruses, you are bound by an ethical code of conduct, so you are required morally and legally to submit your tool and code to antiviruses databases.

### Running the keylogger after a successful backdoor attack that is undetectable by antiviruses

Tanit keylogger or any other hacking tool can be run on the victim remotely by using a backdoor. You can use an awesome tool called the Veil Framework (https://github.com/Veil-Framework/Veil). Veil generates completely undetectable backdoors to hack into computers

You need a Linux preferably a Kali Linux to create the backdoor. Veil requires a lot of libraries and packages to be installed. To install Veil on Linux, you need to clone the **latest** GitHub repo and from the terminal you need to cd into the config directory in the repo. There is a setup.sh script that will install all the libraries needed for the Veil Framework to work properly. Run the setup file. You can of course use the --silent switch to allow the framework to install in silent mode using the default settings. You can also use the --force switch which will overwrite any existing installation of Veil in case you were obliged to install the libraries and the framework again for whatever reason.

```./setup.sh --silent --force```

Veil is a python file that is executable. You can run from the terminal

```./Veil.py```

Make sure that you **always update Veil since your aim to evade anti-viruses**. You can update Veil from inside the framework when executed.

Veil bypasses anti-viruses by encrypting, obfuscating and padding malicious code. In the different backdoor payloads that you have, you  can set the reverse IP/PORT which would be the IP of the attacker. One or two antiviruses might still detect Veil. To bypass this, I strongly advice you to play around with the options of each payload until you get something completely different and thus completely undetectable. It is advisable to try different values for the options of the payload such as the Number of processors, and the sleep in seconds to achieve a perfect result. 

The beauty of Veil is that it generates an .exe completely undetectable if you can figure out the right otions to make your backdoor quite unique from signature-wise perspective. It also generates a source code file of the backdoor depending on the payload language that you have chosen: go, python, lua, C, C# etc….

Two other famous and powerfull tools that do the same thing as Veil framework which you might be obliged to consider in case Veil fails: The Fat Rat (https://github.com/Screetsec/TheFatRat) and the Empire project (https://github.com/EmpireProject/Empire). Both tools can generate undetectable backdoors for MacOS, Android, Linux and MS Windows.
  
Scan your .exe via tools and online services that scan your tool across different antiviruses (famous and non famous) **WITHOUT** submitting the results to antiviruses. One service that is quite handy is called NoDistribute (https://nodistribute.com/).

Please after you are successfull in running your hacking tool which evaded antiviruses, you are bound by an ethical code of conduct, so you are required morally and legally to submit your tool and code to antiviruses databases.

# License
This program is licensed under MIT License - you are free to distribute, change, enhance and include any of the code of this application in your tools. I only expect adequate attribution and citation of this work. The attribution should include the title of the program, the author (me!) and the site or the document where the program is taken from.

