import shodan
SHODAN_API_KEY = 'gNvShBAZ2FKUvHJlt2cmjCXnfDgVybV7'

api = shodan.Shodan(SHODAN_API_KEY)
info = api.host('104.237.143.20' , history=True)

print (info)