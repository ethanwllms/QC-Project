import os
import time
#import paramiko
import shutil
#python remote_mkdir.py 128.10.10.5 guest 14801480 /mis/Test/jobIDNumber

#os.system ('')

#def testAccess():
	#Transport
#	host = "128.10.10.5"
#	port = 22
#	transport = paramiko.Transport((host, port))
	#Auth
#	username = "tester"
#	password = "IuScRe1480"
#	transport.connect(username = username, password = password)
#	time.sleep(2)
	#Connect
#	sftp = paramiko.SFTPClient.from_transport(transport)
#	print ("Transport is active and open. Closing..")
#	time.sleep(3)
	#Upload
#	filepath = '/volume1/mis/TEST/'
#	localpath = '/Users/ethanwilliams/Desktop/Stuff/Work/QC-Pi/Test/321654/exFile.txt'
#	if sftp.listdir(path=os.path.dirname(filepath)):
#		sftp.put(localpath, filepath, callback=None, confirm=True)
#		print("SFTP has now completed.")
	#Stop - Close
#	print("Transport is now inactive. Closing..")
#	sftp.close()
#	transport.close()
#	os.system('clear')

def newNETAccess():
    os.system('ssh tester@128.10.10.5')
