import random

from Carta import Carta


class Baralho:
    '''Classe para criar o baralho inicial, tipo list '''
    def __init__(self):
        self.__baralho = list()
        naipe = ["Ouro", "Espada", "Paus", "Copas"]
        numeracao = [
            "Ás", "2", "3", "4", "5", "6", "7", "8", "9", "10", "valete",
            "dama", "rei"
        ]
        valor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

        for idx in range(len(naipe)):
            for id in range(len(numeracao)):
                self.__baralho.append(
                    Carta(numeracao[id], naipe[idx], valor[id]))

    def numCartas(self):
        '''retorna a quantidade de cartas do baralho inicial'''
        return len(self.__baralho)

    def embaralharar(self):
        '''método para embaralhar o baralho inicial'''
        return random.shuffle(self.__baralho)

    def temCarta(self):
        '''sinalizar se tem carta ou não no baralho'''
        return self.numCartas() > 0

    def retirarCartas(self):
        '''tira uma carta do baralho inicial'''
        return self.__baralho.pop()

    def receberCarta(self, carta):
        '''adicionar carta no final do baralho inicial'''
        self.__baralho.append(carta)

    def __str__(self):
        saida = ''
        for carta in self.__baralho:
            saida += carta.__str__() + '\n'
        return saida
