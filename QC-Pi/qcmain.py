#!/usr/bin/env python
import sys
import keyboard
import qcpiDriver

print("Welcome to the QC Automation Appliance.")

print("Main Menu: ")
print("1. Start Workflow")
print("2. Test Network")
print("3. Exit Appliance")

mainselect = input("Enter the number corresponding to the menu item desired: ")
while mainselect > "0":
	if mainselect == "1":
		print("Made it to Cond. 1")
		driver = qcpiDriver.officialDrive()
	elif mainselect == "2":
		print("Made it to Cond. 2")
		copyTest = networkInteraction.newNETAccess()
	elif mainselect == "5":
		print("Made it to Cond. 3")
		sys.exit()
	else:
		print("Menu item entered is incorrect.")
		mainselect = input("Please re-enter menu option: ")
