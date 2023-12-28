from model.registroEmprestimo import RegistroEmprestimo
from controller.usuario import UsuarioController
from controller.item import ItemController
from database.db import _executar

from datetime import datetime, timedelta

class RegistroController:
    def criar_tabela():
        query = """
            CREATE TABLE IF NOT EXISTS registroEmprestimo(
                Id INTEGER PRIMARY KEY AUTOINCREMENT,
                limiteDevolucao INTEGER,    
                valorMulta REAL,
                dataEmprestimo INTEGER, 
                DataEsperada INTEGER, 
                codItem INTEGER, 
                codUsuario INTEGER)
            """
        _executar(query)
    '''
    método de empréstimo, que chama a criação da tabela registroEmprestimo e:
    caso o usuário esteja no banco de dados, esteja ativo e tenha limite de empréstimo disponível
    caso o item esteja no banco de dados, esteja disponível - o resgistro é concluido
    com exceção de que item do tipo 'tablet',
    que só podem ser requeridos por usuários do tipo '1', que são professores/instrutores

    quando o empréstimo é concluído, é atualizado o limite de livro(caso tenha sido um empréstimo de livro)
    e a disponibilidade do item. [o item tablet não possue limite por professor, é só estar disponível]
    '''
    @staticmethod
    def emprestimo(item, usuario, tipo_emprestimo):
        RegistroController.criar_tabela()
        usuario_encontrado = UsuarioController.get_usuario(usuario)
        item_encontrado = ItemController.get_item(tipo_emprestimo, item)

        if not usuario_encontrado or usuario_encontrado.get_ativo() != 1:
            print("Usuário não está ativo na instituição")
            return

        if not item_encontrado or item_encontrado.get_disponivel() != 1:
            print("Item indisponível para empréstimo")
            return

        tipo_usuario = usuario_encontrado.get_tipo()
        limite_livros = usuario_encontrado.get_limiteLivros()

        if tipo_emprestimo == 'livro' and ((tipo_usuario == 0 and limite_livros >= 3) or (tipo_usuario == 1 and limite_livros >= 4)):
            print("Limite de empréstimos atingido. Devolva os anteriores para prosseguir.")
            return

        if tipo_emprestimo == 'tablet' and tipo_usuario != 1:
            print("Aluno não é capaz de fazer um empréstimo de tablet.")
            return

        registro = RegistroEmprestimo(item, usuario)
        RegistroController.salvar(registro)

        if tipo_emprestimo == 'livro':
            UsuarioController.atualizar_limite(usuario_encontrado.get_limiteLivros() + 1, usuario)

        ItemController.atualizar_disponibilidade(item, 0)

    def salvar(objeto):
        query = "INSERT INTO registroEmprestimo(limiteDevolucao, valorMulta, dataEmprestimo, DataEsperada, codItem, codUsuario) VALUES (?, ?, ?, ?, ?, ?)"
        params = (objeto.get_limiteDevolucao(), objeto.get_multa(), objeto.get_dataEmprestimo(), objeto.get_dataDevolucao(), objeto.get_item(), objeto.get_usuario())
        _executar(query, params)

    # calcular o valor da multa de acordo com os dias passados desde o empréstimo
    def calcular_multa(registro):
        data_devolucao = registro.get_dataDevolucao()
        data_atual = datetime.now()
        multa = registro.get_multa()

        if data_atual > data_devolucao:
            diferenca_dias = (data_atual - data_devolucao).days
            multa_total = diferenca_dias * multa
            return multa_total
        return 0

    '''
    método para a renovação, que avalia se a data esperada é menor igual que a atual, para fazer a renovação sem multa;
    calcula a multa caso seja maior que 0, segue para opção de pagar antes de renovar ou parar a transação caso não seja pago
    '''
    @staticmethod
    def renovacao(id):
        registro = RegistroController.get_registro(id)
        data_atual = datetime.now()

        if registro.get_dataDevolucao() <= data_atual:
            multa = RegistroController.calcular_multa(registro)
            if multa > 0:
                print(f"Usuário possui uma multa de R$ {multa:.2f}")
                entrada = input("Deseja pagar agora? (Sim/Não): ")
                if entrada.lower() == 'sim':
                    registro.set_dataDevolucao(data_atual + timedelta(registro.get_limiteDevolucao()))
                    RegistroController.atualizar_devolucao(registro)
                    print("Renovação concluída.")
                else:
                    print("Volte outro dia com o dinheiro para renovação.")
            else:
                registro.set_dataDevolucao(data_atual + timedelta(registro.get_limiteDevolucao()))
                RegistroController.atualizar_devolucao(registro)
                print("Renovação concluída.")
        else:
            registro.set_dataDevolucao(data_atual + timedelta(registro.get_limiteDevolucao()))
            RegistroController.atualizar_devolucao(registro)
            print("Renovação concluída.")

    '''
    método para a devolução, que avalia se a data esperada é menor igual que a atual, para fazer a renovação sem multa;
    calcula a multa caso seja maior que 0, segue para opção de pagar antes de renovar ou parar a transação caso não seja pago
    '''
    @staticmethod
    def devolucao(id):
        registro = RegistroController.get_registro(id)
        data_atual = datetime.now()

        if registro.get_dataDevolucao() <= data_atual:
            multa = RegistroController.calcular_multa(registro)
            if multa > 0:
                print(f"Usuário possui uma multa de R$ {multa:.2f}")
                entrada = input("Deseja pagar agora? (Sim/Não): ").lower()
                if entrada == 'sim':
                    registro.set_dataDevolucao(data_atual)
                    RegistroController.atualizar_devolucao(registro)
                    ItemController.atualizar_disponibilidade(registro.get_item(), 1)
                    print("Devolução concluída.") 
                else:
                    print("Volte outro dia com o dinheiro para devolução.")
            else:
                registro.set_dataDevolucao(data_atual)
                RegistroController.atualizar_devolucao(registro)
                ItemController.atualizar_disponibilidade(registro.get_item(), 1)
                print("Devolução concluída.")
        else:
            registro.set_dataDevolucao(data_atual)
            RegistroController.atualizar_devolucao(registro)
            ItemController.atualizar_disponibilidade(registro.get_item(), 1)
            print("Devolução concluída.")

    # metodo com a query de sql para update com adaptação para chamadas de métodos de atualização diferentes.
    def _atualizar_coluna(coluna, valor, id):
        query = f"UPDATE resgistroEmprestimo SET {coluna} = ? WHERE id = ?"
        params = (valor, id)
        _executar(query, params)

    @staticmethod
    def atualizar_devolucao(objeto):
        RegistroController._atualizar_coluna('DataEsperada', objeto.get_dataDevolucao(), objeto.get_id())

    # excluir funconário apartir da chave primária
    @staticmethod
    def excluir_registro(id):
        query = "DELETE FROM registroEmprestimo WHERE Id = ?"
        _executar(query, (int(id),))
   
    # listar todas as infos de todos os registros
    @staticmethod
    def get_registros():
        query = "SELECT * FROM registroEmprestimo"
        registros = _executar(query)
        return registros
    
    # buscar todas as infos de registros com id específico, o que no caso resulta num único registro
    @staticmethod
    def get_registro(id):
        query = "SELECT * FROM registroEmprestimo WHERE Id = ?"
        registro_data = _executar(query, (id,))

        if registro_data:
            data_esperada = datetime.fromisoformat(registro_data[0][4])
            registro = RegistroEmprestimo(
                id=registro_data[0][0],
                limite=registro_data[0][1],
                vlrMulta=registro_data[0][2],
                dataEmpres=datetime.fromisoformat(registro_data[0][3]),
                item=registro_data[0][5],
                usuario=registro_data[0][6]
            )
            registro.set_dataDevolucao(data_esperada)
            return registro

        return None