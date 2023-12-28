from model.tablet import Tablet
from database.db import _executar

class TabletController:
    def criar_tabela():
        query = """
                CREATE TABLE IF NOT EXISTS tablet(
                    codigo INTEGER PRIMARY KEY AUTOINCREMENT, 
                    marca TEXT NOT NULL, 
                    modelo TEXT NOT NULL, 
                    memoria TEXT NOT NULL, 
                    so TEXT NOT NULL)
                """
        _executar(query)

    # método intermediario para criar um registro na tabela tablet, que chama a criação da tabela e o insert do registro
    @staticmethod
    def post(marca, modelo, memoria, so):
        TabletController.criar_tabela()

        tablet= Tablet(marca, modelo, memoria, so)
        TabletController.salvar(tablet)

    def salvar(objeto):
        query = """
                INSERT INTO tablet
                (marca, modelo, memoria, so)
                VALUES (?,?,?,?)
                """
        params=(objeto.get_marca(),objeto.get_modelo(),objeto.get_memoria(),objeto.get_so())
        _executar(query,params)

    # excluir funconário apartir da chave primária
    @staticmethod
    def excluir_tablet(id):
        query = f"DELETE FROM tablet WHERE codigo = ?"
        _executar(query,(id,))

    # listar todas as infos de todos os registros
    @staticmethod
    def get_tablets():
        query="SELECT * FROM tablet"
        tablets=_executar(query)
        return tablets

    # buscar todas as infos de registros com id específico, o que no caso resulta num único registro
    @staticmethod
    def get_tablet(id):
        query = "SELECT * FROM tablet WHERE codigo = ?"
        tablet_data=_executar(query,(id,))
        if tablet_data:
            tablet=Tablet(cod=tablet_data[0][0], marca=tablet_data[0][1],
                               modelo=tablet_data[0][2], memoria=tablet_data[0][3],
                               so=tablet_data[0][4])
            return tablet

        return None
