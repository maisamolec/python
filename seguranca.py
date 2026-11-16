import hashlib, re
from cryptography.fernet import Fernet

def gerar_hash(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

def criar_chave():
    try:
        with open("chave.key", "rb") as arquivo:
            chave = arquivo.read()
    except FileNotFoundError:
        chave = Fernet.generate_key()
        with open("chave.key", "wb") as arquivo:
            arquivo.write(chave)
    return chave

chave = criar_chave()
criptografia = Fernet(chave)

def criptografar(texto):
    return criptografia.encrypt(texto.encode()).decode()

def descriptografar(texto):
    return criptografia.decrypt(texto.encode()).decode()

def validar_email(email):
    padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(padrao, email)

def validar_senha(senha):
    if len(senha) < 8:
        return False
    if not any(c.isupper() for c in senha):
        return False
    if not any(c.islower() for c in senha):
        return False
    if not any(c.isdigit() for c in senha):
        return False
    especiais = "!@#$%&*?"
    if not any(c in especiais for c in senha):
        return False
    return True
