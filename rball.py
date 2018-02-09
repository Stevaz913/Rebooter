import rebooter
import time

def rbstation(rig):
	i = 60
	rebooter.rebme(rig)
	while i > 0:
		print('Waiting... ' + str(i))
		i -= 1
		rebooter.delete_last_lines(1)
		time.sleep(1)

def rbooter():
	rbstation('A1')
	rbstation('A2')
	rbstation('A3')
	rbstation('B1')
	rbstation('B2')
	print('Full Reboot Complete')
	time.sleep(3)