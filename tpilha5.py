class Nodo: 
    """Esta classe representa um nodo de uma estrutura encadeada"""
    def __init__(self, dado=0, nodo_anterior=None):
        self.dado = dado  # Inicializa o dado do nodo
        self.anterior = nodo_anterior  # Inicializa o nodo anterior
       
    def __repr__(self):
        return '%s -> %s' % (self.dado, self.anterior)  # Representação do nodo para impressão
    
class Pilha: 
    """Esta classe representa uma pilha encadeada"""
    
    def __init__(self):
        self.topo = None  # Inicializa o topo da pilha como None
        
    def __repr__(self):
        return "[" + str(self.topo) + "]"  # Representação da pilha para impressão
        
    # Inserindo elemento 
    def inserir(self, novo_dado):
        novo_nodo = Nodo(novo_dado)  # Cria um novo nodo com o dado fornecido
        novo_nodo.anterior = self.topo  # Define o nodo anterior como o topo atual
        self.topo = novo_nodo  # Atualiza o topo para o novo nodo
        
    def remove(self): 
        assert self.topo, "Impossível remover o valor de pilha vazia"  # Verifica se a pilha não está vazia
        self.topo = self.topo.anterior  # Remove o topo atual, atualizando para o nodo anterior
        
    def esvaziar(self):
        while self.topo:
            print(f"Removendo {self.topo.dado} da pilha")
            self.remove()

def TPilha(vetor):
    pilha = Pilha()
    for numero in vetor:
        if numero % 2 == 0:
            pilha.inserir(numero)
            print(f"Inserindo {numero} na pilha: {pilha}")
        else:
            if pilha.topo:
                print(f"Número ímpar {numero} encontrado, removendo {pilha.topo.dado} da pilha")
                pilha.remove()
            else:
                print(f"Número ímpar {numero} encontrado, mas a pilha está vazia")
    
    print("\nEsvaziando a pilha:")
    pilha.esvaziar()

# Exemplo de uso
vetor = [i for i in range(1, 16)]  # Vetor de exemplo com 15 elementos
TPilha(vetor)
