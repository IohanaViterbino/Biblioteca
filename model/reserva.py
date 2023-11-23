from database.db import _executar

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

    query = "CREATE TABLE IF NOT EXISTS reserva (idReserva INTEGER PRIMARY KEY AUTOINCREMENT, idUsuario INTEGER NOT NULL, idItem INTEGER NOT NULL)"
    _executar(query)

    def salvar(self):
        query= f"INSERT INTO reserva(idUsuario, idItem) VALUES ({int(self.__idUsuario)}, {int(self.__codItem)})"
        _executar(query)

    def excluirReserva(self):
        query= f"DELETE FROM reserva WHERE idReserva = '{int(self.__idReserva)}'"
        _executar(query)

    @staticmethod
    def getReservas():
        query= "SELECT * FROM reserva"
        reservas= _executar(query)
        return reservas
    
    @staticmethod
    def getReserva(id):
        query= f"SELECT * FROM reserva WHERE idReserva = {int(id)}"
        reserva= _executar(query)[0]
        reserva= Reserva(id=reserva[0], usuario=reserva[1], item=reserva[2])
        return reserva
    
    
    def __str__(self):
        return f"Id da Reserva: {self.__idUsuario}, Id do Usuario: {self.__idUsuario}, Id do Item: {self.__codItem}"