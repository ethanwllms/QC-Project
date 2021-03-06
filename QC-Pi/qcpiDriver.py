import os
import sys
import keyboard
import subprocess
from time import sleep
#import picamera
import createDirectory
import userAuth
import imageCapture

def TestDrive():
	authTokenTest = userAuth.authenticateUser(initializer)
	if authTokenTest == True:
		currDirectory = createDirectory.nameDIR()
		sshTestSession = networkInteraction.testAccess()
		print("Tests complete! ...Bye!")
	else:
		sys.exit()

def officialDrive():
	initializer = 0
	numPhoto = 1
	if initializer > 0:
		return
	authToken = userAuth.authenticateUser(initializer)
	if authToken == True:
		endSession = False
		while endSession != True:
			print("Please select desired option: ")
			print("1. Start Job Session")
			print("2. End Job Session")
			endSession = input("Selection: ")
			if endSession == "2":
				print("Goodbye, come back now ya'hear!")
				sleep(5)
				sys.exit()
			print("\n")
			while endSession != "2":
				os.chdir("/media/usb/TEST/")
				currJobDirectory = createDirectory.nameDIR()
				if currJobDirectory == 'FALSE':
					break
				currJob = currJobDirectory
				temp = 0
				innermostUserSelect = "n"
				currDir = "/media/usb/TEST/" + currJob
				os.chdir(currDir)
				while (innermostUserSelect != "q") or (innermostUserSelect != "Q"):
					print("\n")
					print("Capture point:")
					print("Press Enter key to capture image.")
					print("Press 'P' to preview image for 20s before capture.")
					print("Press 'Q' to Quit and move to next job.")
					innermostUserSelect = input("Selection: ")
					if (innermostUserSelect == "q") or (innermostUserSelect == "Q"):
						sleep(2)
						break
					elif (innermostUserSelect == "p") or (innermostUserSelect == "P"):
						preview = imageCapture.imagePreview()
						print("Previewing Call made . . .")
					elif innermostUserSelect == "":
						imageName = currJobDirectory + '-' + str(numPhoto)
						print("Say, Cheese!")
						imageRendered = imageCapture.imageCapture(imageName)
						numPhoto += 1					#currImageCapture = imageCapture.captureCam(currJobDirectory)
