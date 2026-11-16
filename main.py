from banco import criar_tabelas
from usuarios import cadastrar_usuario, login, alterar_senha, excluir_conta
from senhas import cadastrar_senha, listar_senhas, buscar_senha, editar_senha, excluir_senha
from logs import registrar_log

criar_tabelas()

def menu_usuario(usuario_logado):
    id_usuario = usuario_logado[0]
    nome_usuario = usuario_logado[1]
    
    while True:
        print("\n===== MENU DE USUÁRIO =====")
        print("1 - Cadastrar senha")
        print("2 - Listar senhas")
        print("3 - Buscar senha")
        print("4 - Editar senha")
        print("5 - Excluir senha")
        print("6 - Alterar senha do Cofre Digital")
        print("7 - Excluir minha conta")
        print("0 - Logout")

        opcao = input("Escolha: ")

        if opcao == "1":
            cadastrar_senha(id_usuario)
        elif opcao == "2":
            listar_senhas(id_usuario)
        elif opcao == "3":
            buscar_senha(id_usuario)
        elif opcao == "4":
            editar_senha(id_usuario)
        elif opcao == "5":
            excluir_senha(id_usuario)
        elif opcao == "6":
            alterar_senha(id_usuario, nome_usuario)
        elif opcao == "7":
            conta_excluida = excluir_conta(id_usuario, nome_usuario)
            if conta_excluida:
                break
        elif opcao == "0":
            print("✅ Logout realizado.")
            registrar_log(nome_usuario, "✅ Logout realizado.")
            break
        else:
            print("⚠️  Opção inválida. Tente novamente.")

while True:
    print("\n===== COFRE DIGITAL =====")
    print("1 - Cadastrar usuário")
    print("2 - Login")
    print("3 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        cadastrar_usuario()

    elif opcao == "2":
        usuario_logado = login()
        if usuario_logado:
            menu_usuario(usuario_logado)

    elif opcao == "3":
        print("\n👋 Até logo!")
        break

    else:
        print("\n⚠️  Opção inválida. Tente novamente.")
