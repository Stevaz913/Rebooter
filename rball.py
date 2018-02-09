import rebooter
import time

i = 60
print("-----------------------------------")
print("----- REBOOT BOX v0.0.00000001 ----")
print("-----------------------------------")
print("")
print("-----  REBOOTING ALL RIGS  --------")


while i > 0:
	print('Rebooting A1...' + i)
	i -= 1
rebooter.rebme(A1)
time.sleep(60)
i = 60

while i > 0:
	print('Rebooting A2...' + i)
	i -= 1
rebooter.rebme(A2)
time.sleep(60)
i = 60

while i > 0:
	print('Rebooting A3...' + i)
	i -= 1
rebooter.rebme(A3)
time.sleep(60)
i = 60

while i > 0:
	print('Rebooting B1...' + i)
	i -= 1
rebooter.rebme(B1)
time.sleep(60)
i = 60

while i > 0:
	print('Rebooting B2...' + i)
	i -= 1
rebooter.rebme(B2)
time.sleep(60)
i = 60

print('All Rebooted Probly')