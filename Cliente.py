class Cliente:
    def __init__(self, n, fone):

        self._nome = n
        self._telefone = fone

    #Metodo Get
    def get_nome(self):
        return self._nome

    #metodo Set
    def set_nome(self, nome):
        self._nome = nome
