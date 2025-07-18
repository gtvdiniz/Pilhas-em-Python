class Nodo: 
    """Esta classe representa um nodo de uma estrutura encadeada"""
    def __init__(self, dado=0, nodo_anterior=None):
        self.dado = dado 
        self.anterior = nodo_anterior
       
    def __repr__(self):
        return '%s -> %s' % (self.dado, self.anterior)

class Pilha: 
    """Esta classe representa uma pilha encadeada"""
    
    def __init__(self):
        self.topo = None 
        
    def __repr__(self):
        return "[" + str(self.topo) + "]"
        
    # Inserindo elemento 
    def inserir(self, novo_dado):
        novo_nodo = Nodo(novo_dado)
        novo_nodo.anterior = self.topo 
        self.topo = novo_nodo
        
    def remove(self): 
        assert self.topo, "Impossível remover o valor de pilha vazia"
        
        self.topo = self.topo.anterior 

    def __eq__(self, outra):
        atual1 = self.topo
        atual2 = outra.topo
        while atual1 is not None and atual2 is not None:
            if atual1.dado != atual2.dado:
                return False
            atual1 = atual1.anterior
            atual2 = atual2.anterior
        return atual1 is None and atual2 is None

class Pilha2: 
    """Esta classe representa uma outra pilha encadeada"""
    
    def __init__(self):
        self.topo = None 
        
    def __repr__(self):
        return "[" + str(self.topo) + "]"
        
    # Inserindo elemento 
    def inserir(self, novo_dado):
        novo_nodo = Nodo(novo_dado)
        novo_nodo.anterior = self.topo 
        self.topo = novo_nodo
        
    def remove(self): 
        assert self.topo, "Impossível remover o valor de pilha vazia"
        
        self.topo = self.topo.anterior 

    def __eq__(self, outra):
        atual1 = self.topo
        atual2 = outra.topo
        while atual1 is not None and atual2 is not None:
            if atual1.dado != atual2.dado:
                return False
            atual1 = atual1.anterior
            atual2 = atual2.anterior
        return atual1 is None and atual2 is None

# Testando a comparação
pilha1 = Pilha()
print("Pilha vazia:", pilha1)   
for i in range(5): 
    num = int(input("Digite um número: "))
    pilha1.inserir(num)
    print("Insere o valor ({0}) no topo da pilha: {1}".format(num, pilha1))
    print(pilha1)
    
pilha2 = Pilha2()
print("\n\nPilha vazia:", pilha2)   
for i in range(5): 
    num = int(input("Digite um número: "))
    pilha2.inserir(num)
    print("Insere o valor ({0}) no topo da pilha: {1}".format(num, pilha2))
    print(pilha2)
    
def compara():
    if pilha1 == pilha2:
       print(f"\nA pilha 1: {pilha1} é igual a pilha 2: {pilha2}")
    else: 
        print(f"\nA pilha 1: {pilha1} é diferente da pilha 2: {pilha2}")
compara()


        

        


