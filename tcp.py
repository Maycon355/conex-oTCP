import socket
import sys



def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

    except socket.error as error:
        print ("Erro na ao conectar")
        print ("ERRO {}".format(error))
        sys.exit()
        print("Socket criado com sucesso!!!")

    HostAlvo = input ("Digite o host ou IP a ser conectado: ")
    portAlvo = input ("Digite também a PORTA a ser conectada: ")


    try: 
        s.connect((HostAlvo, int (portAlvo)))
        print("Cliente TCP conectado com sucesso!!! " + HostAlvo + " Na Porta: " + portAlvo)
        s.shutdown(2)

    except socket.error as error:
        print("Não foi possivel conectar no Host: " + HostAlvo + " Na Porta: ", portAlvo)
        print("Error: {}".format(error))
        sys.exit()

if __name__ == "__main__":
    main ()
