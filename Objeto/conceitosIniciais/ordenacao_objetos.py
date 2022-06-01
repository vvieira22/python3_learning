from functools import total_ordering

@total_ordering
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

    #para pode usar > < entre objetos.
    def __lt__(self, outro):
        if(self._saldo != outro._saldo):
            return self._saldo < outro._saldo
        return self._codigo < outro._codigo
        
conta_vitor = ContaSalario(37)
conta_vitor.deposita(100)

conta_matheus = ContaSalario(10)
conta_matheus.deposita(100)

lista_contas = [conta_vitor, conta_matheus]

print(conta_vitor >= conta_matheus)
for conta in sorted(lista_contas):
    print(conta)


#ordenar objeto pelo atributo, caso não tenha problema em acessar var privadas.
#em alguns momentos pode precisar, essa abordagem não utiliza objeto em si.
# from operator import attrgetter
# for conta in sorted(lista_contas, key=attrgetter("_saldo")):
#     print(conta)