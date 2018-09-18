import requests
import json
import time
def sendInfo():
    myIn = input("Message: ")
    if(myIn == EXIT):
        
    url = "https://dweet.io/dweet/for/c4syner?myData="+myName+": "+myIn
    thisOut = requests.get(url)
print("Welcome to Dweety (Sender)")
myName = input("Username: ")
while(True):
    sendInfo()

    
        
        
