import requests
import json
curr = 1
def updateInfo():
	myUrl = "https://dweet.io/get/latest/dweet/for/" + serv
	myDat = requests.get(myUrl)
	thisJson = json.loads(myDat.text)
	try:
		myMess= thisJson["with"][0]["content"]["myData"]
	except:
		pass
	try:
		return myMess
	except:
		pass
print("Welcome to Dweety Reciever")
serv = input("Enter a Nest to Join: ")
print("Connected!")
while(True):
	if curr == 1:
		lastOp = updateInfo()
		curr = curr + 1
	currOp = updateInfo()
	if(currOp == None):
		pass
	else:
		if(lastOp == currOp):
			pass
		else:
			print(currOp)
		lastOp = currOp

	

	
		
		
