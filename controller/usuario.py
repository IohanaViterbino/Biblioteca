from model.usuario import Usuario

class AdicionarUsuario:
    @staticmethod
    def post(nome, telefone, tipo):
        usuario = Usuario(nome, telefone, tipo)
        usuario.salvar()

class AtualizarUsuario:
    @staticmethod
    def telefone(id, telefone):
        usuario= Usuario.getUsuario(id)
        usuario.set_telefone(telefone)
        usuario.alterarTelfone()

    @staticmethod
    def limite(id):
        usuario= Usuario.getUsuario(id)
        usuario.set_limiteLivros(usuario.get_limiteLivros()+1)
        usuario.alterarLimite()

    @staticmethod
    def ativo(id, ativo):
        usuario= Usuario.getUsuario(id)
        usuario.set_ativo(ativo)
        usuario.alterarAtividade()

    @staticmethod
    def inadimplencia(id, inadimplente):
        usuario= Usuario.getUsuario(id)
        usuario.set_inadimplente(inadimplente)
        usuario.alterarInadimplencia()

class ApagarUsuario:
    @staticmethod
    def get(id):
        usuario=Usuario.getUsuario(id)
        usuario.excluirUsuario()

class ListarUsuario:
    @staticmethod
    def get():
        usuarios= Usuario.getUsuarios()
        for usuario in usuarios:
            print(usuario)

class BuscarUsuario:
    @staticmethod
    def get(id):
        return Usuario.getUsuario(id)