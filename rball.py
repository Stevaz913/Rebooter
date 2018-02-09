import rebooter
import time

i = 60
print("-----------------------------------")
print("----- REBOOT BOX v0.0.00000001 ----")
print("-----------------------------------")
print("")
print("-----  REBOOTING ALL RIGS  --------")


def rbstation(rig):
	i = 60
	rebooter.rebme(rig)
	while i > 0:
		print('Rebooting ' + rig + '...' + i)
		i -= 1
		rebooter.delete_last_lines(1)
		time.sleep(1)

rbstation('A1')
rbstation('A2')
rbstation('A3')
rbstation('B1')
rbstation('B2')

print('All Rebooted Probly - Mint')