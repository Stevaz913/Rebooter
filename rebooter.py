from ConfigParser import SafeConfigParser
import time
import sys

CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'

d = '/var/www/html/'

parser = SafeConfigParser()
parser.read(d + 'rebooter.cfg')


def delete_last_lines(n=1):
	for _ in range(n):
		sys.stdout.write(CURSOR_UP_ONE)
		sys.stdout.write(ERASE_LINE)

#print('Current values:')
#print ('A1: ' + parser.get('A1', 'reboot'))
#print ('A2: ' + parser.get('A2', 'reboot'))
#print ('A3: ' + parser.get('A3', 'reboot'))
#print ('B1: ' + parser.get('B1', 'reboot'))
#print ('B2: ' + parser.get('B2', 'reboot'))
#print ('')

def rebme(rig):
	testime = 60
	while testime > 0:
		parser.set(rig, 'reboot', 'False')
		with open(d + 'rebooter.cfg', 'wb') as configfile:
			parser.write(configfile)
		print('waiting ' + str(testime) + ' seconds')
		delete_last_lines(1)
		testime -= 1
		time.sleep(1)

	testime = 10
	print('Sending Reboot')

	parser.set(rig, 'reboot', 'True')
	with open(d + 'rebooter.cfg', 'wb') as configfile:
		parser.write(configfile)

	while testime > 0:
		print('Rebooting...' + str(testime) + 'seconds remain')
		testime -= 1
		delete_last_lines(1)
		time.sleep(1)

	print('Resetting Values to False')
	parser.set(rig, 'reboot', 'False')
	with open(d + 'rebooter.cfg', 'wb') as configfile:
		parser.write(configfile)

rebme('A1')
rebme('A2')
rebme('A3')
rebme('B1')
rebme('B2')