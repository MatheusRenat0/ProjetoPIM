import json
import os

ARQUIVO = "dados.json"
SENHA_CORRETA = "ADS2025"  

def carregar_dados():
    if os.path.exists(ARQUIVO):
        try:
            with open(ARQUIVO, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return []
    return []

def salvar_dados(dados):
    with open(ARQUIVO, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

def verificar_senha():
    senha = input("Digite a senha para acessar os cadastros: ")
    return senha == SENHA_CORRETA

def cadastrar():
    nome = input("Digite o nome: ")
    idade = input("Digite a idade: ")
    email = input("Digite o email: ")

    dados = carregar_dados()
    dados.append({
        "nome": nome,
        "idade": idade,
        "email": email
    })
    salvar_dados(dados)
    print("Cadastro salvo com sucesso!")

def listar():
    if not verificar_senha():
        print("Senha incorreta. Acesso negado.")
        return
        
    dados = carregar_dados()
    if not dados:
        print("Nenhum dado cadastrado.")
        return
    print("\nLista de cadastros:")
    for i, pessoa in enumerate(dados, 1):
        print(f"{i}. Nome: {pessoa['nome']}, Idade: {pessoa['idade']}, Email: {pessoa['email']}")

def menu():
    while True:
        print("\n1 - Cadastrar pessoa")
        print("2 - Listar cadastros")
        print("3 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            listar()
        elif opcao == "3":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
