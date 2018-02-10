import rebooter
import rball
import os
import sys
import time
import urllib, json, requests
import textwrap

def mineStatus():
	ret = urllib2.urlopen(urllib2.Request('http://vega07.ethosdistro.com/?json=yes'))
	data = json.loads(ret.read())
	a1stat = data['rigs']['5026ef']['condition']
	a2stat = data['rigs']['50270d']['condition']
	a3stat = data['rigs']['482892']['condition']
	b1stat = data['rigs']['502b8a']['condition']
	b2stat = data['rigs']['590b29']['condition']

while True:
	os.system('clear')
	print("----------------------------------")
	print("|------ REBOOT BOX v0.0.10 ------|")
	print("|--------------------------------|")
	print("| A1 Status: " + str(a1stat) + "         |")
	print("| A2 Status: " + str(a2stat) + "         |")
	print("| A3 Status: " + str(a3stat) + "         |")
	print("| B1 Status: " + str(b1stat) + "         |")
	print("| B2 Status: " + str(b2stat) + "         |")
	print("|                                |")
	print("|   Commands are A1, A2, etc.    |")
	print("| 'All' to reboot all, Q to quit |")
	print("----------------------------------")
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
		mineStatus()

	else:
		print("")
		print("     " + str(rig) + ' is not a valid command')
		time.sleep(3)
