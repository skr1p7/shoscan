def menu():
	print ("1. Host scan :")
	select = int(input("Enter choice "))
	if select==1:
		host_func()
	else:
		print ('main menu')