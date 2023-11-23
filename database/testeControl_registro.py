from controller.registro import AdicionarRegistro, ListarRegistro,  AtualizarRegistro, BuscarRegistro

if __name__ == '__main__':
    print('Adicionando')  
    AdicionarRegistro.postLivro(2, 3, 1)
    AdicionarRegistro.postLivro(2, 1, 3)
    AdicionarRegistro.postLivro(2, 2, 1)
    AdicionarRegistro.postLivro(2, 4, 3)
    AdicionarRegistro.postLivro(2, 5, 4)
    AdicionarRegistro.postLivro(2, 6, 4)

    print("Listando")
    ListarRegistro.get()

    print('Apagando')
    # Apagar.get(2)

    print("Buscar")
    BuscarRegistro.get(3)

    # print('Atulizaaando')
    # AtualizarRegistro.renovacao(3)
    # Listar.get()
