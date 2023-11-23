from controller.livro import AdicionarLivro, BuscarLivro, ListarLivro

if __name__=='__main__':
    print('Adicionando')   
    AdicionarLivro.adicionar_livro("A psicologia das cores", "Alguem aí", "Outra lá", "Metodologia", "2° ed.")
    AdicionarLivro.adicionar_livro("Dom Casmurro", "Machado de Assis", "Editora A", "Ficção", "1° ed.")
    AdicionarLivro.adicionar_livro("A Arte da Guerra", "Sun Tzu", "Editora B", "Estratégia", "2° ed.")
    AdicionarLivro.adicionar_livro("O Senhor dos Anéis", "J.R.R. Tolkien", "Editora C", "Fantasia", "3° ed.")
    AdicionarLivro.adicionar_livro("A Revolução dos Bichos", "George Orwell", "Companhia das Letras", "Sátira Política", "5ª edição")
    AdicionarLivro.adicionar_livro("Cem Anos de Solidão", "Gabriel García Márquez", "Record", "Realismo Fantástico", "Edição Comemorativa")
    AdicionarLivro.adicionar_livro("1984", "George Orwell", "Companhia Editora Nacional", "Ficção Distópica", "10ª edição")

    print("Listando")
    ListarLivro.listar_livros()

    print("Buscar")
    BuscarLivro.buscar_livro(2)

    print('Atulizaaando')
    # Atualizar.alterar_categoria_livro(4, "sensasionalismo")

    print('Apagando')
    # Apagar.excluir_livro(3)
    # Listar.listar_livros()