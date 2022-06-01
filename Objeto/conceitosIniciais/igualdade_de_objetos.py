class ContaSalario:

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    #definição sua, quando um objeto é igual ao outro, quando codigo é igual ou quando tudo é igual?
    def __eq__(self, outro):
        if type(outro) != type(self):
            return False
        return self._codigo == outro._codigo and self._saldo == outro._saldo

    def __str__(self):
        return "[>>CODIGO{} Saldo{}<<]".format(self._codigo, self._saldo)

conta1 = ContaSalario(37)
conta2 = ContaSalario(37)
conta1.deposita(100)
print(conta1 == conta2)