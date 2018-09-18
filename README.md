# Dweety
The simplest possible chat room built using Python 3 and the dweet.io api! 

## Installation
1. Make sure you have the latest version of Python 3
2. Clone this repo into your directory and your done! No extra dependencies or installations needed!

## Running the Programs
Due to my limited coding abilities you must have 2 programs running at the same time: 
  - The Chat Receiver
  - The Message Sender

The Chat Reciever retrieves the data that others have sent,
while the Message Sender sends your message to the server! 

### To Run on Linux (Ubuntu 18.04 Tested)
Open up two Terminals:

Terminal 1:
- `cd Dweety` or whatever the directory is named.
- `python3 DweetClient_sender.py`

Terminal 2:
- `cd Dweety`
- `python3 DweetClient_receiver.py`

### To Run on Mac (macOs Sierra Tested) and Windows (Not Tested)
Make sure Python 3 IDLE is installed.
Open up two instances of IDLE 3,

On the first instance:
1. Go To `File` and then `Open` and from there choose DweetClient_sender.py in your directory.
2. Run the file by pressing `F5` or run from the dropdown menu

On the second instance:
1. Go To `File` and then `Open` and from there choose DweetClient_reciever.py in your directory.
2. Run that file by pressing `F5` or run from the dropdown menu


## Usage
On The sender program type in a Username (A display name) in the `Username: ` prompt.
Then type in a message you would like to send and press enter!
In a few seconds you will see your Username followed by your message on Receiver Program!
And if people are online then they will see your message too on their Receiver.

## Improvements
By no means is this project finished, there are many things I would like to see done with this project:
- Combining the two programs into one perhaps using multithreading?
- Ability to join different chat servers - Coming Soon!
- Encrypted Data Transmission
- A GUI version for those who fear the terminal
If you have any Ideas, Let me know in the comments!

## Liscensing
This project is liscensed under the GNU GPLv3 Liscense 
which means you have the freedom to do whatever you want with this file! 
As a matter of fact it is encouraged that you modify and make it the way you like!

## Change Log
> 1.0.0: Initial Release
