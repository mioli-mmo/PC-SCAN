from src.servidor import Servidor
from src.cliente import Cliente
from config.config import SERVIDOR_IP, SERVIDOR_PORTA

if __name__ == "__main__":
    modo = input("Iniciar como servidor (s) ou cliente (c)? ")
    if modo == "s":
        servidor = Servidor(SERVIDOR_IP, SERVIDOR_PORTA)
        servidor.iniciar()
    elif modo == "c":
        cliente = Cliente(SERVIDOR_IP, SERVIDOR_PORTA)
        cliente.enviar_dados()
    else:
        print("Modo inválido.")
