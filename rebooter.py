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
	time.sleep(2)
	parser.set(rig, 'reboot', 'False')
	with open(d + 'rebooter.cfg', 'wb') as configfile:
		parser.write(configfile)