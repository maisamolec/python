import sqlite3
from banco import conectar
from seguranca import gerar_hash, validar_email, validar_senha
from logs import registrar_log

def cadastrar_usuario():
    conexao = conectar()
    cursor = conexao.cursor()

    nome = input("\nNome: ")
    while True:
        email = input("Email: ")
        if validar_email(email):
            break
        print("\n❌ E-mail inválido. Tente novamente.\n")
    while True:
        senha = input("Senha: ")
        if validar_senha(senha):
            break
        print("\n⚠️  Senha fraca."
              "\nA senha deve conter:"
              "\n- Pelo menos 8 caracteres"
              "\n- Letra maiúscula"
              "\n- Letra minúscula"
              "\n- Número"
              "\n- Caractere especial (!@#$%&*?)\n")
    senha = gerar_hash(senha)

    try:
        cursor.execute('''
            INSERT INTO usuarios(nome, email, senha)
            VALUES (?, ?, ?)
        ''', (nome, email, senha))

        conexao.commit()
        print("\n✅ Usuário cadastrado com sucesso!")

    except sqlite3.IntegrityError:
        print("\n⚠️  Esse e-mail já está cadastrado.")

    conexao.close()

def login():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT COUNT(*) FROM usuarios")
    quantidade = cursor.fetchone()[0]

    if quantidade == 0:
        print("\nℹ️ Nenhum usuário cadastrado.")
        conexao.close()
        return None

    tentativas = 3

    while tentativas > 0:
        email = input("\nEmail: ")
        cursor.execute("SELECT email FROM usuarios WHERE email = ?", (email,))
        if not cursor.fetchone():
            print("\n❌ E-mail não cadastrado.")
            conexao.close()
            return None
        senha = input("Senha: ")
        senha = gerar_hash(senha)

        cursor.execute('''
            SELECT id, nome
            FROM usuarios 
            WHERE email = ? AND senha = ?
        ''', (email, senha))

        usuario = cursor.fetchone()

        if usuario:
            registrar_log(usuario[1], "✅ Login realizado")
            conexao.close()
            print(f"\n☺️  Bem-vindo(a), {usuario[1]}!")
            return usuario
        
        tentativas -= 1

        if tentativas > 0:
            print(f"\n❌ E-mail ou senha incorretos.")
            print(f"Tentativas restantes: {tentativas}")

    conexao.close()
    print("\n⚠️  Você excedeu o número de tentativas.")
    
    return None

def alterar_senha(id_usuario, nome_usuario):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute('''
                   SELECT senha
                   FROM usuarios
                   WHERE id = ?''', (id_usuario,))
    usuario = cursor.fetchone()
    
    senha_atual = input("\nDigite sua senha atual: ")
    hash_senha = gerar_hash(senha_atual)
    if hash_senha != usuario[0]:
        print("\n⚠️  Senha atual incorreta.")
        conexao.close()
        return
    
    nova_senha = input("\nNova senha: ")
    if not validar_senha(nova_senha):
        print("\n⚠️  A senha não atende aos requisitos de segurança.")
        conexao.close()
        return
    
    confirmacao = input("Confirme a nova senha: ")
    if nova_senha != confirmacao:
        print("\n⚠️  As senhas não coincidem.")
        conexao.close()
        return

    nova_senha = gerar_hash(nova_senha)
    cursor.execute('''
                   UPDATE usuarios
                   SET senha = ?
                   WHERE id = ?''', (nova_senha, id_usuario))
    conexao.commit()

    registrar_log(nome_usuario, "✅ Senha do cofre alterada.")

    print("\n✅ Senha alterada com sucesso!")
    conexao.close()

def excluir_conta(id_usuario, nome_usuario):
    conexao = conectar()
    cursor = conexao.cursor()

    print("\n===== EXCLUIR CONTA =====")
    confirmacao = input("\n⚠️  Tem certeza que deseja excluir sua conta?\n"
                        "1 - Sim\n"
                        "2 - Não\n"
                        "Escolha: ")
    if confirmacao != "1":
        print("\nOperação cancelada.")
        conexao.close()
        return False
    
    senha = input("\nDigite sua senha do cofre: ")
    senha = gerar_hash(senha)

    cursor.execute('''
                   SELECT senha
                   FROM usuarios
                   WHERE id = ?''', (id_usuario,))
    
    usuario = cursor.fetchone()

    if senha != usuario[0]:
        print("\n⚠️  Senha incorreta.")
        conexao.close()
        return False
    
    cursor.execute('''
                   DELETE FROM senhas
                   WHERE usuario_id = ?''', (id_usuario,))
    cursor.execute('''
                   DELETE FROM usuarios
                   WHERE id = ?''', (id_usuario,))
    
    conexao.commit()
    registrar_log(nome_usuario, "Conta excluída.")
    print("\n✅ Conta excluída com sucesso.")
    conexao.close()
    return True

    