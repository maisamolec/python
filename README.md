# 🔐 Cofre Digital

Projeto desenvolvido durante meus estudos de Python e Cibersegurança.

O objetivo é simular um gerenciador de senhas, aplicando conceitos de:

- Autenticação
- Hash
- Criptografia
- Banco de dados
- Validação de entrada
- Segurança da informação

---

## 📌 Funcionalidades

- Cadastro de usuários
- Login com autenticação
- Limite de tentativas de login
- Alteração da senha do Cofre Digital
- Exclusão da conta
- Cadastro de senhas de sites
- Listagem de senhas
- Busca de senhas
- Edição de senhas
- Exclusão de senhas
- Gerador de senhas fortes
- Criptografia das senhas armazenadas
- Registro de logs de auditoria

---

## 🔒 Segurança

O projeto utiliza alguns conceitos importantes de Segurança da informação:

- Hash SHA-256 para proteger a senha do Cofre Digital
- Criptografia Fernet para proteger as senhas dos sites
- Validação de email
- Validação de força da senha
- Limite de tentativas de login
- Confirmação antes de excluir a conta
- Auditoria por meio de logs
- Separação entre autenticação e armazenamento de dados

---

## 🛠️ Tecnologias utilizadas

- Python 3
- SQLite
- Cryptography (Fernet)
- Hashlib
- Secrets
- Datetime

---

## 📂 Estrutura do projeto

```
cofre-digital/
|
|--- banco.py
|--- gerador.py
|--- logs.py
|--- main.py
|--- seguranca.py
|--- senhas.py
|--- usuarios.py
|--- README.md
|--- .gitignore
```

---

## ▶️ Como executar

1. Clone este repositório

```
git clone https://github.com/niveaevelyn/cofre-digital.git
```

2. Entre na pasta

```
cd cofre-digital
```

3. Instale a biblioteca

```
pip install cryptography
```

4. Execute

```
python main.py
```

---

## 📖 O que aprendi

Durante o desenvolvimento deste projeto foram praticados conceitos como:

- Organização de código em módulos
- CRUD com SQLite
- Hash de senhas
- Criptografia de dados
- Validação de entradas
- Tratamento de exceções
- Programação orientada à segurança
- Documentação de projetos
- Versionamento com Git e GitHub

---

## 🚀 Melhorias futuras

- Recuperação de senha
- Interface gráfica
- Autenticação em dois fatores (2FA)
- Exportação criptografada das senhas
- Backup seguro
- Integração com API de verificação de vazamentos de senhas

---

## 👩‍💻 Desenvolvedora

Desenvolvido por **Nívea Evelyn** para praticar Python, SQLite e conceitos de Cibersegurança, simulando um gerenciador de senhas com autenticação, criptografia e armazenamento seguro de credenciais.
