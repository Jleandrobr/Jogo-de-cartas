from PilhaEncadeada import Pilha, Node, PilhaException

class Jogador:
    '''Classe para criar o Jogador com sua pilha sendo o baralho e seu nome'''
    def __init__(self, nome):
        self.__baralhoJ = Pilha()
        self.__nome = nome

    def getNome(self): 
        '''retorna o nome do jogador'''
        return self.__nome
    
    def devolverCartas(self, n, baralho): 
        '''devolve cartas do baralho do Jogador ao baralho inicial'''
        for i in range(n):
            carta = self.__baralhoJ.desempilha()
            baralho.receberCarta(carta)

    def retirarCarta(self, pilha): 
        ''' retira carta do baralho do jogador e empilha em uma outra pilha recebe como parâmetro a pilha que vai ser adicionada as cartas'''
        carta = self.__baralhoJ.desempilha()
        pilha.empilha(carta)

    def mostrarCartas(self):  
        '''método pra mostrar as cartas do baralho do jogador na tela'''
        self.__baralhoJ.imprime()

    def receberCartasInicio(self, n, baralho): 
        ''' método para o jogador receber uma determinada quantidade de cartas de um baralho, tem como parâmetros a quantidade de cartas a serem recebidas "n" e como segundo parâmetro o baralho da onde será retirada as cartas, esse referente ao baralho inicial da classe Baralho.'''
        for i in range(n):
            cart = baralho.retirarCartas()
            self.__baralhoJ.empilha(cart)

    def numCartas(self): 
        ''' retorna o número de cartas na pilha do Jogador'''
        return self.__baralhoJ.tamanho()

    def mostrarElemento(self, posicao): 
        '''retorna uma determinada carta na pilha do jogador'''
        return self.__baralhoJ.elemento(posicao) 

    def temCarta(self): 
        '''retorna True se a pilha do jogador não estiver vazia'''
        return not self.__baralhoJ.estaVazia()

    def addFinal(self, pilha): 
        ''' método para adicionar carta ao final da lista, recebe como parâmetro a pilha a ser retirada todas as cartas'''
        for i in range(pilha.tamanho()):
            cart = pilha.desempilha()
            self.__baralhoJ.empilhaFinal(cart)

    def __str__(self):
        return f'O Jogador {self.__nome} tem {Jogador.numCartas(self)} cartas no seu baralho'

