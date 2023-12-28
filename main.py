from view.usuario import MenuUsuario
from view.item import MenuItem
from view.registro import MenuRegistro
from view.reserva import MenuReserva

if __name__=='__main__':
    while True:
        try:
            print("############################"
                  +"\nBem vinde a biblioteca!"
                  +"\nescolha uma opção:"
                  +"\n1- Empréstimos, devoluções e renovações"
                  +"\n2- Gerenciamento de materiais"
                  +"\n3- Gerenciamento de usuário"
                  +"\n4- Gerenciamento de reservas"
                  +"\n5- Sair")
            op=int(input())

            if op == 1:
                MenuRegistro.menuView()
            elif op == 2:
                MenuItem.menuView()
            elif op == 3:
                MenuUsuario.menuView()
            elif op == 4:
                MenuReserva.menuView()
            elif op == 5:
                exit()
            else:
                print("Opção inválida. Tente outra!")

        except ValueError:
            print("Digite um valor numérico.")