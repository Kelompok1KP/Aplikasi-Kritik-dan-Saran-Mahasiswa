import lib #memanggil file lib.py
print ("==============================================================================")

pilihan = 1
while (pilihan < 4):
	pilihan = lib.option()
	print(pilihan)
	if pilihan == 1:
		lib.oldUser()
	elif pilihan == 2:
		lib.newUser()
	elif pilihan == 3:
		lib.read()
		break
	elif pilihan == 4:
		break	
	