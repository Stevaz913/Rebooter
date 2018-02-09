import rebooter
import rball

print("----------------------------------")
print("---- REBOOT BOX v0.0.00000001 ----")
print("----------------------------------")
print("")
print("Commands are A1, A2, etc.")
print("'All' to reboot all, Q to quit")

while True:
	rig = raw_input("====>  Reboot command: ")
	if rig == 'A1' or 'A2' or 'A3' or 'B1' or 'B2':
		rebooter.rebme(rig)
	elif rig == 'Q' or 'q':
		print('Exiting...')
		sys.exit(0)
	elif rig == 'All':
		rball.rbooter()
	else:
		print(str(rig) + 'not a valid command')
		print('')
