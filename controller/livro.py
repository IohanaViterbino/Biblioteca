from model.livro import Livro
from database.db import _executar

class LivroController: 
    @staticmethod
    def criar_tabela():
        query = """
            CREATE TABLE IF NOT EXISTS livro(
                IdCodigo INTEGER PRIMARY KEY AUTOINCREMENT, 
                titulo TEXT, 
                autor TEXT, 
                editora TEXT, 
                categoria TEXT, 
                edicao TEXT)
            """
        _executar(query)

    # método intermediario para criar um registro na tabela livro, que chama a criação da tabela e faz a query de insert
    @staticmethod
    def adicionar_livro(titulo, autor, editora, categoria, edicao):
        LivroController.criar_tabela()
        query = "INSERT INTO livro (titulo, autor, editora, categoria, edicao) VALUES (?, ?, ?, ?, ?)"
        params = (titulo, autor, editora, categoria, edicao)
        _executar(query, params)
    
    # metodo com a query de sql para update com adaptação para chamadas de métodos de atualização diferentes.
    def _atualizar_coluna(coluna, valor, id):
        query = f"UPDATE usuario SET {coluna} = ? WHERE id = ?"
        params = (valor, id)
        _executar(query, params)

    @staticmethod
    def atualizar_categoria(id, categoria):
        LivroController._atualizar_coluna('categoria', categoria, id)

    # excluir funconário apartir da chave primária
    @staticmethod
    def excluir_livro(id):
        query = "DELETE FROM livro WHERE IdCodigo = ?"
        _executar(query, (id,))

    # listar todas as infos de todos os registros
    @staticmethod
    def get_livros():
        query = "SELECT * FROM livro"
        return _executar(query)

    # buscar todas as infos de registros com id específico, o que no caso resulta num único registro
    @staticmethod
    def get_livro(id):
        query = "SELECT * FROM livro WHERE IdCodigo = ?"
        livro_data = _executar(query, (id,))
        if livro_data:
            livro = Livro(codLivro=livro_data[0][0], titulo=livro_data[0][1],
                          autor=livro_data[0][2], editora=livro_data[0][3], 
                          categoria=livro_data[0][4], edicao=livro_data[0][5])
            return livro
        
        return None