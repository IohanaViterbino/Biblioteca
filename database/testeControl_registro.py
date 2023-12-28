from controller.registro import RegistroController

if __name__ == '__main__':
    print('Adicionando')  
    # RegistroController.emprestimo(2, 3, 1)
    # RegistroController.emprestimo(2, 1, 3)
    # RegistroController.emprestimo(2, 4, 3)
    # RegistroController.emprestimo(2, 3, 3)
    RegistroController.emprestimo(2, 5, 2, 'livro')

    print("Listando")
    for rg in RegistroController.get_registros():
        print(rg)

    print('Apagando')
    # Apagar.get(2)

    print("Buscar")
    print(RegistroController.get_registro(4))

    # print('Atulizaaando')
    # AtualizarRegistro.renovacao(3)
    # Listar.get()
