from genie.testbed import load

tb = load('testbed.yml') #loads the testbed file
dev = tb.devices['R1'] # creates an object for the device R1 from the testbed file
dev.connect() #Connects to R1 and displays connection details
exit() #Exits the programme