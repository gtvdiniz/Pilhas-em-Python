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

    # Encontrar o maior elemento
    def encontrar_maior(self):
        if self.topo is None:
            return None 
        
        maior = self.topo.dado  
        atual = self.topo.anterior
        
        while atual is not None:
            if atual.dado > maior:
                maior = atual.dado
            atual = atual.anterior
        
        return maior

pilha = Pilha()
print("Pilha vazia:", pilha)   

for i in range(5):
    num = int(input("Digite um número: "))
    pilha.inserir(num)
    print("Insere o valor ({0}) no topo da pilha: {1}".format(num, pilha))

maior_valor = pilha.encontrar_maior()
print("O maior valor na pilha é:", maior_valor)
