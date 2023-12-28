import os
from controller.usuario import UsuarioController

class UsuarioView:
    @staticmethod
    def cadastrar_usuario():
        try:
            tipo = int(input("Insira o tipo de usuário:\n0- Aluno\n1- Professor\n"))
            if tipo in (0, 1):
                nome = input("Insira o nome do usuário: ")
                telefone = input("Insira o telefone de contato: ")
                return UsuarioController.post(nome, telefone, tipo)
            else:
                print("Tipo de usuário inexistente.")
        except ValueError:
            print("Digite um valor numérico.")

    @staticmethod
    def busca_por_id():
        try:
            id = int(input("Insira o ID do usuário: "))
            print("\t", UsuarioController.get_usuario(id))
        except (IndexError, ValueError):
            print("Identificação do usuário não encontrada ou valor inválido.")

    @staticmethod
    def atualizar_atividade():
        try:
            id = int(input("Insira o ID do usuário: "))
            ativo = int(input("Insira se o usuário está ativo na instituição:\n0- Inativo\n1- Ativo\n"))
            if ativo in (0, 1):
                UsuarioController.atualizar_ativo(id, ativo)
            else:
                print("Opção inválida.")
        except (IndexError, ValueError):
            print("Identificação do usuário não encontrada ou valor inválido.")

    @staticmethod
    def atualizar_telefone():
        try:
            id = int(input("Insira o ID do usuário: "))
            telefone = input("Insira o telefone de contato: ")
            UsuarioController.atualizar_telefone(id, telefone)
        except (IndexError, ValueError):
            print("Identificação do usuário não encontrada ou valor inválido.")

    @staticmethod
    def listar_usuarios():
        try:
            lista_usuarios = UsuarioController.get_usuarios()
            for usuario in lista_usuarios:
                print(usuario)
        except Exception as e:
            print(f"Ocorreu um erro ao listar os usuários: {e}")

class MenuUsuario:
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
                MenuUsuario.limpar_console()
                print("================*=================\nGerenciamento de usuários\nInsira a opção desejada:\n")

                for idx, opcao in enumerate(opcoes, start=1):
                    print(f"{idx}- {opcao};")

                print(f"{len(opcoes) + 1}- Sair;")

                op = int(input("\nOpção: "))

                MenuUsuario.limpar_console()
                print(f"Opção selecionada: {op}\n")

                if 1 <= op <= len(opcoes):
                    MenuUsuario.executar_acao(acoes[op - 1])
                elif op == len(opcoes) + 1:
                    exit()
                else:
                    print("Opção inválida. Insira uma válida.")

            except ValueError:
                print("Digite uma opção numérica válida.")
                input("Pressione Enter para continuar...")

    @staticmethod
    def menu_atualizacao():
        while True:
            try:
                MenuUsuario.limpar_console()
                print("====================+======================\n"
                      "Insira a opção que deseja para atualizar:\n"
                      "1- Telefone de contato\n"
                      "2- Em atividade na instituição\n"
                      "3- Sair do menu\n"
                )

                op = int(input("\nOpção: "))

                MenuUsuario.limpar_console()
                print(f"Opção selecionada: {op}\n")

                if op == 1:
                    UsuarioView.atualizar_telefone()
                elif op == 2:
                    UsuarioView.atualizar_atividade()
                elif op == 3:
                    break
                else:
                    print("Opção inválida. Insira uma válida.")

                input("Pressione Enter para continuar...")

            except ValueError:
                print("Digite uma opção numérica válida.")
                input("Pressione Enter para continuar...")

# Exemplo de uso:
opcoes_usuario = [
    "Cadastrar novo usuário",
    "Buscar usuário por ID",
    "Atualizar informações do usuário",
    "Listar todos os usuários"
]

acoes_usuario = [
    UsuarioView.cadastrar_usuario,
    UsuarioView.busca_por_id,
    MenuUsuario.menu_atualizacao,
    UsuarioView.listar_usuarios
]

MenuUsuario.visualizar_menu(opcoes_usuario, acoes_usuario)
