from controller.usuario import AdicionarUsuario, ListarUsuario, BuscarUsuario, AtualizarUsuario

if __name__=='__main__':
    print('Adicionando')   
    # AdicionarUsuario.post("João", "123456789", 0)
    # AdicionarUsuario.post("Maria", "987654321", 1)
    # AdicionarUsuario.post("Pedro", "555555555", 0)
    # AdicionarUsuario.post("Jorge", "5555777755", 0)
    
    print("Listando")
    ListarUsuario.get()
    
    print("Buscar")
    print(BuscarUsuario.get(4))

    print('Atulizaaando')
    # AtualizarUsuario.telefone(2, '84966552211')
    # AtualizarUsuario.limite(1, 1)
    # AtualizarUsuario.ativo(3, 0)
    # AtualizarUsuario.inadimplencia(1, 1)
    # ListarUsuario.get()

    print('Apagando')
    # Apagar.get(2)
    # Listar.get()