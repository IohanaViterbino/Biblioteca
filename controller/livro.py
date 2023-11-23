from model.livro import Livro

class AdicionarLivro:
    @staticmethod
    def adicionar_livro(titulo, autor, editora, categoria, edicao):
        livro = Livro(titulo, autor, editora, categoria, edicao)
        livro.salvar()

class AtualizarLivro:
    @staticmethod
    def alterar_categoria_livro(cod_livro, categoria):
        livro = Livro.getLivro(cod_livro)
        livro.set_categoria(categoria)
        livro.alterarCategoria()

class ApagarLivro:
    @staticmethod
    def excluir_livro(cod_livro):
        livro = Livro.getLivro(cod_livro)
        livro.excluirLivro()

class ListarLivro:    
    @staticmethod
    def listar_livros():
        print(Livro.getLivros())

class BuscarLivro:
    @staticmethod
    def buscar_livro(cod_livro):
        print(Livro.getLivro(cod_livro))
