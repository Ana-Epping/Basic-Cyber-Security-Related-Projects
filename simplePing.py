import os

print("#" * 60)

ip_host = input("Digite o ip ou host a ser verificado: ")

print("-" * 60)

os.system("ping -n 6 {}" .format(ip_host))
