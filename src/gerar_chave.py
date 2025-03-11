from cryptography.fernet import Fernet

# Gera uma chave
chave = Fernet.generate_key()

# Exibe a chave gerada
print("Chave gerada:", chave.decode())

# Salva a chave em um arquivo (opcional)
with open("chave.txt", "wb") as arquivo_chave:
    arquivo_chave.write(chave)
