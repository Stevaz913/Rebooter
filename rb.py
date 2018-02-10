import rebooter
import rball
import os
import sys
import time
import urllib, urllib2, json, requests
import textwrap
import string

def minerStatus(rig):
	status = data['rigs'][rig]['condition']
	if status == 'mining':
		x = status.replace('mining', 'OK      ')
	elif status == 'stuck_miners':
		x = status.replace('stuck_miners', 'STUCK   ')
	elif status =='just_booted':
		x = status.replace('just_booted', 'BOOTUP  ')
	else:
		x = status
	return x

def minerGPUs(rig):
	status = data['rigs'][rig]['miner_instance']
	return status

while True:
	ret = urllib2.urlopen(urllib2.Request('http://vega07.ethosdistro.com/?json=yes'))
	data = json.loads(ret.read())
	os.system('clear')
	print("---------------------------------------------")
	print("|------------ RIG PANEL v0.1.03  -----------|")
	print("|-------------------------------------------|")
	print("|                                           |")
	print("|  A1 Status: " + minerStatus('5026ef') + "|  " + minerGPUs('5026ef') + "/7 GPUs Running   |")
	print("|  A2 Status: " + minerStatus('50270d') + "|  " + minerGPUs('50270d') + "/7 GPUs Running   |")
	print("|  A3 Status: " + minerStatus('482892') + "|  " + minerGPUs('482892') + "/9 GPUs Running   |")
	print("|  B1 Status: " + minerStatus('502b8a') + "|  " + minerGPUs('502b8a') + "/9 GPUs Running   |")
	print("|  B2 Status: " + minerStatus('590b29') + "|  " + minerGPUs('590b29') + "/8 GPUs Running   |")
	print("|                                           |")
	print("|      Reboot commands are A1, A2, etc.     |")
	print("|      'stats' to update miner status       |")
	print("|      'All' to reboot all, Q to quit       |")
	print("---------------------------------------------")
	print("")
	
	rig = raw_input("====>  Panel Command: ")
	
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
		a1gpu = data['rigs']['5026ef']['miner_instance']
		a2gpu = data['rigs']['50270d']['miner_instance']
		a3gpu = data['rigs']['482892']['miner_instance']
		b1gpu = data['rigs']['502b8a']['miner_instance']
		b2gpu = data['rigs']['590b29']['miner_instance']
		print('Updating miner stats....')
		time.sleep(1)
		print('Done')
		time.sleep(0.2)

	else:
		print("")
		print("     " + str(rig) + ' is not a valid command')
		time.sleep(3)
