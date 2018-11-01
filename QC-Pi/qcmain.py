#!/usr/bin/env python
import sys
import keyboard
import qcpiDriver
import networkInteraction

print("Welcome to the QC Automation Appliance.")

print("Main Menu: ")
print("1. Start Workflow")
print("2. Test Network")
print("3. View Job Log")
print("4. Administrator Settings")
print("5. Exit Appliance")

mainselect = raw_input("Enter the number corresponding to the menu item desired: ")
while mainselect > "0":
    if mainselect == "1":
        print("Made it to Cond. #1")
	driver = qcpiDriver.officialDrive()
    elif mainselect == "2":
        print("Made it to Cond. #2")
	#sshTest = networkInteraction.testAccess()
	copyTest = networkInteraction.newNETAccess()
    elif mainselect == "3":
        print("Made it to Cond. #3")
	pass
    elif mainselect == "4":
        print("Made it to Cond. #4")
	pass
    elif mainselect == "5":
        print("Made it to Cond. #5")
	sys.exit()
    else:
	print("Menu item entered is incorrect.")
	mainselect = input("Please re-enter menu option: ")
