import rebooter
import rball
import os
import sys

while True:
	os.system('clear')
	print("----------------------------------")
	print("|------ REBOOT BOX v0.0.10 ------|")
	print("|--------------------------------|")
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
	else:
		print(str(rig) + 'not a valid command')
		print('')
