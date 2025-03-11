import socket
import psutil
from .utils import criptografar_dados

class Cliente:
    def __init__(self, servidor_host, servidor_port):
        self.servidor_host = servidor_host
        self.servidor_port = servidor_port

    def coletar_dados(self):
        processadores = psutil.cpu_count(logical=True)
        ram_livre_bytes = psutil.virtual_memory().available
        disco_livre_bytes = psutil.disk_usage('/').free
        
        ram_livre_gb = ram_livre_bytes / (1024 ** 3)
        disco_livre_gb = disco_livre_bytes / (1024 ** 3)
        
        return processadores, ram_livre_gb, disco_livre_gb

    def enviar_dados(self):
        dados = self.coletar_dados()
        processadores, ram_livre_gb, disco_livre_gb = dados
        print(f"Dados coletados: \n Processadores = {processadores} \n RAM livre = {ram_livre_gb:.2f} GB \n Disco livre = {disco_livre_gb:.2f} GB")
        dados_criptografados = criptografar_dados(dados)
        print("Dados criptografados e enviados ao servidor.")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.servidor_host, self.servidor_port))
            s.sendall(dados_criptografados)
            print("Dados enviados com sucesso!")
