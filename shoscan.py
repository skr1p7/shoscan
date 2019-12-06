import shodan
import sys
import os

class colors:
    GREEN = '\033[92m'
    STOP = '\033[0m'
    RED='\033[31m'

priv_key = str(raw_input("Enter you Shodan API key > "))
if not priv_key:
	print colors.RED + ("You have not entered you API Key")
	print ("Exiting the code...") + colors.STOP
	sys.exit()
else:
	pass

api = shodan.Shodan(priv_key)

print colors.RED +  " _____  _             _____                    "
print "/  ___|| |           /  ___|                   "
print "\ `--. | |__    ___  \ `--.   ___  __ _  _ __  "
print "`--. \ | '_ \  / _ \  `--. \ / __|/ _` || '_ \ "
print "/\__/ /| | | || (_) |/\__/ /| (__| (_| || | | |"
print "\____/ |_| |_| \___/ \____/  \___|\__,_||_| |_|" + colors.STOP
                                               
                                               
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
	print "-"*50
	print colors.GREEN + "IP: %s"%info["ip_str"] + colors.STOP
	print "Hostnames:\n"
	for i in info["hostnames"]:
			print ("  [+] %s\n"%str(i))
	print "Organization: %s"%info.get("org", "n/a")
	print "Operating System: %s"%info.get("os", "n/a")
	print "Latitude: %s"%info["latitude"]
	print "Longitude: %s"%info["longitude"]
	print "City: %s"%info["city"]
	print "-"*50

		

def search_func():
	query = str(raw_input("query > "))
	res = api.search(query)
	for service in res['matches']:
		print service['ip_str'] + '   |   ' + str(service['port']) + '   |   ' + str(service['org'])

def ip():
	ip = os.system('shodan myip')
	print (ip)

menu()
