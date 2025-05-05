class Venda:
    def __init__(self):
        self.__codvenda = 0
        self.__data = ""
        self.__valor_total = 0.0
        self.__codcliente = 0
        self.__lista = 'data,valor_total,codcliente'
        self.__tabelaBanco = 'venda'

    @property
    def lista(self):
        return self.__lista

    @property
    def dadosInserir(self):
        return f"'{self.data}', {self.valor_total}, {self.codcliente}"

    @property
    def dadosUpdate(self):
        return f"data='{self.data}', valor_total={self.valor_total}, codcliente={self.codcliente} WHERE codvenda={self.codvenda}"

    @property
    def dadosDelete(self):
        return f"WHERE codvenda={self.codvenda}"

    @property
    def dadosPesquisa(self):
        return f"SELECT * FROM venda WHERE codvenda={self.codvenda}"

    @property
    def tabelaBanco(self):
        return self.__tabelaBanco

    @property
    def codvenda(self): return self.__codvenda
    @codvenda.setter
    def codvenda(self, v): self.__codvenda = v

    @property
    def data(self): return self.__data
    @data.setter
    def data(self, v): self.__data = v

    @property
    def valor_total(self): return self.__valor_total
    @valor_total.setter
    def valor_total(self, v): self.__valor_total = v

    @property
    def codcliente(self): return self.__codcliente
    @codcliente.setter
    def codcliente(self, v): self.__codcliente = v

    def __repr__(self):
        return f"Venda {self.codvenda} - Cliente {self.codcliente} - Total: R$ {self.valor_total:.2f}"
