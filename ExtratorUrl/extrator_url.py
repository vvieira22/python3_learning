url = "http://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"

indice_interrogacao = url.find("?")
url_base = url[0:indice_interrogacao]
url_parametros = url[indice_interrogacao+1:]

print(url_base)
print(url_parametros)

