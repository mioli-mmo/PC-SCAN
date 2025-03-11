import socket
from threading import Thread
from .computador import Computador
from .utils import descriptografar_dados

class Servidor:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.clientes = []

    def iniciar(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            s.listen()
            print(f"Servidor ouvindo em {self.host}:{self.port}")
            while True:
                conn, addr = s.accept()
                cliente_thread = Thread(target=self.tratar_cliente, args=(conn, addr))
                cliente_thread.start()

    def tratar_cliente(self, conn, addr):
        print(f"Conexão recebida de {addr}")
        dados_criptografados = conn.recv(1024)
        print(f"Dados recebidos do cliente.")
        dados = descriptografar_dados(dados_criptografados)

        processadores, ram_livre_gb, disco_livre_gb = dados

        print(f"Dados descriptografados: \n Processadores = {processadores} \n RAM livre = {ram_livre_gb:.2f} GB \n Disco livre = {disco_livre_gb:.2f} GB")
        computador = Computador(addr[0], *dados)
        self.clientes.append(computador)
        print(f"Computador {addr[-1]} adicionado à lista.")
        conn.close()
