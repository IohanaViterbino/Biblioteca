from model.usuario import Usuario
from database.db import _executar

class UsuarioController:
    def criar_tabela():
        query = """
                CREATE TABLE IF NOT EXISTS usuario(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT,
                    telefone TEXT,
                    tipo NUMERIC,
                    limiteLivros NUMERIC,
                    inadimplente NUMERIC,
                    ativo NUMERIC
                )
                """
        _executar(query)

    # método intermediario para criar um registro na tabela usuario, que chama a criação da tabela e o insert do registro
    @staticmethod
    def post(nome, telefone, tipo):
        UsuarioController.criar_tabela()

        usuario = Usuario(nome, telefone, tipo)
        UsuarioController.salvar(usuario)

    def salvar(objeto):
        query = """
                INSERT INTO usuario (nome, telefone, tipo, limiteLivros, inadimplente, ativo)
                VALUES (?, ?, ?, ?, ?, ?)
                """
        params = (objeto.get_nome(), objeto.get_telefone(), objeto.get_tipo(),
                  objeto.get_limiteLivros(), objeto.get_inadimplente(), objeto.get_ativo())
        _executar(query, params)

    # metodo com a query de sql para update com adaptação para chamadas de métodos de atualização diferentes.
    def _atualizar_coluna(coluna, valor, id):
        query = f"UPDATE usuario SET {coluna} = ? WHERE id = ?"
        params = (valor, id)
        _executar(query, params)

    @staticmethod
    def atualizar_telefone(id, telefone):
        UsuarioController._atualizar_coluna('telefone', telefone, id)

    @staticmethod
    def atualizar_limite(id, limite):
        UsuarioController._atualizar_coluna('limiteLivros', limite, id)

    @staticmethod
    def atualizar_inadimplencia(id, inadimplente):
        UsuarioController._atualizar_coluna('inadimplente', inadimplente, id)

    @staticmethod
    def atualizar_ativo(id, ativo):
        UsuarioController._atualizar_coluna('ativo', ativo, id)

    # excluir funconário apartir da chave primária
    @staticmethod
    def excluir_usuario(id):
        query = "DELETE FROM usuario WHERE id = ?"
        _executar(query, (id,))

    # listar todas as infos de todos os registros
    @staticmethod
    def get_usuarios():
        query = "SELECT * FROM usuario"
        return _executar(query)

    # buscar todas as infos de registros com id específico, o que no caso resulta num único registro
    @staticmethod
    def get_usuario(id):
        query = "SELECT * FROM usuario WHERE id = ?"
        usuario_data = _executar(query, (id,))
        if usuario_data:
            usuario = Usuario(matricula=usuario_data[0][0], nome=usuario_data[0][1],
                              telefone=usuario_data[0][2], tipo=usuario_data[0][3],
                              limite=usuario_data[0][4], inadimplente=usuario_data[0][5],
                              ativo=usuario_data[0][6])
            return usuario
        
        return None
