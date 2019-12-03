import shodan
import sys
import os
SHODAN_API_KEY = 'gNvShBAZ2FKUvHJlt2cmjCXnfDgVybV7'

api = shodan.Shodan(SHODAN_API_KEY)

def menu():
	print ("1. Host scan")
	print ("2. Search for your query")
	print ("3. My IP")
	print ("0. Exit") 
	select = int(input("Enter choice : "))
	if select==1:
		host_func()
	elif select==2:
		search_func()
	elif select==3:
		ip()
	elif select ==0:
		sys.exit()
	else:
		sys.exit()
		
def host_func():
	h_name = str(raw_input("Enter the host name :"))
	info = api.host(h_name , history=True)
	print (info)

def search_func():
	query = str(raw_input("query > "))
	res = api.search(query)
	for service in res['matches']:
		print service['ip_str'] + '   |   ' + str(service['port']) + '   |   ' + str(service['org'])

def ip():
	ip = os.system('shodan myip')
	print (ip)

menu()