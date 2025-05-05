from controllers.conectar_banco import Banco
from models.item_venda import ItemVenda
from controllers.controle_generico import (ControleGenerico)

class ControleItemVenda(ControleGenerico):

    def incluirItem(self, item):
        self.incluir(item)

    def alterarItem(self, item):
        self.alterar(item)

    def deletarItem(self, item):
        self.delete(item)

    def pesquisaItem(self, entrada: ItemVenda):
        dados = self.procuraRegistro(entrada)
        if dados:
            return self.converteItem(dados)
        return None

    def converteItem(self, entrada):
        item = ItemVenda()
        item.codvenda = entrada[0][0]
        item.codproduto = entrada[0][1]
        item.qtde = entrada[0][2]
        item.valor = entrada[0][3]
        return item

    def listarTodosItens(self):
        return self.listarTodos(ItemVenda())

    def listarItensPorVenda(self, codvenda):
        self.ob = Banco()
        self.ob.configura("localhost", "root", "ifsp", "vendas_db")
        self.ob.abrirConexao()
        sql = f"SELECT * FROM itemvenda WHERE codvenda = {codvenda}"
        resultado = self.ob.selectQuery(sql)
        return resultado

    def converteObjeto(self, entrada):
        item = ItemVenda()
        item.codvenda = entrada[0]
        item.codproduto = entrada[1]
        item.qtde = entrada[2]
        item.valor = entrada[3]
        return item
