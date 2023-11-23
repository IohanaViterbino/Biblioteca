from controller.item import AdicionarItem, ListarItens, BuscarItem

if __name__=='__main__':
    print('Adicionando')   
    AdicionarItem.postLivro(2)
    AdicionarItem.postLivro(2)
    AdicionarItem.postLivro(4)
    AdicionarItem.postLivro(4)
    AdicionarItem.postLivro(4)
    AdicionarItem.postLivro(7)
    AdicionarItem.postLivro(7)
    AdicionarItem.postLivro(7)
    AdicionarItem.postLivro(7)

    # AdicionarItem.postTablet(2)
    # AdicionarItem.postTablet(2)
    # AdicionarItem.postTablet(2)
    # AdicionarItem.postTablet(2)
    # AdicionarItem.postTablet(7)
    # AdicionarItem.postTablet(7)
    # AdicionarItem.postTablet(5)

    print('listando')   
    ListarItens.get()

    print('buscando')   
    print(BuscarItem.getLivro(4))
    # print(BuscarItem.getTablet(14))
