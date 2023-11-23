from database.db import _executar

class Tablet:
    def __init__(self, marca, modelo, memoria, so, cod=None):
        self.__marca = marca
        self.__modelo = modelo
        self.__memoria = memoria
        self.__so = so
        self.__cod = cod

    # Getters
    def get_marca(self):
        return self.__marca
    def get_modelo(self):
        return self.__modelo
    def get_memoria(self):
        return self.__memoria
    def get_so(self):
        return self.__so
    def get_cod(self):
        return self.__cod
    # Setters
    def set_marca(self, marca):
        self.__marca = marca
    def set_modelo(self, modelo):
        self.__modelo = modelo
    def set_memoria(self, memoria):
        self.__memoria = memoria
    def set_so(self, so):
        self.__so = so
    def set_cod(self, cod):
        self.__cod = cod

    query = "CREATE TABLE IF NOT EXISTS tablet (codigo INTEGER PRIMARY KEY AUTOINCREMENT, marca TEXT NOT NULL, modelo TEXT NOT NULL, memoria TEXT NOT NULL, so TEXT NOT NULL)"
    _executar(query)

    def salvar(self):
        query = f"INSERT INTO tablet (marca, modelo, memoria, so) VALUES ('{self.__marca}', '{self.__modelo}', '{self.__memoria}', '{self.__so}')"
        _executar(query)

    def excluirTablet(self):
        query=f"DELETE FROM tablet WHERE codigo = '{int(self.__cod)}'"
        _executar(query)

    @staticmethod
    def getTablets():
        query="SELECT * FROM tablet"
        tablets=_executar(query)
        return tablets

    @staticmethod
    def getTablet(id):
        query = f"""
                SELECT * FROM tablet
                WHERE codigo ='{int(id)}'
                """
        tablet=_executar(query)[0]
        tablet=Tablet(cod=tablet[0], marca=tablet[1], modelo=tablet[2], memoria=tablet[3], so=tablet[4])
        return tablet

    def __str__(self):
        return f"Código: {self.__cod}, Marca: {self.__marca}, Modelo: {self.__modelo}, Memória: {self.__memoria}, Sistema Operacional: {self.__so}"
