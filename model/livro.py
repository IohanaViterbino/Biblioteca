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

    def __str__(self):
        return (
            f"Código Livro: {self.__codLivro}, Título: {self.__titulo}, Autor: {self.__autor}, "
            f"Editora: {self.__editora}, Categoria: {self.__categoria}, Edição: {self.__edicao}"
        )
