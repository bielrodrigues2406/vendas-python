class Cliente:
    def __init__(self):
        self.__codcliente = 0
        self.__nome = ""
        self.__endereco = ""
        self.__lista = 'nome,endereco'
        self.__tabelaBanco = 'cliente'

    @property
    def lista(self):
        return self.__lista

    @property
    def dadosInserir(self):
        return f"'{self.nome}','{self.endereco}'"

    @property
    def dadosUpdate(self):
        return f"nome='{self.nome}', endereco='{self.endereco}' WHERE codcliente={self.codcliente}"

    @property
    def dadosDelete(self):
        return f"WHERE codcliente={self.codcliente}"

    @property
    def dadosPesquisa(self):
        return f"SELECT * FROM cliente WHERE codcliente={self.codcliente}"

    @property
    def tabelaBanco(self):
        return self.__tabelaBanco

    @property
    def codcliente(self): return self.__codcliente
    @codcliente.setter
    def codcliente(self, v): self.__codcliente = v

    @property
    def nome(self): return self.__nome
    @nome.setter
    def nome(self, v): self.__nome = v

    @property
    def endereco(self): return self.__endereco
    @endereco.setter
    def endereco(self, v): self.__endereco = v

    def __repr__(self):
        return f"{self.nome} - {self.endereco}"
