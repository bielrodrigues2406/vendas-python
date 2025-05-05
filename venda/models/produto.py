class Produto:
    def __init__(self):
        self.__codproduto = 0
        self.__nome = ""
        self.__preco = 0.0
        self.__lista = 'nome,preco'
        self.__tabelaBanco = 'produto'

    @property
    def lista(self):
        return self.__lista

    @property
    def dadosInserir(self):
        return f"'{self.nome}', {self.preco}"

    @property
    def dadosUpdate(self):
        return f"nome='{self.nome}', preco={self.preco} WHERE codproduto={self.codproduto}"

    @property
    def dadosDelete(self):
        return f"WHERE codproduto={self.codproduto}"

    @property
    def dadosPesquisa(self):
        return f"SELECT * FROM produto WHERE codproduto={self.codproduto}"

    @property
    def tabelaBanco(self):
        return self.__tabelaBanco

    @property
    def codproduto(self): return self.__codproduto
    @codproduto.setter
    def codproduto(self, v): self.__codproduto = v

    @property
    def nome(self): return self.__nome
    @nome.setter
    def nome(self, v): self.__nome = v

    @property
    def preco(self): return self.__preco
    @preco.setter
    def preco(self, v): self.__preco = v

    def __repr__(self):
        return f"{self.nome} - R$ {self.preco:.2f}"
