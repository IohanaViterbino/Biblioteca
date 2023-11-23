from model.registroEmprestimo import RegistroEmprestimo
from controller.usuario import AtualizarUsuario, BuscarUsuario
from controller.item import AtualizarItem, BuscarItem

from datetime import datetime, timedelta

class AdicionarRegistro:
    @staticmethod
    def postLivro(vlrMulta, item, usuario):
        usuario_encontrado = BuscarUsuario.get(usuario)
        item_encontrado = BuscarItem.getLivro(item)

        if usuario_encontrado and usuario_encontrado.get_ativo() == 1:
            if item_encontrado and item_encontrado.get_disponivel() == 1:
                tipo_usuario = usuario_encontrado.get_tipo()
                limite_livros = usuario_encontrado.get_limiteLivros()

                if (tipo_usuario == 0 and limite_livros < 3) or (tipo_usuario == 1 and limite_livros < 4):
                    registro = RegistroEmprestimo(vlrMulta, item, usuario)
                    registro.salvar()
                    AtualizarUsuario.limite(usuario)
                    AtualizarItem.disponibilidade_Livro(item, 0)
                else:
                    print("Limite de empréstimos atingido. Devolva os anteriores para prosseguir.")
            else:
                print("Item indisponível para empréstimo")
        else:
            print("Usuário não está ativo na instituição")

    @staticmethod
    def postTablet(vlrMulta, item, usuario):
        usuario_encontrado = BuscarUsuario.get(usuario)
        item_encontrado = BuscarItem.getLivro(item)

        if usuario_encontrado and usuario_encontrado.get_ativo() == 1:
            if item_encontrado and item_encontrado.get_disponivel() == 1:
                tipo_usuario = usuario_encontrado.get_tipo()

                if tipo_usuario == 1:
                    registro = RegistroEmprestimo(vlrMulta, item, usuario)
                    registro.salvar()
                    AtualizarItem.disponibilidade_Tablet(item, 0)
                else:
                    print("Aluno não é capaz fazer um empréstimo de tablet.")
            else:
                print("Item indisponível para empréstimo")
        else:
            print("Usuário não está ativo na instituição")

class AtualizarRegistro:
    @staticmethod
    def calcularMulta(registro):
        data_devolucao = registro.get_dataDevolucao()
        data_atual = datetime.now()
        multa = registro.get_multa()

        if data_atual > data_devolucao:
            diferenca_dias = (data_atual - data_devolucao).days
            multa_total = diferenca_dias * multa
            return multa_total
        return 0

    @staticmethod
    def renovacao(id):
        registro = RegistroEmprestimo.getRegistro(id)
        if registro.get_dataDevolucao() <= datetime.now():
            multa = AtualizarRegistro.calcularMulta(registro)
            if multa > 0:
                print(f"Usuário possui uma multa de R$ {multa:.2f}")
                entrada = input("Deseja pagar agora? (Sim/Não): ")
                if entrada.lower() == 'sim':
                    registro.set_dataDevolucao(datetime.now() + timedelta(registro.get_limiteDevolucao()))
                    registro.alterarDevolucao()
                    print("Renovação concluída.")
                else:
                    print("Volte outro dia com o dinheiro para renovação.")
            else:
                registro.set_dataDevolucao(datetime.now() + timedelta(registro.get_limiteDevolucao()))
                registro.alterarDevolucao()
                print("Renovação concluída.")
        else:
            print("Data de devolução ainda não foi ultrapassada.")

    @staticmethod
    def devolucao(id):
        registro = RegistroEmprestimo.getRegistro(id)
        data_atual = datetime.now()

        if registro.get_dataDevolucao() <= data_atual:
            multa = AtualizarRegistro.calcularMulta(registro)
            if multa > 0:
                print(f"Usuário possui uma multa de R$ {multa:.2f}")
                entrada = input("Deseja pagar agora? (Sim/Não): ").lower()
                if entrada == 'sim':
                    registro.set_dataDevolucao(data_atual)
                    registro.alterarDevolucao()
                    print("Devolução concluída.")
                else:
                    print("Volte outro dia com o dinheiro para devolução.")
            else:
                print("Devolução concluída.")
        else:
            registro.set_dataDevolucao(data_atual)
            registro.alterarDevolucao()
            print("Devolução concluída.")

class ApagarRegistro:
    @staticmethod
    def get(id):
        registro = RegistroEmprestimo.getRegistro(id)
        registro.excluirRegistro()

class ListarRegistro:
    @staticmethod
    def get():
        registros= RegistroEmprestimo.getRegistros()
        for registro in registros:
            print(registro)

class BuscarRegistro:
    @staticmethod
    def get(id):
        print(RegistroEmprestimo.getRegistro(id))