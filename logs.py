from datetime import datetime

def registrar_log(usuario, acao):
    data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    with open("logs.txt", "a", encoding = "utf-8") as arquivo:
        arquivo.write(f"[{data_hora}] Usuário: {usuario} | {acao}\n")
