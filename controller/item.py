from model.item import Item
from database.db import _executar

class ItemController:
    def criar_tabela():
        query = """
                CREATE TABLE IF NOT EXISTS item (
                    codigo INTEGER PRIMARY KEY AUTOINCREMENT,
                    disponivel NUMERIC NOT NULL,
                    dataAquisicao DATE NOT NULL,
                    idLivro NUMERIC,
                    idTablet NUMERIC
                )
                """
        _executar(query)
    '''
    método intermediario para criar um registro na tabela usuario, que chama a criação da tabela
    e caso seja livro ou tablet chama o método de insert do registro adaptável para as respectivas colunas
    '''
    @staticmethod
    def adicionar_item(tipo, codLivroTablet):
        ItemController.criar_tabela()
        item = Item(codLivroTablet)

        if tipo == 'livro':
            ItemController.salvar(item, 'idLivro')
        elif tipo == 'tablet':
            ItemController.salvar(item, 'idTablet')

    def salvar(objeto, campo_id):
        query = f"""
                INSERT INTO item (dataAquisicao, {campo_id}, disponivel)
                VALUES (?, ?, ?)
                """
        params = (objeto.get_dataAquisicao(), objeto.get_livroTablet(), objeto.get_disponivel())
        _executar(query, params)

    # metodo com a query de sql para update com adaptação para chamadas de métodos de atualização diferentes.
    def _atualizar_coluna(coluna, valor, id):
        query = f"UPDATE usuario SET {coluna} = ? WHERE id = ?"
        params = (valor, id)
        _executar(query, params)

    @staticmethod
    def atualizar_disponibilidade(id, disponibilidade):
        ItemController._atualizar_coluna('disponivel', disponibilidade, id)

    # excluir funconário apartir da chave primária
    @staticmethod
    def excluir_item(id):
        query=f"DELETE FROM item WHERE Codigo = ?"
        _executar(query, (id,))

    # listar todas as infos de todos os registros
    @staticmethod
    def get_itens():
        query="SELECT * FROM item"
        itens=_executar(query)
        return itens

    # buscar todas as infos de registros com id específico, o que no caso resulta num único registro
    @staticmethod
    def get_item(tipo, id):
        campo_id = 'idLivro' if tipo == 'livro' else 'idTablet'
        query = f"""
                SELECT codigo, dataAquisicao, {campo_id}, disponivel FROM item
                WHERE codigo = ?
                """
        item_data = _executar(query, (int(id),))
        if item_data:
            item= Item(codigo=item_data[0][0], livroOUtablet=item_data[0][2], 
                       disponivel=item_data[0][3])
            return item
        
        return None