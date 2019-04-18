import os
import userDict
import getpass
from userDict import users

userfile = open('userDict.py')

def checkUsername(username):
	if username in users:
		return True
	else:
		return False

def checkPassword(username, password):
	if password == users[username]:
		return True
	else:
		return False

def authenticateUser(initializer):
	os.system('clear')
	username = input("Please enter username: ")
	if checkUsername(username) == True:
		password = getpass.getpass(prompt='Please enter password: ')
	if checkPassword(username, password) == True:
		os.system('clear')
		initializer += 1
		return True
	else:
		while checkUsername(username) != True:
			print ("Incorrect username.")
			username = input("Please re-enter username: ")
			if checkUsername(username) == True:
				password = getpass.getpass(prompt='Please enter password: ')
			if checkPassword(username, password) == True:
				initializer += 1
				return True
				break
		else:
			while checkPassword(username, password) != True:
				print("Incorrect password.")
				password = getpass.getpass(prompt='Please enter password: ')
				if checkPassword(username, password) == True:
					initializer += 1
					return True
					break
