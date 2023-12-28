import os
from controller.registro import RegistroController

class RegistroView:
    @staticmethod
    def cadastrar_emprestimo():
        try:
            tipo = input("Insira o tipo de item que deseja fazer o empréstimo:\n0- Livro\n1- Tablet\n")
            tipo = 'livro' if tipo == '0' else 'tablet'
            cod_lt = int(input(f"Insira o ID do {tipo} que deseja fazer o empréstimo: "))
            cod_us = int(input(f"Insira o ID do usuário que deseja fazer o empréstimo: "))
            return RegistroController.emprestimo(cod_lt, cod_us, tipo)
        
        except ValueError:
            print("Digite um valor numérico.")

    @staticmethod
    def listar_registros():
        registros = RegistroController.get_registros()
        for registro in registros:
            print(registro)

    @staticmethod
    def buscar_por_id():
        try:
            id = int(input("Insira o ID do registro: "))
            print("\t", RegistroController.get_registro(id))

        except ValueError:
            print("Digite um valor numérico.")

    @staticmethod
    def operacao_registro(operacao):
        try:
            id = int(input("Insira o ID do registro: "))
            getattr(RegistroController, operacao)(id)

        except ValueError:
            print("Digite um valor numérico.")

class MenuRegistro:
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
                MenuRegistro.limpar_console()
                print(
                    "================*=================\n"
                    "Gerenciamento de registro de empréstimo\n"
                    "Insira a opção desejada:\n"
                )

                for idx, opcao in enumerate(opcoes, start=1):
                    print(f"{idx}- {opcao};")

                print(f"{len(opcoes) + 1}- Sair;")

                op = int(input("\nOpção: "))

                MenuRegistro.limpar_console()
                print(f"Opção selecionada: {op}\n")

                if 1 <= op <= len(opcoes):
                    MenuRegistro.executar_acao(acoes[op - 1])
                elif op == len(opcoes) + 1:
                    break
                else:
                    print("Opção inválida. Insira uma válida.")

            except ValueError:
                print("Digite uma opção numérica válida.")
                input("Pressione Enter para continuar...")

# Exemplo de uso:
opcoes = [
    "Cadastrar novo empréstimo",
    "Buscar registro por ID",
    "Excluir registro",
    "Listar todos os registros",
    "Renovação do empréstimo",
    "Devolução do empréstimo"
]

acoes = [
    RegistroView.cadastrar_emprestimo,
    RegistroView.buscar_por_id,
    lambda: RegistroView.operacao_registro('excluir_registro'),
    RegistroView.listar_registros,
    lambda: RegistroView.operacao_registro('renovacao'),
    lambda: RegistroView.operacao_registro('devolucao')
]
