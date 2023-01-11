class PilhaException(Exception):
    def __init__(self, mensagem, metodo=''):
        super().__init__(mensagem)
        self.metodo = metodo


class Node: 
    '''classe de nó entre dados de um pilha'''
    def __init__(self, dado):
        self.dado = dado
        self.prox = None

    def insereProximo(self, dado): 
        '''inserir próximo dado na pilha'''
        if (self.prox == None):
            self.prox = Node(dado)

    def getProximo(self): 
        '''retornar o próximo dado da pilha, se houver'''
        return self.prox

    def __str__(self):
        return str(self.data)

    def temProximo(self): 
        '''analizar se tem um próximo dado na pilha'''
        return self.prox != None


class Pilha: 
    '''classe de pilha'''
    def __init__(self):
        self.__head = None
        self.__tamanho = 0

    def estaVazia(self): 
        '''confirmar se a pilha está vazia'''
        return self.__head == None

    def tamanho(self): 
        '''retornar o tamanho da pilha'''
        return self.__tamanho

    def elemento(self, posicao): 
        '''retorna um elemento da posição de dado na pilha, se houver'''
        try:
            assert posicao > 0 and posicao <= self.__tamanho

            cursor = self.__head
            contador = 1
            while (cursor != None and contador < posicao):
                contador += 1
                cursor = cursor.prox

            return cursor.dado
        except TypeError:
            raise PilhaException('Digite um número inteiro referente ao elemento desejado')
        except AssertionError:
            raise PilhaException(f'O elemento {posicao} NAO existe na pilha de tamanho {self.__tamanho}')
        except:
            raise

    def busca(self, valor): 
        '''função de buscar'''
        cursor = self.__head
        contador = 1

        while (cursor != None):
            if cursor.dado == valor:
                return contador
            cursor = cursor.prox
            contador += 1

        raise PilhaException(f'Valor {valor} nao esta na pilha', 'busca()')

    def empilha(self, valor): 
        '''função de empilhar'''
        novo = Node(valor)
        novo.prox = self.__head
        self.__head = novo
        self.__tamanho += 1

    def desempilha(self): 
        '''função de desempilhar'''
        if not self.estaVazia():
            dado = self.__head.dado
            self.__head = self.__head.prox
            self.__tamanho -= 1
            return dado
        raise PilhaException('A pilha está vazia')

    def imprime(self): 
        print(self.__str__())

    #a função abaixo foi adicionada para empilhar no final da pilha "Base"  
    def empilhaFinal(self, valor): 
        ''' pecorre a pilha pelo seu tamanho até encontrar o último no e adiciona um novo no no lugar do próximo do nó final anterior'''
        no = Node(valor)
        cursor = self.__head
        contador = 1
        while contador < self.tamanho():
            contador += 1
            cursor = cursor.prox
        self.__tamanho += 1
        cursor.prox = no

    def InsereNoFundo(self, valor):
        cursor = self.__head
        while cursor.prox != None:  
            pass

            
    def __str__(self):
        cursor = self.__head
        primeiro = True
        s = 'topo->['
        while (cursor != None):
            if primeiro:
                s += f'{cursor.dado}'
                primeiro = False
            else:
                s += f', {cursor.dado}'
            cursor = cursor.prox

        s += ']'
        return s
