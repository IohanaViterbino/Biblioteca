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

    def __str__(self):
        return f"Código: {self.__cod}, Marca: {self.__marca}, Modelo: {self.__modelo}, Memória: {self.__memoria}, Sistema Operacional: {self.__so}"
