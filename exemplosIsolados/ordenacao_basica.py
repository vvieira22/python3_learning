#Ordenação básica
#======================================#
idades = [10,15,67,98,1,2,5,6]

idades_ordenada = sorted(idades)
idades_ordenada_ao_contrario = sorted(idades, reverse=True)
idades_ao_contrario = list(reversed(idades)) #nao devolve ainda, precisa chamar list
#isso é chamado de lazy. Lazy é apenas uma maneira de converter expressões em uma árvore 
# de objetos de computação adiados chamados thunks .
#  Thunks envolvem funções normais não avaliando-as até que o valor seja necessário

print(idades_ordenada_ao_contrario)

#lista já tem sorted implementado, sendo assim nao precisa

idades.sort()
print(idades)
#======================================#