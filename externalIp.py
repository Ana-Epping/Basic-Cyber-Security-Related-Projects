import re
import json
from urllib.request import urlopen

url = "https://ipinfo.io/json"

answer = urlopen(url)

data = json.load(answer)

ip = data['ip']
org = data['org']
city = data['city']
country = data['country']
region = data['country']

print("Detalhes do IP externo\n")
print('IP: {4}\nRegião: {1}\nPaís: {2}\nCidade: {3}\nOrg.: {0}'.format(org, region, country, city, ip))