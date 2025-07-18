class Nodo: 
    """Esta classe representa um nodo de uma estrutura encadeada"""
    def __init__(self, dado=0, nodo_anterior=None):
        self.dado = dado  # Inicializa o atributo 'dado' com o valor fornecido ou 0 por padrão
        self.anterior = nodo_anterior  # Inicializa o atributo 'anterior' com o nodo anterior ou None por padrão
       
    def __repr__(self):
        return '%s -> %s' % (self.dado, self.anterior)  # Representação em string do nodo, mostrando o dado e o nodo anterior

class Pilha: 
    """Esta classe representa uma pilha encadeada"""
    
    def __init__(self):
        self.topo = None  # Inicializa o topo da pilha como None, indicando que a pilha está vazia
        
    def __repr__(self):
        return "[" + str(self.topo) + "]"  # Representação em string da pilha, mostrando o nodo no topo
        
    # Inserindo elemento 
    def inserir(self, novo_dado):
        novo_nodo = Nodo(novo_dado)  # Cria um novo nodo com o dado fornecido
        novo_nodo.anterior = self.topo  # Define o nodo anterior do novo nodo como o atual topo da pilha
        self.topo = novo_nodo  # Atualiza o topo da pilha para o novo nodo
        
    def remove(self): 
        assert self.topo, "Impossível remover o valor de pilha vazia"  # Verifica se a pilha não está vazia
        self.topo = self.topo.anterior  # Atualiza o topo da pilha para o nodo anterior

    def __eq__(self, outra):
        atual1 = self.topo  # Começa a comparação a partir do topo da pilha atual
        atual2 = outra.topo  # Começa a comparação a partir do topo da outra pilha
        while atual1 is not None and atual2 is not None:
            if atual1.dado != atual2.dado:
                return False  # Retorna False se os dados dos nodos não forem iguais
            atual1 = atual1.anterior  # Move para o próximo nodo na pilha atual
            atual2 = atual2.anterior  # Move para o próximo nodo na outra pilha
        return atual1 is None and atual2 is None  # Retorna True se ambas as pilhas tiverem o mesmo comprimento e dados

class Pilha2: 
    """Esta classe representa uma outra pilha encadeada"""
    
    def __init__(self):
        self.topo = None  # Inicializa o topo da pilha como None, indicando que a pilha está vazia
        
    def __repr__(self):
        return "[" + str(self.topo) + "]"  # Representação em string da pilha, mostrando o nodo no topo
        
    # Inserindo elemento 
    def inserir(self, novo_dado):
        novo_nodo = Nodo(novo_dado)  # Cria um novo nodo com o dado fornecido
        novo_nodo.anterior = self.topo  # Define o nodo anterior do novo nodo como o atual topo da pilha
        self.topo = novo_nodo  # Atualiza o topo da pilha para o novo nodo
        
    def remove(self): 
        assert self.topo, "Impossível remover o valor de pilha vazia"  # Verifica se a pilha não está vazia
        self.topo = self.topo.anterior  # Atualiza o topo da pilha para o nodo anterior

    def __eq__(self, outra):
        atual1 = self.topo  # Começa a comparação a partir do topo da pilha atual
        atual2 = outra.topo  # Começa a comparação a partir do topo da outra pilha
        while atual1 is not None and atual2 is not None:
            if atual1.dado != atual2.dado:
                return False  # Retorna False se os dados dos nodos não forem iguais
            atual1 = atual1.anterior  # Move para o próximo nodo na pilha atual
            atual2 = atual2.anterior  # Move para o próximo nodo na outra pilha
        return atual1 is None and atual2 is None  # Retorna True se ambas as pilhas tiverem o mesmo comprimento e dados

# Testando a comparação
pilha1 = Pilha()  # Cria uma nova instância da pilha
print("Pilha vazia:", pilha1)  # Imprime a pilha vazia
for i in range(5): 
    num = int(input("Digite um número: "))  # Solicita ao usuário que digite um número
    pilha1.inserir(num)  # Insere o número na pilha
    print("Insere o valor ({0}) no topo da pilha: {1}".format(num, pilha1))  # Imprime o estado atual da pilha
    print(pilha1)  # Imprime a pilha após a inserção
    
pilha2 = Pilha2()  # Cria uma nova instância da segunda pilha
print("\n\nPilha vazia:", pilha2)  # Imprime a segunda pilha vazia
for i in range(5): 
    num = int(input("Digite um número: "))  # Solicita ao usuário que digite um número
    pilha2.inserir(num)  # Insere o número na segunda pilha
    print("Insere o valor ({0}) no topo da pilha: {1}".format(num, pilha2))  # Imprime o estado atual da segunda pilha
    print(pilha2)  # Imprime a segunda pilha após a inserção
    
def compara():
    if pilha1 == pilha2:
       print(f"\nA pilha 1: {pilha1} é igual a pilha 2: {pilha2}")  # Imprime se as pilhas são iguais
    else: 
        print(f"\nA pilha 1: {pilha1} é diferente da pilha 2: {pilha2}")  # Imprime se as pilhas são diferentes
compara()  # Compara as duas pilhas e imprime o resultado
