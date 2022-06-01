idades = [10,15,67,98,1,2,5,6]

#Pegar valor e index de uma lista
#forma padrão
for i in range(len(idades)):
    print(i, idades[i])

#forma usando enumarate
#desempactoando indice e valor. 
for indice, valor in enumerate(idades):
    print(indice,valor)

# _ vai ignorar, não é legal, é melhor saber quem ta sendo passado.
for indice, _ in enumerate(idades):
    print(indice)