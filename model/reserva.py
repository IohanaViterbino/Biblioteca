class Reserva:
    def __init__(self, usuario, item, id=None):
        self.__idUsuario = usuario
        self.__codItem = item
        self.__idReserva = id

    # Getters
    def get_idUsuario(self):
        return self.__idUsuario
    def get_codItem(self):
        return self.__codItem
    def get_idReserva(self):
        return self.__idReserva

    # Setters
    def set_idUsuario(self, usuario):
        self.__idUsuario = usuario
    def set_codItem(self, item):
        self.__codItem = item
    def set_idReserva(self, id):
        self.__idReserva = id   
    
    def __str__(self):
        return f"Id da Reserva: {self.__idUsuario}, Id do Usuario: {self.__idUsuario}, Id do Item: {self.__codItem}"