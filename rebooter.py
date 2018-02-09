from ConfigParser import SafeConfigParser
import time
import sys

CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'

parser = SafeConfigParser()
parser.read('rebooter.cfg')

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

testime = 30

while testime > 0:
	parser.set('A1', 'reboot', 'False')
	with open('rebooter.cfg', 'wb') as configfile:
		parser.write(configfile)
	print('waiting' + testtime + ' seconds')
	time.sleep(1)

testime = 10
print('Sending Reboot')

parser.set('A1', 'reboot', 'True')
with open('rebooter.cfg', 'wb') as configfile:
	parser.write(configfile)

while testime > 0:
	print('Rebooting...' + testime + 'seconds remain')
	time.sleep(1)

parser.set('A1', 'reboot', 'False')
with open('rebooter.cfg', 'wb') as configfile:
	parser.write(configfile)