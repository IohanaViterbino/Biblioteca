
class Usuario():
    def __init__(self, nome, telefone, tipo, limite=0, inadimplente=0, ativo=1, matricula=None):
        super().__init__()
        self.__nome = nome
        self.__matricula = matricula
        self.__telefone = telefone
        self.__ativo = ativo #1- se esta ativo, 0- Não esta ativo na instituição
        self.__inadimplente = inadimplente #1- se tem dívida, 0- Não tem dívida
        self.__tipo = tipo #0- aluno, 1- professor
        self.__limiteLivros = limite
        
    # Getters
    def get_nome(self):
        return self.__nome
    def get_telefone(self):
        return self.__telefone
    def get_tipo(self):
        return self.__tipo
    def get_matricula(self):
        return self.__matricula
    def get_ativo(self):
        return self.__ativo
    def get_limiteLivros(self):
        return self.__limiteLivros
    def get_inadimplente(self):
        return self.__inadimplente

    # Setters
    def set_nome(self, nome):
        self.__nome = nome
    def set_telefone(self, telefone):
        self.__telefone = telefone
    def set_tipo(self, tipo):
        self.__tipo = tipo
    def set_limiteLivros(self, limiteLivros):
        self.__limiteLivros = limiteLivros
    def set_inadimplente(self, inadimplente):
        self.__inadimplente = inadimplente
    def set_matricula(self, m):
        self.__matricula = m
    def set_ativo(self, a):
        self.__ativo = a


    def __str__(self):
        tipo_usuario = 'Aluno' if self.__tipo == 0 else 'Professor'
        return (
            f"Nome: {self.__nome}, Matrícula: {self.__matricula}, Telefone: {self.__telefone}, "
            f"Ativo: {self.__ativo}, Inadimplente: {self.__inadimplente}, Tipo: {tipo_usuario}, "
            f"Limite de Livros: {self.__limiteLivros}"
        )
