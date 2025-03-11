from cryptography.fernet import Fernet

# Gere uma chave e armazene em config.py
CHAVE = b"-6dRwF_oN8dXfeBJcIb6bbp5n3ggEd1MpioiOZ5acyg="

def criptografar_dados(dados):
    cipher_suite = Fernet(CHAVE)
    dados_str = str(dados).encode()
    return cipher_suite.encrypt(dados_str)

def descriptografar_dados(dados_criptografados):
    cipher_suite = Fernet(CHAVE)
    dados_str = cipher_suite.decrypt(dados_criptografados)
    return eval(dados_str.decode())
