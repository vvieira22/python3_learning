lista_usuarios_java = [10,34,56,30]
lista_usuarios_python = [13,34,16,42]

lista_todos_usuarios = lista_usuarios_java + lista_usuarios_python
print(lista_todos_usuarios)

'''Se eu quiser enviar um email para cada usuario sobre linguagem nova, vou enviar
2x para o aluno 34, pq ele é duplicado na junção da lista.
    Por isso vamos usar o set. tradução = conjunto, ele vai sempre ignorar dados com mesmo valor.
geralmente usado, quando o ACESSO A ESSE DADO NÃO PRECISA SE SEQUENCIAL, ou seja a ordem não importa e não tem posição.
ELE SÓ TEM OS ELEMENTOS E PRONTO.'''

lista_todos_usuarios = set(lista_todos_usuarios)
print(lista_todos_usuarios)

#Para juntarmos dados e nao se repetir usando set, podemos fazer assim:
lista_usuarios_java = {10,34,56,30}
lista_usuarios_python = {13,34,16,42}

print(lista_usuarios_java & lista_usuarios_python)

#podemos adicionar elementos no conjunto
lista_usuarios_java.add(99)
print(lista_usuarios_java)

#podemos congelar o conjunto para não ser mais alterado e modificado.
lista_usuarios_java_congelado = frozenset(lista_usuarios_java)

#Podemos usar também conjuntos com textos
my_text = "texto maneiro e muito legal".split()
conjunto_my_text = set(my_text)
print(conjunto_my_text)