from database.db import _executar

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

    query="CREATE TABLE IF NOT EXISTS usuario(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, telefone TEXT, tipo NUMERIC, limiteLivros NUMERIC, inadimplente NUMERIC, ativo NUMERIC)"
    _executar(query)

    def salvar(self):
        query = f"""
                INSERT INTO usuario (nome, telefone, tipo, limiteLivros, inadimplente, ativo)
                VALUES ('{self.__nome}','{self.__telefone}','{int(self.__tipo)}',{int(self.__limiteLivros)},{int(self.__inadimplente)}, {int(self.__ativo)})
                """
        _executar(query)
    
    def alterarTelfone(self):
        query = f"""
                UPDATE usuario SET telefone = {self.__telefone}
                WHERE id = {int(self.__matricula)}
                """
        _executar(query)
    
    def alterarInadimplencia(self):
        query = f"""
                UPDATE usuario SET inadimplente = {int(self.__inadimplente)}
                WHERE id = {int(self.__matricula)}
                """
        _executar(query)
    
    def alterarAtividade(self):
        query = f"""
                UPDATE usuario SET ativo = {int(self.__ativo)}
                WHERE id = {int(self.__matricula)}
                """
        _executar(query)
        
    def alterarLimite(self):
        query = f"""
                UPDATE usuario SET limiteLivros = {int(self.__limiteLivros)}
                WHERE id = {int(self.__matricula)}
                """
        _executar(query)

    def excluirUsuario(self):
        query=f"DELETE FROM usuario WHERE id = {int(self.__matricula)}"
        _executar(query)

    @staticmethod
    #listar todos os professores cadastrados
    def getUsuarios():
        query = f"""
                SELECT * FROM usuario
                """
        usuarios=_executar(query)
        return usuarios
        
   #buscar um professor especifico
    @staticmethod
    def getUsuario(id):
        query = f"""
                SELECT*FROM usuario
                WHERE id = {int(id)}
                """
        usuario=_executar(query)[0]
        usuario=Usuario(matricula=usuario[0], nome=usuario[1], telefone=usuario[2], tipo=usuario[3], limite=usuario[4], inadimplente=usuario[5], ativo=usuario[6])
        return usuario

    def __str__(self):
        tipo_usuario = 'Aluno' if self.__tipo == 0 else 'Professor'
        return (
            f"Nome: {self.__nome}, Matrícula: {self.__matricula}, Telefone: {self.__telefone}, "
            f"Ativo: {self.__ativo}, Inadimplente: {self.__inadimplente}, Tipo: {tipo_usuario}, "
            f"Limite de Livros: {self.__limiteLivros}"
        )
