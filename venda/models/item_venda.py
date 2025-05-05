class ItemVenda:
    def __init__(self):
        self.__codvenda = 0
        self.__codproduto = 0
        self.__qtde = 0
        self.__valor = 0.0
        self.__lista = 'codvenda,codproduto,qtde,valor'
        self.__tabelaBanco = 'itemvenda'

    @property
    def lista(self):
        return self.__lista

    @property
    def dadosInserir(self):
        return f"{self.codvenda}, {self.codproduto}, {self.qtde}, {self.valor}"

    @property
    def dadosUpdate(self):
        return f"qtde={self.qtde}, valor={self.valor} WHERE codvenda={self.codvenda} AND codproduto={self.codproduto}"

    @property
    def dadosDelete(self):
        return f"WHERE codvenda={self.codvenda} AND codproduto={self.codproduto}"

    @property
    def dadosPesquisa(self):
        return f"SELECT * FROM itemvenda WHERE codvenda={self.codvenda} AND codproduto={self.codproduto}"

    @property
    def tabelaBanco(self):
        return self.__tabelaBanco

    @property
    def codvenda(self): return self.__codvenda
    @codvenda.setter
    def codvenda(self, v): self.__codvenda = v

    @property
    def codproduto(self): return self.__codproduto
    @codproduto.setter
    def codproduto(self, v): self.__codproduto = v

    @property
    def qtde(self): return self.__qtde
    @qtde.setter
    def qtde(self, v): self.__qtde = v

    @property
    def valor(self): return self.__valor
    @valor.setter
    def valor(self, v): self.__valor = v

    def __repr__(self):
        return f"Produto {self.codproduto} - Qtde: {self.qtde} - R$ {self.valor:.2f}"
