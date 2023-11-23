from database.db import _executar

class Livro:
    def __init__(self, titulo, autor, editora, categoria, edicao, codLivro=None):
        self.__titulo = titulo
        self.__autor = autor
        self.__editora = editora
        self.__categoria = categoria
        self.__edicao = edicao
        self.__codLivro = codLivro

    # Getters
    def get_titulo(self):
        return self.__titulo
    def get_autor(self):
        return self.__autor
    def get_editora(self):
        return self.__editora
    def get_categoria(self):
        return self.__categoria
    def get_edicao(self):
        return self.__edicao
    def get_codLivro(self):
        return self.__codLivro
    # Setters
    def set_titulo(self, titulo):
        self.__titulo = titulo
    def set_autor(self, autor):
        self.__autor = autor
    def set_editora(self, editora):
        self.__editora = editora
    def set_categoria(self, categoria):
        self.__categoria = categoria
    def set_edicao(self, edicao):
        self.__edicao = edicao
    def set_codLivro(self, cod):
        self.__codLivro = cod

    query = "CREATE TABLE IF NOT EXISTS livro(IdCodigo INTEGER PRIMARY KEY AUTOINCREMENT, titulo TEXT, autor TEXT, editora TEXT, categoria TEXT, edicao TEXT)"
    _executar(query)

    def salvar(self):
        query = f"INSERT INTO livro (titulo, autor, editora, categoria, edicao) VALUES ('{self.__titulo}','{self.__autor}','{self.__editora}','{self.__categoria}','{self.__edicao}')"
        _executar(query)

    def alterarCategoria(self):
        query = f"""
                UPDATE livro SET categoria = '{self.__categoria}'
                WHERE IdCodigo = '{int(self.__codLivro)}'
                """
        _executar(query)

    def excluirLivro(self):
        query=f"DELETE FROM livro WHERE IdCodigo = '{int(self.__codLivro)}'"
        _executar(query)

   #buscar livros
    @staticmethod
    def getLivros():
        query="SELECT * FROM livro"
        livros=_executar(query)
        return livros

    @staticmethod
    def getLivro(id):
        query = f"""
                SELECT * FROM livro
                WHERE idCodigo ='{int(id)}'
                """
        livro=_executar(query)[0]
        livro=Livro(codLivro=livro[0], titulo=livro[1], autor=livro[2], editora=livro[3], categoria=livro[4], edicao=livro[5])
        return livro

    def __str__(self):
        return (
            f"Código Livro: {self.__codLivro}, Título: {self.__titulo}, Autor: {self.__autor}, "
            f"Editora: {self.__editora}, Categoria: {self.__categoria}, Edição: {self.__edicao}"
        )
