import os
import datetime

def findCurrentYear():
    now = datetime.datetime.now()
    return str(now.year)

def createDIR(directory):
	if not os.path.exists(directory):
		os.makedirs(directory)
	elif os.path.exists(directory):
		print("Directory (" + directory + ") already exists")
		pass
	else:
		print ('Error: Creating directory. ' + directory)

def nameDIR():
    jobIDNumber = raw_input("Please scan or enter job ID (or Press Q to quit): ")
    if (jobIDNumber == 'q') or (jobIDNumber == 'Q'):
		jobIDNumber = 'FALSE'
		return jobIDNumber
    year = findCurrentYear()
    #dirPathPART = "Documents/" + year + "/" + jobIDNumber		#Needs to be
    dirPathPART = "/mnt/usbstorage/" + year + "/" + jobIDNumber
    testDIRPathPART = "Test/" + jobIDNumber
    createDIR(jobIDNumber)
    print (dirPathPART)		#Test PRINT
    return jobIDNumber
