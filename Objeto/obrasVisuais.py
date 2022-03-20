
class ProducaoAudioVisual:
    def __init__(self, nome, ano_lancamento, classificacao):
        self._nome = nome.title()
        self._ano_lancamento = ano_lancamento
        self._classificacao = classificacao
        self._likes = 0

    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome_filme(self, nome):
        self._nome = nome

    @property
    def ano_lancamento(self):
        return self._ano_lancamento
    @ano_lancamento.setter
    def ano_lancamento(self, ano_lancamento):
        self._ano_lancamento = ano_lancamento 

    @property
    def likes(self):
        return self.__likes
    @likes.setter
    def likes(self):
        self._likes += 1   

class Filme(ProducaoAudioVisual):
    def __init__(self, nome = None, ano_lancamento = None, classificacao = None, duracao = None):
        super().__init__(nome, ano_lancamento, classificacao)
        self.duracao = duracao

    #sempre colocar essa nomeclatura para metodos exclusivos da classe "filha"
    @classmethod
    def metodo_expecifico_para_class(cls):
        pass
    
    #O método estático é acessível a partir da classe e também da instância.
    @staticmethod
    def log():
        pass

    #The __str__ é  uma representação de string de um objeto
    #Podemos ter o __repr__, que é usado para mostrar uma representação que ajude no debug ou log de um código.
    #Esse último vai printar literalmente o que foi definido. (geralmente usado para debugar e gerar log)
    def __str__(self):
        return f'\nNOME: {self._nome}\nANO: {self._ano_lancamento}\nClassificação: {self._classificacao}\nDuração: {self.duracao}m'

class Serie(ProducaoAudioVisual):
    def __init__(self, nome = None, ano_lancamento = None, classificacao = None, temporadas = None):
        super().__init__(nome, ano_lancamento, classificacao)
        self.__temporadas = temporadas

    @property
    def temporadas(self):
        return self.__temporadas
    @temporadas.setter
    def temporadas(self, temporadas):
        self.__temporadas = temporadas 

    def __str__(self):
        return f'\nNOME: {self._nome}\nANO: {self._ano_lancamento}\nClassificação: {self._classificacao}\nTemporadas: {self.temporadas}'

Vingadores = Filme("vingadores guerra de ultron", "2017", "14", "160")
TheWalkingDead = Serie("the walking dead", "2014", "18", "9")

listaUsuario = [Vingadores, TheWalkingDead]

for programa  in listaUsuario:
    print(programa)
