class Carta:
    '''Classe para criar uma carta com número, naipe e valor'''
    def __init__(self, numero, naipe, valor):
        self.__numero = numero
        self.__naipe = naipe
        self.__valor = valor

    def getNaipe(self): 
        ''' retorna naipe de cada carta'''
        return self.__naipe

    def mostrarNumeracao(self): 
        ''' retorna o número de cada carta'''
        return self.__numero

    def mostrarValor(self): 
        '''retorna o valor de cada carta'''
        return self.__valor

    def __str__(self):
        return f'{self.__numero} de {self.__naipe} e de valor {self.__valor}'
