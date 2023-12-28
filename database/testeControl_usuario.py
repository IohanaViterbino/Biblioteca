from controller.usuario import UsuarioController

if __name__=='__main__':
    print('Adicionando')   
    UsuarioController.post("João", "123456789", 0)
    UsuarioController.post("Maria", "987654321", 1)
    UsuarioController.post("Pedro", "555555555", 0)
    UsuarioController.post("Jorge", "5555777755", 0)
    
    print("Listando")
    for usuario in UsuarioController.get_usuarios():
        print(usuario)
    
    print("Buscar")
    print(UsuarioController.get_usuario(4))

    print('Atulizaaando')
    # UsuarioController.telefone(2, '84966552211')
    # UsuarioController.limite(1, 1)
    # UsuarioController.ativo(3, 0)
    # UsuarioController.inadimplencia(1, 1)
    # UsuarioController.get_usuarios()

    print('Apagando')
    # UsuarioController.excluir(2)
    # UsuarioController.get_usuarios()