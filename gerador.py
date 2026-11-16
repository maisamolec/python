import secrets
import string

def gerar_senha():
    while True:
        try:
            tamanho = int(input("Digite a quantidade de caracteres (mínimo 8 e máximo 12): "))
            if tamanho < 8:
                print("\n⚠️  A senha deve possuir no mínimo 8 caracteres.\n")
                continue
            if tamanho > 12:
                print("\n⚠️  A senha deve possuir no máximo 12 caracteres.\n")
                continue
            break
        except ValueError:
            print("\n⚠️  Digite apenas números.\n")

    maiusculas = string.ascii_uppercase
    minusculas = string.ascii_lowercase
    numeros = string.digits
    simbolos = "!@#$%&*?"

    senha = [  
        secrets.choice(maiusculas),
        secrets.choice(minusculas),
        secrets.choice(numeros),
        secrets.choice(simbolos)
    ]

    caracteres = maiusculas + minusculas + numeros + simbolos

    while len(senha) < tamanho:
        senha.append(secrets.choice(caracteres))
    
    secrets.SystemRandom().shuffle(senha)

    senha = "".join(senha)
    print("\n✅ Senha gerada:")
    print(senha)

    return senha

def obter_senha():
    while True:
        opcao = input("Como deseja definir a senha?"
                      "\n1 - Digitar senha\n"
                      "2 - Gerar uma senha forte\n"
                      "Escolha: ")
        if opcao == "1":
            return input("Senha: ")
        elif opcao == "2":
            return gerar_senha()
        else:
            print("\n⚠️  Opção inválida. Tente novamente.")
