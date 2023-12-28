from controller.item import ItemController
from view.livro import MenuLivro
from view.tablet import MenuTablet
import os

class ItemView:
    @staticmethod
    def cadastro_item():
        try:
            tipo = input("Insira o tipo de item:\n0- Livro\n1- Tablet\n")
            tipo = 'livro' if tipo == 0 else 'tablet'
            codLt = int(input(f"Insira o id do {tipo}: "))
            return ItemController.adicionar_item(tipo, codLt)
        
        except ValueError:
            print("Digite um valor numérico.")

    @staticmethod
    def listar_itens():
        itens= ItemController.get_itens()
        for tb in itens:
            print(tb)

    @staticmethod
    def buscar_por_id():
        try:
            id = int(input("Insira o id do item: "))
            print("\t", ItemController.get_item(id))

        except IndexError:
            print("Identificação do item não encontrada.")
        except ValueError:
            print("Digite um valor numérico.")

    @staticmethod
    def excluir():
        try:
            id = int(input("Insira o id do item: "))
            ItemController.excluir_item(id)

        except IndexError:
            print("Identificação do item não encontrada.")
        except ValueError:
            print("Digite um valor numérico.")

class MenuItem:
    @staticmethod
    def clear_console():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def menuView():
        while True:
            try:
                MenuItem.clear_console()
                print(f"================*================="+
                      "\nGerenciamento de materiais\nInsira a opção desejada:"
                      +"\n1- Cadastrar novo item;"
                      +"\n2- Buscar item por id;"
                      +"\n3- Excluir item;"
                      +"\n4- Listar todos os itens;"
                      +"\n5- Gerenciamento de Livros;"
                      +"\n6- Gerenciamento de Tablets;"
                      +"\n7- Sair;")

                op = int(input("\nOpção: "))

                MenuItem.clear_console()
                print(f"Opção selecionada: {op}\n")

                if op == 1:
                    ItemView.cadastro_item()
                elif op == 2:
                    ItemView.buscar_por_id()
                elif op == 3:
                    ItemView.excluir()
                elif op == 4:
                    ItemView.listar_itens()
                elif op == 5:
                    MenuLivro.menuView()
                elif op == 6:
                    MenuTablet.menuView()
                elif op == 7:
                    break
                else:
                    print("Opção inválida. Insira uma válida")

                input("Pressione Enter para continuar...")

            except ValueError:
                print("Digite uma opção NUMÉRICA válida")
                input("Pressione Enter para continuar...")