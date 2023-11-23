from database.db import _executar
from datetime import datetime, timedelta

class RegistroEmprestimo:
    def __init__(self, vlrMulta, item, usuario, dataEmpres=None, limite=7, id=None):
        self.__multa = vlrMulta
        self.__item = item
        self.__usuario = usuario
        self.__id = id
        self.__dataEmprestimo = dataEmpres if dataEmpres else datetime.now()
        self.__limiteDevolucao = limite        
        self.__dataDevolucao = self.__dataEmprestimo + timedelta(days=self.__limiteDevolucao)

    # Getters
    def get_multa(self):
        return self.__multa
    def get_item(self):
        return self.__item
    def get_usuario(self):
        return self.__usuario
    def get_id(self):
        return self.__id
    def get_limiteDevolucao(self):
        return self.__limiteDevolucao
    def get_dataEmprestimo(self):
        return self.__dataEmprestimo
    def get_dataDevolucao(self):
        return self.__dataDevolucao

    # Setters
    def set_multa(self, vlrMulta):
        self.__multa = vlrMulta
    def set_item(self, item):
        self.__item = item
    def set_usuario(self, usuario):
        self.__usuario = usuario
    def set_id(self, id):
        self.__id = id
    def set_limiteDevolucao(self, limiteDevolucao):
        self.__limiteDevolucao = limiteDevolucao
    def set_dataEmprestimo(self, dataEmprestimo):
        self.__dataEmprestimo = dataEmprestimo
    def set_dataDevolucao(self, dataDevolucao):
        self.__dataDevolucao = dataDevolucao

    query = "CREATE TABLE IF NOT EXISTS resgistroEmprestimo(Id INTEGER PRIMARY KEY AUTOINCREMENT, limiteDevolucao INTEGER, valorMulta REAL, dataEmprestimo INTEGER, DataEsperada INTEGER, codItem INTEGER, matricula INTEGER)"
    _executar(query)

    def salvar(self):
        query = f"INSERT INTO resgistroEmprestimo(limiteDevolucao, valorMulta, dataEmprestimo, DataEsperada, codItem, matricula) VALUES ({int(self.__limiteDevolucao)}, {float(self.__multa)}, '{self.__dataEmprestimo}', '{self.__dataDevolucao}', {int(self.__item)}, {int(self.__usuario)})"
        _executar(query)

    def alterarDevolucao(self):
        query = f"""
                UPDATE resgistroEmprestimo SET DataEsperada = '{self.__dataDevolucao}'
                WHERE Id = '{int(self.__id)}'
                """
        _executar(query)
    
    def excluirRegistro(self):
        query=f"DELETE FROM resgistroEmprestimo WHERE id = '{int(self.__id)}'"
        _executar(query)
    
    @staticmethod
    def getRegistros():
        query="SELECT * FROM resgistroEmprestimo"
        registros=_executar(query)
        return registros
    
    @staticmethod
    def getRegistro(id):
        query = f"""
                SELECT * FROM resgistroEmprestimo
                WHERE id = {int(id)}
                """
        registro=_executar(query)[0]
        dataEsperada = datetime.fromisoformat(registro[4]) # Convertendo a string do banco para datetime
        registro=RegistroEmprestimo(id=registro[0],limite=registro[1], vlrMulta=registro[2], dataEmpres=datetime.fromisoformat(registro[3]), item=registro[5], usuario=registro[6])
        registro.set_dataDevolucao(dataEsperada)
        return registro


    def __str__(self):
        return f"ID: {self.__id}, Valor da multa: {self.__multa}, Item: {self.__item}, " \
               f"Usuário: {self.__usuario}, Data do empréstimo: {self.__dataEmprestimo}, " \
               f"Data esperada de devolução: {self.__dataDevolucao}"    