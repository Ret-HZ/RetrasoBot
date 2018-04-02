import socket
import string
import datetime
import time
import win32api
import win32con
from Settings import HOST, PORT, PASS, BOTNAME, CHANNEL, KEYMAPS, ALLOW_REMOTE_SHUTDOWN, REMOTE_SHUTDOWN_PASSWORD, HELP

def openSocket():
	
	s = socket.socket()
	s.connect((HOST, PORT))
	s.send("PASS " + PASS + "\r\n")
	s.send("NICK " + BOTNAME + "\r\n")
	s.send("JOIN #" + CHANNEL + "\r\n")
	return s
	
def sendMessage(s, message):
	messageTemp = "PRIVMSG #" + CHANNEL + " :" + message
	s.send(messageTemp + "\r\n")
	print("Sent: " + messageTemp)

def joinRoom(s):
	readbuffer = ""
	Loading = True
	while Loading:
		readbuffer = readbuffer + s.recv(1024)
		temp = string.split(readbuffer, "\n")
		readbuffer = temp.pop()
		
		for line in temp:
			print(line)
			Loading = loadingComplete(line)
	sendMessage(s, "/me is here!")
	
def loadingComplete(line):
	if("End of /NAMES list" in line):
		return False
	else:
		return True

def getUser(line):
	separate = line.split(":", 2)
	user = separate[1].split("!", 1)[0]
	return user

def getMessage(line):
	separate = line.split(":", 2)
	message = separate[2]
	return message

def isButtonValid(button):
	return button in KEYMAPS().keymap.keys()

def buttonPush(button):
	win32api.keybd_event(KEYMAPS().keymap.get(button,"None"),0,0,0)
	time.sleep(0.20)
	win32api.keybd_event(KEYMAPS().keymap.get(button,"None"),0, win32con.KEYEVENTF_KEYUP, 0)
	print ">>> Pressing " + button.upper()
	

print """
  _____      _                       ____        _   
 |  __ \    | |                     |  _ \      | |  
 | |__) |___| |_ _ __ __ _ ___  ___ | |_) | ___ | |_ 
 |  _  // _ \ __| '__/ _` / __|/ _ \|  _ < / _ \| __|
 | | \ \  __/ |_| | | (_| \__ \ (_) | |_) | (_) | |_ 
 |_|  \_\___|\__|_|  \__,_|___/\___/|____/ \___/ \__|   v1.0
 
"""
print "The selected channel is: " + CHANNEL +"\n"
s=openSocket()
joinRoom(s)
readbuffer = ""

while True:
		readbuffer = readbuffer + s.recv(1024)
		temp = string.split(readbuffer, "\n")
		readbuffer = temp.pop()
		
		for line in temp:
			if "PING :tmi.twitch.tv" in line: #Send PONG to Twitch to avoid a disconnection
				print(line)
				s.send("PONG\r\n")
				print "PONG sent to tmi.twitch.tv at " + datetime.datetime.now().strftime("%I:%M:%S")
				break
			user = getUser(line)
			message = getMessage(line)
			print datetime.datetime.now().strftime("%I:%M:%S") + " | " + user + " typed: " + message

			#PING
			if "!ping" in message:
				sendMessage(s, "PONG")
			
			#HELP
			if "!help" in message:
				sendMessage(s, HELP)
			
			#REMOTE SHUTDOWN
			if ALLOW_REMOTE_SHUTDOWN.lower() == "true" and REMOTE_SHUTDOWN_PASSWORD in message:
				sendMessage(s, "/me is shutting down...")
				quit()
			
			#KEY PRESS
			tempbutton = message.lower()
			button = tempbutton.replace("\r","") #Twitch adds \r at the end of each message so we remove that to match the key names
			if isButtonValid(button):
				buttonPush(button)

			break