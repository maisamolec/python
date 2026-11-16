from banco import conectar
from seguranca import criptografar, descriptografar
from gerador import gerar_senha, obter_senha

def cadastrar_senha(id_usuario):
    conexao = conectar()
    cursor = conexao.cursor()

    titulo = input("\nNome do site/serviço: ")
    if not titulo.strip():
        print("\n❌ Título inválido.")
        conexao.close()
        return
    login = input("Usuário ou email: ")
    if not login.strip():
        print("\n❌ Login inválido.")
        conexao.close()
        return
    senha = obter_senha()
    senha = criptografar(senha)

    cursor.execute('''
                   INSERT INTO senhas(usuario_id, titulo, login, senha)
                   VALUES (?, ?, ?, ?)
                   ''', (id_usuario, titulo, login, senha))

    conexao.commit()
    conexao.close()
    print("\n✅ Senha cadastrada com sucesso!")

def listar_senhas(id_usuario):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute('''
                   SELECT id, titulo, login, senha
                   FROM senhas
                   WHERE usuario_id = ?
                   ''', (id_usuario,))
    
    senhas = cursor.fetchall()
    conexao.close()

    if len(senhas) == 0:
        print("\nℹ️  Nenhuma senha cadastrada.")
    else:
        print("\n===== SENHAS CADASTRADAS =====")
        for senha in senhas:
            print("\nID:", senha[0])
            print("Título:", senha[1])
            print("Login:", senha[2])
            print("Senha:", descriptografar(senha[3]))

def buscar_senha(id_usuario):
    conexao = conectar()
    cursor = conexao.cursor()

    site = input("\n🔍 Digite o site que deseja buscar: ")

    cursor.execute('''
                   SELECT titulo, login, senha
                   FROM senhas
                   WHERE usuario_id = ? AND titulo LIKE ?
                   ''', (id_usuario, f"%{site}%"))

    senhas = cursor.fetchall()
    conexao.close()

    if len(senhas) == 0:
        print("\nℹ️  Nenhuma senha encontrada.")
    else:
        print("\n===== SENHAS CADASTRADAS =====")
        for senha in senhas:
            print("\nTítulo:", senha[0])
            print("Login:", senha[1])
            print("Senha:", descriptografar(senha[2]))

def editar_senha(id_usuario):
    conexao = conectar()
    cursor = conexao.cursor()

    id_senha = input("\nDigite o ID da senha que deseja editar: ")

    cursor.execute('''
                   SELECT titulo, login, senha
                   FROM senhas
                   WHERE id = ? AND usuario_id = ?
                   ''', (id_senha, id_usuario))
    
    senha = cursor.fetchone()

    if senha:
        print("\n✅ Senhas encontradas!")
        print("Título:", senha[0])
        print("Login:", senha[1])

        novo_login = input("\nNovo login: ")
        nova_senha = obter_senha()
        nova_senha = criptografar(nova_senha)

        cursor.execute('''
                       UPDATE senhas
                       SET login = ?, senha = ?
                       WHERE id = ? AND usuario_id = ?
                       ''', (novo_login, nova_senha, id_senha, id_usuario))
        
        conexao.commit()

        print("\n✅ Senha atualizada com sucesso!")

    else:
        print("\n❌ Senha não encontrada.")
    
    conexao.close()

def excluir_senha(id_usuario):
    conexao = conectar()
    cursor = conexao.cursor()

    id_senha = input("\nDigite o ID da senha que deseja excluir: ")

    cursor.execute('''
                   SELECT titulo
                   FROM senhas
                   WHERE id = ? AND usuario_id = ?
                   ''', (id_senha, id_usuario))
    
    senha = cursor.fetchone()

    if senha:
        confirmacao = input(f"⚠️ Tem certeza que deseja excluir {senha[0]}? (S/N): ")

        if confirmacao.upper() == "S":
            cursor.execute('''
                           DELETE FROM senhas
                           WHERE id = ? AND usuario_id = ?
                           ''', (id_senha, id_usuario))
            conexao.commit()

            print("\n✅ Senha excluída com sucesso!")

        else:
            print("\n❌ Exclusão cancelada.")
    
    else:
        print("\n❌ Senha não encontrada.")

    conexao.close()
