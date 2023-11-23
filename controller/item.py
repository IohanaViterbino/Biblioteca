from model.item import Item

class AdicionarItem:
    @staticmethod
    def postLivro(codLivroTablet):
        item = Item(codLivroTablet)
        item.salvarLivro()

    @staticmethod
    def postTablet(codLivroTablet):
        item = Item(codLivroTablet)
        item.salvarTablet()

class AtualizarItem:
    @staticmethod
    def disponibilidade_Livro(id, disponibilidade):
        item= Item.getItemLivro(id)
        item.set_disponivel(disponibilidade)
        item.alterarDisponibilidade()
    
    @staticmethod
    def disponibilidade_Tablet(id, disponibilidade):
        item= Item.getItemTablet(id)
        item.set_disponivel(disponibilidade)
        item.alterarDisponibilidade()

class ApagarItem:
    @staticmethod
    def get(id):
        item= Item.getItemTablet(id)
        item.excluirItem()

class ListarItens:
    @staticmethod
    def get():
        itens= Item.getItens()
        for item in itens:
            print(item)

class BuscarItem:
    @staticmethod
    def getLivro(id):
        return Item.getItemLivro(id)

    @staticmethod
    def getTablet(id):
        return Item.getItemTablet(id)