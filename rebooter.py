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
	testime = 10
	print('Sending Reboot to ' + rig)

	parser.set(rig, 'reboot', 'True')
	with open(d + 'rebooter.cfg', 'wb') as configfile:
		parser.write(configfile)

	while testime > 0:
		print(str(rig) + ' Rebooting... ' + str(testime))
		testime -= 1
		delete_last_lines(1)
		time.sleep(1)

	print(str(rig) + ' Rebooted')
	parser.set(rig, 'reboot', 'False')
	with open(d + 'rebooter.cfg', 'wb') as configfile:
		parser.write(configfile)