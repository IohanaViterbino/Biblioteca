from model.reserva import Reserva
from controller.item import BuscarItem

class AdicionarReserva:
    @staticmethod
    def post(usuario, item):
        item_encontrado = BuscarItem.getLivro(item)
        if item_encontrado and item_encontrado.get_disponivel() == 0:
            reserva= Reserva(usuario, item)
            reserva.salvar()
        else:
            print("Item disponível para empréstimo.")

class ApagarReserva:
    @staticmethod
    def get(id):
        reserva= Reserva.getReserva(id)
        reserva.excluirReserva()

class ListarReserva:
    @staticmethod
    def get():
        reservas= Reserva.getReservas()
        for reserva in reservas:
            print(reserva)

class BuscarReserva:
    @staticmethod
    def get(id):
        print(Reserva.getReserva(id))