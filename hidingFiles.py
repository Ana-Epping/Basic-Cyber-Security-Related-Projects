import ctypes

pasta = input("Digite o caminho da pasta a ser ocultada: ")

attribute_hide = 0x02

returning = ctypes.windll.kernel32.SetFileAttributesW(pasta, attribute_hide)

if returning:
    print("Arquivo foi ocultado")
else:
    print("Arquivo não foi ocultado")