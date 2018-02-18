ver = 'v1.0.3'

from ConfigParser import SafeConfigParser
import rebooter
import rball
import os
import sys
import time
import urllib, urllib2, json, requests
import textwrap
import string
import random
import datetime
from slackclient import SlackClient



parser = SafeConfigParser()
parser.read('rb.cfg')
CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'

slack_token = ''
sc = SlackClient(slack_token)

togStr = 'Hash'

def slackmessage(m):
    sc.api_call(
      "chat.postMessage",
      channel="#rigstatus",
      text=m,
      as_user="False",
      username=user,
    )

def delete_last_lines(n=1):
    for _ in range(n):
        sys.stdout.write(CURSOR_UP_ONE)
        sys.stdout.write(ERASE_LINE)

def minerStatus(rig):
	status = str(data['rigs'][rig]['condition'])
	if status == 'mining':
		x = status.replace('mining', 'RUNNING      ')
	elif status == 'stuck_miners':
		x = status.replace('stuck_miners', 'CARD CRASH   ')
	elif status =='just_booted':
		x = status.replace('just_booted', 'BOOTUP (' + str(data['rigs'][rig]['gpus']) + ')   ')
	elif status == 'unreachable':
		x = status.replace('unreachable', 'RIG DOWN     ')
	elif status == 'overheat':
		x = status.replace('overheat', 'OVER-HEAT    ')
	elif status == 'no_hash':
		x = status.replace('no_hash', 'NOT HASHING  ')
	elif status == 'autorebooted':
		x = status.replace('autorebooted', 'AUTO BOOTED  ')
	else:
		x = status
	return x

def minerGPUs(rig):
	status = str(data['rigs'][rig]['miner_instance'])
	return status

def perRigGpu(rig):
	g = str(data['rigs'][rig]['gpus'])
	return g

def print_slow(typeout):
    for letter in typeout:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.045)

def print_slower(typeout):
    for letter in typeout:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.15)

def slicer(rig, start, end):
	if togStr == 'Hash':
		hashData = data['rigs'][rig]['miner_hashes']
	else:
		hashData = data['rigs'][rig]['temp']
	hashSlice = (hashData[start:end])
	if hashSlice == "":
		hashSlice = "     "
	return hashSlice

def hashrateMod(hashrate):
	hr = hashrate
	# hr = int((data['per_info']['claymore']['hash']))
	if hr > 1000:
		x = str(hr) + "  "
	elif hr > 100:
		x = str(hr) + "  -"
	elif hr > 10:
		x = str(hr) + "  --"
	elif hr >= 0:
		x = str(hr) + "  ---"
	return x

def upTime(rig):
	up = int(data['rigs'][rig]['uptime'])
	utime = str(datetime.timedelta(seconds=up))
	if up < 36000:
		x = "          " + utime
	if up >= 36000:
		x = "         " + utime
	if up >= 86400:
		x = "   " + utime
	if up >= 172800:
		x = "  " + utime
	if up >= 864000:
		x = " " + utime
	if up >= 8640000:
		x = utime
	return x

def getNano():
	try:
		account = 'https://api.nanopool.org/v1/eth/balance/0x865f80e37dc3360aacc76d0064c5c1b61639e9c5'
		hdr = { 'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36' }
		req = urllib2.Request(account, None, hdr)
		html = urllib2.urlopen(req).read()
		data = json.loads(html)
		roundVal = '%.9f' % data['data']
		return roundVal
	except Exception as e:
		print e
		sleep.time(2)

while True:
	os.system('clear')
	print("    ---------------------------------------------")
	print("   |-----------  RIG PANEL " + ver + "  --------------|")
	print("    ---------------------------------------------")
	print("")
	print("    Enter User Number:")
	print("    [1] Freak")
	print("    [2] Weeze")
	print("")
	uin = raw_input("====> ")

	if uin == '1':
		user = 'Freak'
		break
	elif uin == '2':
		user = 'Weeze'
		break
	else:
		print('    Enter 1 or 2')
		time.sleep(2)

idlecount = 0
nidle = 10
idle = 600
rig = ''
riggo = ''
rtime = nidle
status = '(active)'

def userStatUpdate(userName, status):
	if userName == 'Freak':
		parser.set('fstatus', 'online', status)
		with open('rb.cfg', 'wb') as configfile:
			parser.write(configfile)
	else:
		parser.set('wstatus', 'online', status)
		with open('rb.cfg', 'wb') as configfile:
			parser.write(configfile)

nanBal = getNano()

while True:
	try:
		if user == 'Freak':
			iduser = 'Weeze'
			userStatus = parser.get('wstatus', 'online')
		else:
			iduser = 'Freak'
			userStatus = parser.get('fstatus', 'online')

		if status == '(active)':
			userStatUpdate(user, '_ACTIVE')
		elif status == '(idle)  ':
			userStatUpdate(user, '___IDLE')
		else:
			userStatUpdate(user, 'OFFLINE')

		os.system('clear')
		ret = urllib2.urlopen(urllib2.Request('http://vega07.ethosdistro.com/?json=yes'))
		data = json.loads(ret.read())
		hashrate = int((data['per_info']['claymore']['hash']))
		print("    ---------------------------------------------------")
		print("   |---------------  RIG PANEL " + ver + "  ----------------|")
		print("    -------------------  HR: " + str(hashrateMod(hashrate)) + "--------------------")
		print("    |            Logged in as " + user + " " + status + "          |")
		print("    |                                                 |")
		print("    |  A1: " + minerStatus('5026ef') + "| " + minerGPUs('5026ef') + "/7 GPU | " + upTime('5026ef') + " |")
		print("    |  A2: " + minerStatus('50270d') + "| " + minerGPUs('50270d') + "/9 GPU | " + upTime('50270d') + " |")
		print("    |  A3: " + minerStatus('482892') + "| " + minerGPUs('482892') + "/9 GPU | " + upTime('482892') + " |")
		print("    |  B1: " + minerStatus('502b8a') + "| " + minerGPUs('502b8a') + "/9 GPU | " + upTime('502b8a') + " |")
		print("    |  B2: " + minerStatus('590b29') + "| " + minerGPUs('590b29') + "/8 GPU | " + upTime('590b29') + " |")
		print("    ---------------------------------------------------")
		print("    | A1 " + togStr + " | A2 " + togStr + " | A3 " + togStr + " | B1 " + togStr + " | B2 " + togStr + " |")
		print("    |  " + slicer('5026ef', 0, 5)  + "     "  + slicer('50270d', 0, 5) + "     " + slicer('482892', 0, 5) + "     " + slicer('502b8a', 0, 5) + "     " + slicer('590b29', 0, 5) + "  |")
		print("    |  " + slicer('5026ef', 6, 11)  + "     "  + slicer('50270d', 6, 11) + "     " + slicer('482892', 6, 11) + "     " + slicer('502b8a', 6, 11) + "     " + slicer('590b29', 6, 11) + "  |")
		print("    |  " + slicer('5026ef', 12, 17)  + "     "  + slicer('50270d', 12, 17) + "     " + slicer('482892', 12, 17) + "     " + slicer('502b8a', 12, 17) + "     " + slicer('590b29', 12, 17) + "  |")
		print("    |  " + slicer('5026ef', 18, 23)  + "     "  + slicer('50270d', 18, 23) + "     " + slicer('482892', 18, 23) + "     " + slicer('502b8a', 18, 23) + "     " + slicer('590b29', 18, 23) + "  |")
		print("    |  " + slicer('5026ef', 24, 29)  + "     "  + slicer('50270d', 24, 29) + "     " + slicer('482892', 24, 29) + "     " + slicer('502b8a', 24, 29) + "     " + slicer('590b29', 24, 29) + "  |")
		print("    |  " + slicer('5026ef', 30, 35)  + "     "  + slicer('50270d', 30, 35) + "     " + slicer('482892', 30, 35) + "     " + slicer('502b8a', 30, 35) + "     " + slicer('590b29', 30, 35) + "  |")
		print("    |  " + slicer('5026ef', 36, 41)  + "     "  + slicer('50270d', 36, 41) + "     " + slicer('482892', 36, 41) + "     " + slicer('502b8a', 36, 41) + "     " + slicer('590b29', 36, 41) + "  |")
		print("    |  " + slicer('5026ef', 42, 47)  + "     "  + slicer('50270d', 42, 47) + "     " + slicer('482892', 42, 47) + "     " + slicer('502b8a', 42, 47) + "     " + slicer('590b29', 42, 47) + "  |")
		print("    |  " + slicer('5026ef', 48, 53)  + "     "  + slicer('50270d', 48, 53) + "     " + slicer('482892', 48, 53) + "     " + slicer('502b8a', 48, 53) + "     " + slicer('590b29', 48, 53) + "  |")
		print("    ---------------------------------------------------")
		print("    | Nanopool Balance: " + nanBal + "  Ethereums        |")	
		print("    ---------------------------------------------------")			
		while rtime >= 0:
			print("    |  Input: ctrl + c  | " + str(datetime.timedelta(seconds=rtime)) + " |  " + iduser + ": " + userStatus + "   |")
			print("    ---------------------------------------------------")
			delete_last_lines(2)
			time.sleep(1)
			rtime -= 1

	except KeyboardInterrupt:
		idlecount = 0
		status = "(active)"
		print("    \| [a1]... : Reboot Single Rig               |/")
		print("       | [all]   : Reboot all rigs                 |")
		print("       | [t]     : Toggle Hash/Temp in panel       |")
		print("       | [s]     : Send slack message              |")
		print("       | [n]     : Update Nanopool Balance         |")
		print("       | [q]     : Quit back to terminal           |")
		print("       | ENTER (no command) for manual update      |")
		print("       ---------------------------------------------")
		riggo = raw_input("====>  Panel Command: ")
		rig = riggo.upper()
	
		if rig == 'A1' or rig == 'A2' or rig == 'A3' or rig == 'B1' or rig == 'B2':
			s = raw_input('Send message to slack channel? (y/n) ')
			if s == 'y':
				q = raw_input('Enter message (Leave blank for a generic): ')
				if q != '':
					slackmessage("Rebooting " + rig + " - " + q)
				else:
					slackmessage("Rebooting " + rig)
			rebooter.rebme(rig)
	
		elif rig == 'Q':
			print('Exiting...')
			userStatUpdate(user, "OFFLINE")
			sys.exit(0)

		elif rig == "T":
			if togStr == 'Hash':
				togStr = 'Temp'
			else:
				togStr = 'Hash'

		elif rig == 'N':
			nanBal = getNano()
	
		elif rig == 'ALL':
			s = raw_input('Send message to slack channel? (y/n) ')
			if s == 'y':
				q = raw_input('Enter message (Leave blank for a generic): ')
				if q != '':
					slackmessage(q)
				else:
					slackmessage("Rebooting ALL")
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

		elif rig == 'ACCESS MAIN PROGRAMMING':
			sys.stdout.write("        ")
			sys.stdout.flush()
			print_slow("Ah ah ah!")
			time.sleep(1.1)
			sys.stdout.write("  ")
			print_slow("You didn't say the magic word!")
			time.sleep(3)

		elif rig == 'S':
			s = raw_input('====> Message: ')
			slackmessage(s)

		elif riggo == '':
			print('')
			sys.stdout.write('     Updating')
			sys.stdout.flush()
			print_slower('.....')

		else:
			print("")
			print("    " + riggo + "ed your mom last night")
			time.sleep(3)

	except Exception as e:
		print e
		time.sleep(2)

	idlecount += 1
	rtime = nidle
	if idlecount >= 30:
		status = "(idle)  "
		rtime = idle
	if idlecount >= 360:
		userStatUpdate(user, 'OFFLINE')