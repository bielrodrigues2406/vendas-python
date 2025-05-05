from controllers.conectar_banco import Banco
from models.venda import Venda
from controllers.controle_generico import ControleGenerico

class ControleVenda(ControleGenerico):

    def incluirVenda(self, venda):
        self.incluir(venda)

    def alterarVenda(self, venda):
        self.alterar(venda)

    def deletarVenda(self, venda):
        self.delete(venda)

    def pesquisaCodigo(self, entrada: Venda):
        dados = self.procuraRegistro(entrada)
        if dados:
            return self.converteVenda(dados)
        return None

    def converteVenda(self, entrada):
        venda = Venda()
        venda.codvenda = entrada[0][0]
        venda.data = entrada[0][1]
        venda.valor_total = entrada[0][2]
        venda.codcliente = entrada[0][3]
        return venda

    def listarTodasVendas(self):
        return self.listarTodos(Venda())

    def converteObjeto(self, entrada):
        venda = Venda()
        venda.codvenda = entrada[0]
        venda.data = entrada[1]
        venda.valor_total = entrada[2]
        venda.codcliente = entrada[3]
        return venda
