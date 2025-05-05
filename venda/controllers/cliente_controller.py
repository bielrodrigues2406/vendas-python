from controllers.conectar_banco import Banco
from models.cliente import Cliente
from controllers.controle_generico import ControleGenerico


class ControleCliente(ControleGenerico):

    def incluirCliente(self, cliente):
        self.incluir(cliente)

    def alterarCliente(self, cliente):
        self.alterar(cliente)

    def deletarCliente(self, cliente):
        self.delete(cliente)

    def pesquisaCodigo(self, entrada: Cliente):
        dados = self.procuraRegistro(entrada)
        if dados:
            return self.converteCliente(dados)
        return None

    def converteCliente(self, entrada):
        cliente = Cliente()
        cliente.codcliente = entrada[0][0]
        cliente.nome = entrada[0][1]
        cliente.endereco = entrada[0][2]
        return cliente

    def listarTodosClientes(self):
        return self.listarTodos(Cliente())

    def converteObjeto(self, entrada):
        cliente = Cliente()
        cliente.codcliente = entrada[0]
        cliente.nome = entrada[1]
        cliente.endereco = entrada[2]
        return cliente
