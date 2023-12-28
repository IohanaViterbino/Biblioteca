import os
from controller.reserva import ReservaController

class ReservaView:
    @staticmethod
    def cadastrar_reserva():
        try:
            tipo = input("Insira o tipo de item para fazer a reserva:\n0- Livro\n1- Tablet\n")
            tipo = 'livro' if tipo == '0' else 'tablet'
            cod_lt = int(input(f"Insira o ID do {tipo} para fazer a reserva: "))
            cod_us = int(input(f"Insira o ID do usuário para fazer a reserva: "))
            return ReservaController.post(cod_us, cod_lt, tipo)
        
        except ValueError:
            print("Digite um valor numérico.")

    @staticmethod
    def listar_reservas():
        reservas = ReservaController.get_reservas()
        for reserva in reservas:
            print(reserva)

    @staticmethod
    def buscar_por_id():
        try:
            id = int(input("Insira o ID da reserva: "))
            print("\t", ReservaController.get_reserva(id))

        except (IndexError, ValueError):
            print("Identificação da reserva não encontrada ou valor inválido.")

    @staticmethod
    def excluir():
        try:
            id = int(input("Insira o ID da reserva: "))
            ReservaController.excluir_reserva(id)

        except (IndexError, ValueError):
            print("Identificação da reserva não encontrada ou valor inválido.")

class MenuReserva:
    @staticmethod
    def limpar_console():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def executar_acao(acao):
        try:
            acao()
        except ValueError:
            print("Digite uma opção válida")
        input("Pressione Enter para continuar...")

    @staticmethod
    def visualizar_menu(opcoes, acoes):
        while True:
            try:
                MenuReserva.limpar_console()
                print("================*=================")
                print("Gerenciamento de reservas")
                print("Insira a opção desejada:")

                for idx, opcao in enumerate(opcoes, start=1):
                    print(f"{idx}- {opcao};")

                print(f"{len(opcoes) + 1}- Sair;")

                op = int(input("\nOpção: "))

                MenuReserva.limpar_console()
                print(f"Opção selecionada: {op}\n")

                if 1 <= op <= len(acoes):
                    MenuReserva.executar_acao(acoes[op - 1])
                elif op == len(acoes) + 1:
                    break
                else:
                    print("Opção inválida. Insira uma válida")

            except ValueError:
                print("Digite uma opção NUMÉRICA válida")
                input("Pressione Enter para continuar...")

# Exemplo de uso:
opcoes = [
    "Cadastrar nova reserva",
    "Buscar reserva por ID",
    "Excluir reserva",
    "Listar todas as reservas"
]

acoes = [
    ReservaView.cadastrar_reserva,
    ReservaView.buscar_por_id,
    ReservaView.excluir,
    ReservaView.listar_reservas
]
