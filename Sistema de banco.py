class Main:
    pass


print("Testando o Projeto")

from Cliente import Cliente

from Conta import Conta

c1 = Cliente("João", "114444-2222")
conta = Conta(c1.get_nome(), 1222)

conta.deposita(10)
conta.saque(5)
conta.extrato()

