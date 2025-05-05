from controllers.conectar_banco import Banco
from models.produto import Produto
from controllers.controle_generico import ControleGenerico

class ControleProduto(ControleGenerico):

    def incluirProduto(self, produto):
        self.incluir(produto)

    def alterarProduto(self, produto):
        self.alterar(produto)

    def deletarProduto(self, produto):
        self.delete(produto)

    def pesquisaCodigo(self, entrada: Produto):
        dados = self.procuraRegistro(entrada)
        if dados:
            return self.converteProduto(dados)
        return None

    def converteProduto(self, entrada):
        produto = Produto()
        produto.codproduto = entrada[0][0]
        produto.nome = entrada[0][1]
        produto.preco = entrada[0][2]
        return produto

    def listarTodosProdutos(self):
        return self.listarTodos(Produto())

    def converteObjeto(self, entrada):
        produto = Produto()
        produto.codproduto = entrada[0]
        produto.nome = entrada[1]
        produto.preco = entrada[2]
        return produto
