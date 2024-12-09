class Conta:
    def __init__(self, titular, numero):
        self._saldo = 1000
        self._numero = numero
        self._titular = titular

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        if (saldo < 0):
            print("O saldo não pode ficar negativo")
        else:
            self._saldo = saldo

    def saque(self, valor):
        if (self.saldo >= valor):
            self.saldo -= valor
            print('Saldo realizado com sucesso')
        else:
            print('Saldo insuficiente')

    def deposita(self,valor):
        self.saldo += valor

    def extrato(self):
        print("cliente ", self._titular, " Saldo Atual: ", self._saldo)