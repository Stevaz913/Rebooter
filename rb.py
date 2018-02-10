import rebooter
import rball
import os
import sys
import time
import urllib, urllib2, json, requests
import textwrap
import string
import random

def minerStatus(rig):
	status = str(data['rigs'][rig]['condition'])
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
	status = str(data['rigs'][rig]['miner_instance'])
	return status

def print_slow(typeout):
    for letter in typeout:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(random.randrange(0.05, 0.1))

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
	
	riggo = raw_input("====>  Panel Command: ")
	rig = riggo.upper()
	
	if rig == 'A1' or rig == 'A2' or rig == 'A3' or rig == 'B1' or rig == 'B2':
		rebooter.rebme(rig)
	
	elif rig == 'Q':
		print('Exiting...')
		sys.exit(0)
	
	elif rig == 'ALL':
		rball.rbooter()
	
	elif rig == 'DADJOKE':
		response = requests.get("https://icanhazdadjoke.com/",
  		  headers={
    	    "Accept": "application/json"
  		  }
		)
		print textwrap.fill(response.json()['joke'], 40)
		print('')
		raw_input("Press enter to return...")

	elif rig == 'STATS':
		ret = urllib2.urlopen(urllib2.Request('http://vega07.ethosdistro.com/?json=yes'))
		data = json.loads(ret.read())
		minerStatus('5026ef')
		minerStatus('50270d')
		minerStatus('482892')
		minerStatus('502b8a')
		minerStatus('590b29')
		minerGPUs('5026ef')
		minerGPUs('50270d')
		minerGPUs('482892')
		minerGPUs('502b8a')
		minerGPUs('590b29')
		print('Updating miner stats....')
		time.sleep(1)
		print('Done')
		time.sleep(0.2)

	else:
		sys.stdout.write("        ")
		sys.stdout.flush()
		print_slow("Ah ah ah!  You didn't say the magic word!")
		print("")
		time.sleep(1)
		print("      ('" + str(riggo) + "' is not a valid command)")
		time.sleep(3)