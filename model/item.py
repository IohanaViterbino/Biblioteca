from datetime import datetime

class Item:
    def __init__(self, livroOUtablet, codigo=None, disponivel=1):
        self.__dataAquisicao = datetime.now()
        self.__livroTablet = livroOUtablet
        self.__codItem = codigo
        self.__disponivel = disponivel #1- se ta disponível, 0- Não ta disponível

    # Getters
    def get_dataAquisicao(self):
        return self.__dataAquisicao
    def get_livroTablet(self):
        return self.__livroTablet
    def get_reservas(self):
        return self.__reservas
    def get_codItem(self):
        return self.__codItem
    def get_disponivel(self):
        return self.__disponivel

    # Setters
    def set_dataAquisicao(self, dataAquisicao):
        self.__dataAquisicao = dataAquisicao
    def set_livroTablet(self, livroTablet):
        self.__livroTablet = livroTablet
    def set_disponivel(self, disponivel):
        self.__disponivel = disponivel
    def set_codItem(self, codItem):
        self.__codItem = codItem
  
    def __str__(self):
        disponibilidade_item = 'Indisponível' if self.__tipo == 0 else 'Disponível'
        return f"Item: {self.__codItem}, Data de Aquisição: {self.__dataAquisicao}, Tipo: {self.__livroTablet}, Disponível: {disponibilidade_item}"