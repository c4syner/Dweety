import requests
import json
import time
def sendInfo():
    myIn = input("Message: ")
    if(myIn == "EXIT"):
        return 9
    url = "https://dweet.io/dweet/for/dweetyserver?myData="+myName+": "+myIn
    thisOut = requests.get(url)
print("Welcome to Dweety (Sender)")
myName = input("Username: ")
while(True):
    myVal = sendInfo()
    if(myVal == 9):
        break

    
        
        
