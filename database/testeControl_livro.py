from controller.livro import LivroController

if __name__=='__main__':
    print('Adicionando')   
    LivroController.adicionar_livro("A psicologia das cores", "Alguem aí", "Outra lá", "Metodologia", "2° ed.")
    LivroController.adicionar_livro("Dom Casmurro", "Machado de Assis", "Editora A", "Ficção", "1° ed.")
    LivroController.adicionar_livro("A Arte da Guerra", "Sun Tzu", "Editora B", "Estratégia", "2° ed.")
    LivroController.adicionar_livro("O Senhor dos Anéis", "J.R.R. Tolkien", "Editora C", "Fantasia", "3° ed.")
    LivroController.adicionar_livro("A Revolução dos Bichos", "George Orwell", "Companhia das Letras", "Sátira Política", "5ª edição")
    LivroController.adicionar_livro("Cem Anos de Solidão", "Gabriel García Márquez", "Record", "Realismo Fantástico", "Edição Comemorativa")
    LivroController.adicionar_livro("1984", "George Orwell", "Companhia Editora Nacional", "Ficção Distópica", "10ª edição")

    print("Listando")
    for li in LivroController.get_livros():
        print(li)

    print("Buscar")
    print(LivroController.get_livro(2))

    print('Atulizaaando')
    # LivroController.categoria(4, "sensasionalismo")

    print('Apagando')
    # LivroController.excluir_livro(3)
    # LivroController.get_livros()