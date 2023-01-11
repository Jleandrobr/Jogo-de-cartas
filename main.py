# Grupo: Ricardo Pereira Lins, Geraldo da Silva Neto e José Leandro Fernandes de Medeiros Brasileiro

from Baralho import Baralho
from Jogador import Jogador
from PilhaEncadeada import Pilha


class Jogo:
    def __init__(self, nomeJogador1, nomeJogador2, rodadasTotal):
        '''Inicia o Jogo com uma pilha de Descarte para auxiliar nas rodadas, o baralho inicial e já o embaralha, os dois jogadores e como parâmetros os seus nomes e como terceiro parâmetro o número total de rodadas e inicia uma variável que mostrará qual a rodada atual'''
        self.__pilhaDescarte = Pilha()
        self.__baralhoInicial = Baralho()
        self.__baralhoInicial.embaralharar()
        self.__jogador1 = Jogador(nomeJogador1)
        self.__jogador2 = Jogador(nomeJogador2)
        self.__rodadasTotal = rodadasTotal
        self.__rodadaAtual = 1

    def inicio(self):
        '''Define a quantidade de cartas que cada jogador vai receber no inicio'''
        self.__jogador1.receberCartasInicio(26, self.__baralhoInicial)
        self.__jogador2.receberCartasInicio(26, self.__baralhoInicial)

    def compararCartas(self):
        '''Método para comparar qual valor da carta atual é maior, se é a carta do jogador 1 ou do jogador 2 e print na tela o funcionamento do jogo'''
        while self.__rodadaAtual <= self.__rodadasTotal:
            print(f'\nRodada {self.__rodadaAtual} de {self.__rodadasTotal}\n')
            input('Tecle enter para mostrar a rodada:')

            # caso o jogador 1 ganhe
            if self.__jogador1.mostrarElemento(1).mostrarValor() > self.__jogador2.mostrarElemento(1).mostrarValor():
                print(f'\nO Jogador {self.__jogador1.getNome()} ganhou essa rodada!\n')
                print(
                    f'Carta do {self.__jogador1.getNome()} é {self.__jogador1.mostrarElemento(1)} X Carta do {self.__jogador2.getNome()} é {self.__jogador2.mostrarElemento(1)}\n')
                self.__jogador1.retirarCarta(self.__pilhaDescarte)
                self.__jogador2.retirarCarta(self.__pilhaDescarte)
                print('As cartas abaixo serão adicionadas no fim do baralho do vencedor:')
                self.__pilhaDescarte.imprime()
                self.__jogador1.addFinal(self.__pilhaDescarte)
                self.__rodadaAtual += 1
                print(f'{self.__jogador1.getNome()} tem {self.__jogador1.numCartas()} cartas em seu baralho')
                print(f'{self.__jogador2.getNome()} tem {self.__jogador2.numCartas()} cartas em seu baralho')

            # caso o jogador 2 ganhe:
            elif self.__jogador2.mostrarElemento(1).mostrarValor() > self.__jogador1.mostrarElemento(1).mostrarValor():
                print(f'\nO Jogador {self.__jogador2.getNome()} ganhou essa rodada!\n')
                print(
                    f'Carta do {self.__jogador1.getNome()} é {self.__jogador1.mostrarElemento(1)} X Carta do {self.__jogador2.getNome()} é {self.__jogador2.mostrarElemento(1)}\n')
                self.__jogador1.retirarCarta(self.__pilhaDescarte)
                self.__jogador2.retirarCarta(self.__pilhaDescarte)
                print('As cartas abaixo serão adicionadas no fim do baralho do vencedor:')
                self.__pilhaDescarte.imprime()
                self.__jogador2.addFinal(self.__pilhaDescarte)
                self.__rodadaAtual += 1
                print(f'{self.__jogador1.getNome()} tem {self.__jogador1.numCartas()} cartas em seu baralho')
                print(f'{self.__jogador2.getNome()} tem {self.__jogador2.numCartas()} cartas em seu baralho')

            # caso de empate:
            elif self.__jogador1.mostrarElemento(1).mostrarValor() == self.__jogador2.mostrarElemento(1).mostrarValor():
                print('\nDeu empate nessa rodada!\n')
                print(
                    f'Carta do {self.__jogador1.getNome()} é {self.__jogador1.mostrarElemento(1)} X Carta do {self.__jogador2.getNome()} é {self.__jogador2.mostrarElemento(1)}\n')
                self.__jogador1.retirarCarta(self.__pilhaDescarte)
                self.__jogador2.retirarCarta(self.__pilhaDescarte)
                print('As cartas abaixo serão adicionadas no fim do baralho do da próxima rodada:')
                self.__pilhaDescarte.imprime()
                self.__rodadaAtual += 1
                print(f'{self.__jogador1.getNome()} tem {self.__jogador1.numCartas()} cartas em seu baralho')
                print(f'{self.__jogador2.getNome()} tem {self.__jogador2.numCartas()} cartas em seu baralho')

    def ganhador(self):
        '''Método para ser chamado no final da aplicação e printar na tela o jogador que ganhou ou se o jogo terminou empatado'''
        if self.__jogador1.numCartas() > self.__jogador2.numCartas():
            print(f'\n{self.__jogador1} é o ganhador\n')
        elif self.__jogador2.numCartas() > self.__jogador1.numCartas():
            print(f'\n{self.__jogador2} é o ganhador\n')
        else:
            print('\nO jogo terminou empatado!\n')

    def resetar(self):
        '''Método para resetar o jogo, devolvendo todas as cartas dos baralhos dos jogadores ao baralho Inicial'''
        self.__jogador1.devolverCartas(self.__jogador1.numCartas(), self.__baralhoInicial)
        self.__jogador2.devolverCartas(self.__jogador2.numCartas(), self.__baralhoInicial)


# Programa principal início:
if __name__ == "__main__":
    rePlay = 'Y'
    while (rePlay == 'y' or rePlay == 'Y'):
        while True:
            # tratamento de erro, caso digite uma string no lugar de um inteiro no numRodadastotal
            try:
                n = int(input('Digite a quantidade de rodadas necessárias para o término do jogo: '))
                break
            except ValueError:
                print('\nDigite um número inteiro!\n')

        nome1 = input('Digite o nome do Jogador 1: ')
        # tratamento de erro para caso o input do nome ser vazio ou com um espaço
        while nome1 == '' or nome1 == ' ':
            print('\nDigite um nome válido\n')
            nome1 = input('Digite o nome do Jogador 1: ')
        nome2 = input('Digite o nome do Jogador 2: ')
        # tratamento de erro para caso o input do nome ser vazio ou com um espaço
        while nome2 == '' or nome2 == ' ':
            print('\nDigite um nome válido\n')
            nome2 = input('Digite o nome do Jogador 2: ')
        j = Jogo(nome1, nome2, n)
        j.inicio()
        j.compararCartas()
        j.ganhador()
        j.resetar()
        rePlay = input('Digite "Y" se quiser jogar novamente ou qualquer valor para encerrar o jogo:')

    print("\nAgradecemos por ter jogado o jogo Batalha!")




