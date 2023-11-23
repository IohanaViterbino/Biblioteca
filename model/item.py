from database.db import _executar
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

    query = "CREATE TABLE IF NOT EXISTS item (codigo INTEGER PRIMARY KEY AUTOINCREMENT, disponivel NUMERIC NOT NULL, dataAquisicao DATE NOT NULL, idLivro NUMERIC, idTablet NUMERIC)"
    _executar(query)

    def salvarTablet(self):
        query = f"""
        INSERT INTO item (dataAquisicao, idTablet, disponivel)
        VALUES ('{self.__dataAquisicao}', {int(self.__livroTablet)}, {int(self.__disponivel)})
        """
        _executar(query)

    def salvarLivro(self):
        query = f"""
        INSERT INTO item (dataAquisicao, idLivro, disponivel)
        VALUES ('{self.__dataAquisicao}', {int(self.__livroTablet)}, {int(self.__disponivel)})
        """
        _executar(query)

    def alterarDisponibilidade(self):
        query = f"""
                UPDATE item SET disponivel = {self.__disponivel}
                WHERE Codigo = '{int(self.__codItem)}'
                """
        _executar(query)

    def excluirItem(self):
        query=f"DELETE FROM item WHERE Codigo = '{int(self.__codItem)}'"
        _executar(query)
    
   #buscar itens
    @staticmethod
    def getItens():
        query="SELECT * FROM item"
        itens=_executar(query)
        return itens

    @staticmethod
    def getItemTablet(id):
        query = f"""
                SELECT codigo, dataAquisicao, idTablet, disponivel FROM item
                WHERE codigo ={int(id)}
                """
        item=_executar(query)[0]
        item=Item(codigo=item[0], livroOUtablet=item[2], disponivel=item[3])
        return item
    
    @staticmethod
    def getItemLivro(id):
        query = f"""
                SELECT codigo, dataAquisicao, idLivro, disponivel FROM item
                WHERE codigo ={int(id)}
                """
        item=_executar(query)[0]
        item=Item(codigo=item[0], livroOUtablet=item[2], disponivel=item[3])
        return item

    def __str__(self):
        return f"Item: {self.__codItem}, Data de Aquisição: {self.__dataAquisicao}, Tipo: {self.__livroTablet}, Disponível: {self.__disponivel}"