import ipaddress

#ip = '192.168.0.1'
ip = '192.168.0.1/24'

network = ipaddress.ip_network(ip, strict=False)

#address = ipaddress.ip_address(ip)
#address = ipaddress.ip_network(ip)

for ip in network: 
    print(ip)
