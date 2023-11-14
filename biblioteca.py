# PUC - GO
# Estrutura de Dados
# Atividade Prática: Sistema de Gerenciamento de Biblioteca usando Listas
# Felipe de Paula Palmeira

# Inicialização da lista de livros
livros = []

# Função para criar um novo livro
def criar_livro(titulo, autor, ano):
    return {"titulo": titulo, "autor": autor, "ano": ano}

# Função para adicionar um livro à lista
def adicionar_livro():
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o nome do autor: ")
    ano = input("Digite o ano de publicação: ")
    novo_livro = criar_livro(titulo, autor, ano)
    livros.append(novo_livro)
    print(f"O livro '{titulo}' foi adicionado com sucesso!")

# Função para listar todos os livros
def listar_livros():
    if not livros:
        print("Ainda não há livros cadastrados.")
        return

    print("\nLista de Livros:")
    for livro in livros:
        print(f"{livro['titulo']} | {livro['autor']} | {livro['ano']}")

# Função para buscar um livro pelo título
def buscar_livro():
    termo_busca = input("Digite o título ou parte do título do livro: ").lower()
    livros_encontrados = [livro for livro in livros if termo_busca in livro['titulo'].lower()]

    if not livros_encontrados:
        print("Nenhum livro encontrado.")
        return

    print("\nLivros encontrados:")
    for i, livro in enumerate(livros_encontrados, 1):
        print(f"{i}. {livro['titulo']} | {livro['autor']} | {livro['ano']}")

    while True:
        escolha = input("\nDigite o número do livro para mais opções ou 'v' para voltar: ").lower()

        if escolha == 'v':
            return
        elif escolha.isdigit() and 1 <= int(escolha) <= len(livros_encontrados):
            index = int(escolha) - 1
            livro_selecionado = livros_encontrados[index]
            print(f"Você selecionou: {livro_selecionado['titulo']} | {livro_selecionado['autor']} | {livro_selecionado['ano']}")
            
            print("\n1. Remover Livro")
            print("2. Voltar")
            sub_escolha = input("Escolha uma opção: ")

            if sub_escolha == "1":
                remover_livro(livro_selecionado['titulo'])
                break
            elif sub_escolha == "2":
                return
            else:
                print("Opção inválida. Tente novamente.")
        else:
            print("Opção inválida. Tente novamente.")

# Função de remover livro pelo título
def remover_livro(titulo):
    global livros
    livros_original = list(livros)
    livros = [livro for livro in livros if livro['titulo'].lower() != titulo.lower()]
    
    if len(livros) == len(livros_original):
        print(f"Nenhum livro com o título '{titulo}' foi encontrado.")
    else:
        print(f"O(s) livro(s) com o título '{titulo}' foram removidos.")

# Função para exibir o menu e processar a escolha do usuário
def menu():
    while True:
        print("\n--- Menu da Biblioteca ---")
        print("1. Cadastrar novo Livro")
        print("2. Listar todos os Livros")
        print("3. Buscar Livro")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            adicionar_livro()
        elif escolha == "2":
            listar_livros()
        elif escolha == "3":
            buscar_livro()
        elif escolha == "4":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executar o programa
menu()
