import os
from ftplib import FTP

#def networkConnection():
#def connectionTest1():
#	s = pxssh.pxssh()
#	hostname = '128.10.10.5/volume1/mis/TEST'
#	username = 'tester'
#	password = 'IuScRe1480'
#	s.login(hostname, username, password)
#	s.sendlin('echo "Made it."')
#	print('Made it 2!')
#	sleep(10)
#
def connectionTest2(currJob):
	ftp = FTP('128.10.10.5')
	uname = "admin"
	pword = "sImCiTy55!"
	filenames = "example.txt"
	ftp.login(uname, pword)
	print("Inside NAS")
	ftp.cwd('volume1/mis/TEST/')
	print("Changed DIR success")
	ftp.sendcmd('pwd')
	ftp.quit()
	#print("File List: ")
	#files = ftp.dir()
	#print files
	#ftp.cwd('/volume1/public/PHOTO SHIP/2018')
	#ftp.mkd('/volume1/public/PHOTO SHIP/2018' + currJob)
	#ftp.transfercmd()
