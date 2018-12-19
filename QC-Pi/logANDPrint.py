from datetime import date, time, datetime

now = datetime.now()
day_number = now.strftime("%d")
month_number = now.strftime("%m")
year_number = now.strftime("%Y")
time_stamp = now.strftime("%X")
counter = 0

currDATE = month_number + "-" + day_number + "-" + year_number
print (currDATE)

currTIME = time_stamp
print (time_stamp)

logNAME = currDATE + "-||-" + currTIME + "-||-" + "log.txt"
print (logNAME)

def logStartUser (username)
	f = open("home/pi/Desktop/Logs/Log01.txt", "w+")
	f.write("Hello there, from afar")
	f.close()

