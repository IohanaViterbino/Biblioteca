from model.tablet import Tablet

class AdicionarTablet:
    @staticmethod
    def post(marca, modelo, memoria, so):
        tablet= Tablet(marca, modelo, memoria, so)
        tablet.salvar()

class ApagarTablet:
    @staticmethod
    def get(id):
        tablet= Tablet.getTablet(id)
        tablet.excluirTablet()

class ListarTablet:
    @staticmethod
    def get():
        tablets= Tablet.getTablets()
        for tablet in tablets:
            print(tablet)

class BuscarTablet:
    @staticmethod
    def get(id):
        print(Tablet.getTablet(id))