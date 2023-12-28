from datetime import datetime, timedelta

class RegistroEmprestimo:
    def __init__(self, item, usuario, vlrMulta=2.0, dataEmpres=datetime.now(), limite=7, id=None):
        self.__multa = vlrMulta
        self.__item = item
        self.__usuario = usuario
        self.__id = id
        self.__dataEmprestimo = dataEmpres
        self.__limiteDevolucao = limite        
        # calcula a data de devolução a partir do empréstimo mais os 7 dias de limite
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

    def __str__(self):
        return f"ID: {self.__id}, Valor da multa: {self.__multa}, Item: {self.__item}, " \
               f"Usuário: {self.__usuario}, Data do empréstimo: {self.__dataEmprestimo}, " \
               f"Data esperada de devolução: {self.__dataDevolucao}"    