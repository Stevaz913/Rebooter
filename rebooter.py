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

print('Current values:')
print ('A1: ' + parser.get('A1', 'reboot'))
print ('A2: ' + parser.get('A2', 'reboot'))
print ('A3: ' + parser.get('A3', 'reboot'))
print ('B1: ' + parser.get('B1', 'reboot'))
print ('B2: ' + parser.get('B2', 'reboot'))
print ('')

parser.set('A1', 'reboot', 'False')
parser.set('A2', 'reboot', 'False')
parser.set('A3', 'reboot', 'False')
parser.set('B1', 'reboot', 'False')
parser.set('B2', 'reboot', 'False')

with open('rebooter.cfg', 'wb') as configfile:
    parser.write(configfile)