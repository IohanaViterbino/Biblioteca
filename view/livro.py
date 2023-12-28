import os
from controller.livro import LivroController

class LivroView:
    @staticmethod
    def cadastrar_livro():
        titulo = input("Insira o título do livro: ")
        autor = input("Insira o autor do livro: ")
        editora = input("Insira a editora do livro: ")
        categoria = input("Insira a categoria do livro: ")
        edicao = input("Insira a edição do livro: ")
        LivroController.adicionar_livro(titulo, autor, editora, categoria, edicao)

    @staticmethod
    def alterar_categoria():
        try:
            id = int(input("Insira o ID do livro: "))
            categoria = input("Insira a nova categoria do livro: ")
            LivroController.atualizar_categoria(id, categoria)

        except (IndexError, ValueError):
            print("Identificação da reserva não encontrada ou valor inválido.")

    @staticmethod
    def listar_livros():
        livros = LivroController.get_livros()
        for livro in livros:
            print(livro)

    @staticmethod
    def buscar_por_id():
        try:
            id = int(input("Insira o ID do livro: "))
            print("\t", LivroController.get_livro(id))

        except (IndexError, ValueError):
            print("Identificação da reserva não encontrada ou valor inválido.")

class MenuLivro:
    @staticmethod
    def limpar_console():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def executar_acao(acao):
        try:
            acao()
        except ValueError:
            print("Digite uma opção válida.")
        input("Pressione Enter para continuar...")

    @staticmethod
    def visualizar_menu(opcoes, acoes):
        while True:
            try:
                MenuLivro.limpar_console()
                print(
                    "================-=================\n"
                    "Gerenciamento de livros\n"
                    "Insira a opção desejada:\n"
                )

                for idx, opcao in enumerate(opcoes, start=1):
                    print(f"{idx}- {opcao};")

                print(f"{len(opcoes) + 1}- Sair;")

                op = int(input("\nOpção: "))

                MenuLivro.limpar_console()
                print(f"Opção selecionada: {op}\n")

                if 1 <= op <= len(opcoes):
                    MenuLivro.executar_acao(acoes[op - 1])
                elif op == len(opcoes) + 1:
                    break
                else:
                    print("Opção inválida. Insira uma válida.")

            except ValueError:
                print("Digite uma opção numérica válida.")
                input("Pressione Enter para continuar...")

    @staticmethod
    def menu_atualizacao():
        while True:
            try:
                MenuLivro.limpar_console()
                print(
                    "====================!======================\n"
                    "Insira a opção que deseja para atualizar:\n"
                    "1- Categoria\n"
                    "2- Sair do menu\n"
                )

                op = int(input("\nOpção: "))

                MenuLivro.limpar_console()
                print(f"Opção selecionada: {op}\n")

                if op == 1:
                    LivroView.alterar_categoria()
                elif op == 2:
                    break
                else:
                    print("Opção inválida. Insira uma válida.")

                input("Pressione Enter para continuar...")

            except ValueError:
                print("Digite uma opção numérica válida.")
                input("Pressione Enter para continuar...")

# Exemplo de uso:
opcoes_livro = [
    "Cadastrar novo livro",
    "Buscar livro por ID",
    "Atualizar informações do livro",
    "Listar todos os livros"
]

acoes_livro = [
    LivroView.cadastrar_livro,
    LivroView.buscar_por_id,
    MenuLivro.menu_atualizacao,
    LivroView.listar_livros
]

MenuLivro.visualizar_menu(opcoes_livro, acoes_livro)
