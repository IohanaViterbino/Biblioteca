from model.reserva import Reserva
from controller.item import ItemController
from database.db import _executar

class ReservaController:
    def criar_tabela():
        query = """
            CREATE TABLE IF NOT EXISTS reserva (
            idReserva INTEGER PRIMARY KEY AUTOINCREMENT, 
            idUsuario INTEGER NOT NULL, 
            idItem INTEGER NOT NULL)
            """
        _executar(query)
        
    '''
    método intermediario para criar um registro na tabela reserva, que chama a criação da tabela
    caso o item a ser reservado esteja indisponível, chama o método de insert do registro
    senão, é apresentado uma mensagem de aviso de empréstimo válido.
    '''
    @staticmethod
    def post(usuarioID, itemID, tipo):
        item_encontrado = ItemController.get_item(tipo,itemID)
        ReservaController.criar_tabela()
        if item_encontrado and item_encontrado.get_disponivel() == 0:
            reserva= Reserva(usuarioID, itemID)
            ReservaController.salvar(reserva)
        else:
            print("Item disponível para empréstimo.")

    def salvar(objeto):
        query = f"INSERT INTO reserva(idUsuario, idItem) VALUES (?, ?)"
        params=(int(objeto.get_idUsuario()), int(objeto.get_codItem()))
        _executar(query, params)

     # excluir funconário apartir da chave primária
    @staticmethod
    def excluir_reserva(id):
        query = f"DELETE FROM reserva WHERE idReserva = ?"
        _executar(query, (id,))

    # listar todas as infos de todos os registros
    @staticmethod
    def get_reservas():
        query= "SELECT * FROM reserva"
        reservas= _executar(query)
        return reservas

    # buscar todas as infos de registros com id específico, o que no caso resulta num único registro
    @staticmethod
    def get_reserva(id):
        query= f"SELECT * FROM reserva WHERE idReserva = ?"
        reserva_data= _executar(query, (id,))
        if reserva_data:
            reserva= Reserva(id=reserva_data[0][0], usuario=reserva_data[0][1],
                             item=reserva_data[0][2])
            return reserva
        
        return None