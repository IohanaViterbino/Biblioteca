from controller.item import ItemController

if __name__=='__main__':
    print('Adicionando')   
    ItemController.adicionar_item('livro',2)
    ItemController.adicionar_item('livro',2)
    ItemController.adicionar_item('livro',4)
    ItemController.adicionar_item('livro',4)
    ItemController.adicionar_item('livro',4)
    ItemController.adicionar_item('livro',7)
    ItemController.adicionar_item('livro',7)
    ItemController.adicionar_item('livro',7)
    ItemController.adicionar_item('livro',5)
    ItemController.adicionar_item('livro',5)
    ItemController.adicionar_item('livro',5)

    # ItemController.adicionar_item('tablet',2)
    # ItemController.adicionar_item('tablet',2)
    # ItemController.adicionar_item('tablet',1)
    # ItemController.adicionar_item('tablet',1)
    # ItemController.adicionar_item('tablet',6)
    # ItemController.adicionar_item('tablet',6)
    # ItemController.adicionar_item('tablet',6)
    # ItemController.adicionar_item('tablet',8)
    # ItemController.adicionar_item('tablet',8)
    # ItemController.adicionar_item('tablet',8)

    print('listando')   
    for ite in ItemController.get_itens():
        print(ite)

    print('buscando')   
    print(ItemController.get_item('livro',4))
