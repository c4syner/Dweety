import requests
import json
import time
curr = 1
def updateInfo():
	myUrl = "https://dweet.io/get/latest/dweet/for/" + serv
	myDat = requests.get(myUrl)
	time.sleep(2)
	thisJson = json.loads(myDat.text)
	try:
		myMess= thisJson["with"][0]["content"]["myData"]
	except:
		goodMeat = 1
	try:
		return myMess
	except:
		coolStuffBEan = 9
print("Welcome to Dweety Reciever")
serv = input("Enter a Nest to Join: ")
print("Connected!")
while(True):
	if curr == 1:
		lastOp = updateInfo()
		curr = curr + 1
	currOp = updateInfo()
	if(currOp == None):
		HiGoodFood = 20
	else:
		if(lastOp == currOp):
			Rekt = 20
		else:
			print(currOp)
		lastOp = currOp

	

	
		
		
