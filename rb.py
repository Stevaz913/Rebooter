import rebooter
import rball
import os
import sys
import time
import urllib, urllib2, json, requests
import textwrap

ret = urllib2.urlopen(urllib2.Request('http://vega07.ethosdistro.com/?json=yes'))
data = json.loads(ret.read())

a1stat = data['rigs']['5026ef']['condition']
a2stat = data['rigs']['50270d']['condition']
a3stat = data['rigs']['482892']['condition']
b1stat = data['rigs']['502b8a']['condition']
b2stat = data['rigs']['590b29']['condition']

a1gpu = data['rigs']['5026ef']['gpus']
a2gpu = data['rigs']['50270d']['gpus']
a3gpu = data['rigs']['482892']['gpus']
b1gpu = data['rigs']['502b8a']['gpus']
b2gpu = data['rigs']['590b29']['gpus']

while True:
	os.system('clear')
	print("---------------------------------------------")
	print("|------------ REBOOT BOX v0.0.11 -----------|")
	print("|-------------------------------------------|")
	print("|                                           |")
	print("|    A1 Status: " + str(a1stat) + " | " + str(a1gpu) + "/7 GPUs Running   |")
	print("|    A2 Status: " + str(a2stat) + " | " + str(a2gpu) + "/7 GPUs Running   |")
	print("|    A3 Status: " + str(a3stat) + " | " + str(a3gpu) + "/9 GPUs Running   |")
	print("|    B1 Status: " + str(b1stat) + " | " + str(b1gpu) + "/9 GPUs Running   |")
	print("|    B2 Status: " + str(b2stat) + " | " + str(b2gpu) + "/8 GPUs Running   |")
	print("|                                           |")
	print("|          Commands are A1, A2, etc.        |")
	print("|       'stats' to update miner status      |")
	print("|       'All' to reboot all, Q to quit      |")
	print("---------------------------------------------")
	print("")
	
	rig = raw_input("====>  Reboot command: ")
	
	if rig == 'A1' or rig == 'A2' or rig == 'A3' or rig == 'B1' or rig == 'B2':
		rebooter.rebme(rig)
	
	elif rig == 'Q' or rig == 'q':
		print('Exiting...')
		sys.exit(0)
	
	elif rig == 'All':
		rball.rbooter()
	
	elif rig == 'dadjoke':
		response = requests.get("https://icanhazdadjoke.com/",
  		  headers={
    	    "Accept": "application/json"
  		  }
		)
		print textwrap.fill(response.json()['joke'], 40)
		print('')
		raw_input("Press enter to return...")

	elif rig == 'stats':
		ret = urllib2.urlopen(urllib2.Request('http://vega07.ethosdistro.com/?json=yes'))
		data = json.loads(ret.read())
		a1stat = data['rigs']['5026ef']['condition']
		a2stat = data['rigs']['50270d']['condition']
		a3stat = data['rigs']['482892']['condition']
		b1stat = data['rigs']['502b8a']['condition']
		b2stat = data['rigs']['590b29']['condition']
		a1gpu = data['rigs']['5026ef']['gpus']
		a2gpu = data['rigs']['50270d']['gpus']
		a3gpu = data['rigs']['482892']['gpus']
		b1gpu = data['rigs']['502b8a']['gpus']
		b2gpu = data['rigs']['590b29']['gpus']
		print('Updating miner stats....')
		time.sleep(1)
		print('Done')
		time.sleep(0.2)

	else:
		print("")
		print("     " + str(rig) + ' is not a valid command')
		time.sleep(3)
