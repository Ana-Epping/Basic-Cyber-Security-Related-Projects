import socket
import sys

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e: 
        print("A conexão falhou!")
        print("Erro: {}".format(e))
        sys.exit()

    print("Socket criado com sucesso")

    targetHost = input("Digite o Host ou Ip a ser conectado: ")
    targetPort = input("Digite a porta a ser conectada: ")

    try:
        s.connect((targetHost, int(targetPort)))
        print("Cliente TCP conectado com Sucesso no Host: " + targetHost + " - Porta " + targetPort)
        s.shutdown(2)
    except socket.error as e:
        print("Não foi possível conectar no Host: " + targetHost + " - Porta " + targetPort)
        print("Erro: {}".format(e))
        sys.exit()

if __name__ == "__main__":
    main()