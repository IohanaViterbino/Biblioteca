import os
from controller.tablet import TabletController

class TabletView:
    @staticmethod
    def cadastrar_tablet():
        marca = input("Insira a marca do tablet: ")
        modelo = input("Insira o modelo do tablet: ")
        memoria = input("Insira o tamanho da memória do tablet: ")
        so = input("Insira o sistema operacional do tablet: ")
        TabletController.post(marca, modelo, memoria, so)

    @staticmethod
    def listar_tablets():
        tablets = TabletController.get_tablets()
        for tablet in tablets:
            print(tablet)

    @staticmethod
    def buscar_por_id():
        try:
            id = int(input("Insira o ID do tablet: "))
            print("\t", TabletController.get_tablet(id))

        except (IndexError, ValueError):
            print("Identificação da reserva não encontrada ou valor inválido.")

class MenuTablet:
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
                MenuTablet.limpar_console()
                print(
                    "================-=================\n"
                    "Gerenciamento de tablets\n"
                    "Insira a opção desejada:\n"
                )

                for idx, opcao in enumerate(opcoes, start=1):
                    print(f"{idx}- {opcao};")

                print(f"{len(opcoes) + 1}- Sair;")

                op = int(input("\nOpção: "))

                MenuTablet.limpar_console()
                print(f"Opção selecionada: {op}\n")

                if 1 <= op <= len(opcoes):
                    MenuTablet.executar_acao(acoes[op - 1])
                elif op == len(opcoes) + 1:
                    break
                else:
                    print("Opção inválida. Insira uma válida.")

            except ValueError:
                print("Digite uma opção numérica válida.")
                input("Pressione Enter para continuar...")

# Exemplo de uso:
opcoes_tablet = [
    "Cadastrar novo tablet",
    "Buscar tablet por ID",
    "Listar todos os tablets"
]

acoes_tablet = [
    TabletView.cadastrar_tablet,
    TabletView.buscar_por_id,
    TabletView.listar_tablets
]

