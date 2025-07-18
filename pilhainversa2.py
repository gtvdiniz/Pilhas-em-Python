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

    # Inverter a pilha
    def inverter(self):
        elementos = []
        atual = self.topo  # Começa a partir do topo da pilha
        while atual is not None:
            elementos.append(atual.dado)  # Adiciona o dado do nodo atual à lista de elementos
            atual = atual.anterior  # Move para o próximo nodo na pilha
        
        self.topo = None  # Esvazia a pilha original
        
        for dado in elementos:
            self.inserir(dado)  # Insere novamente os elementos na pilha, recriando-a na ordem inversa

pilha = Pilha()  # Cria uma nova instância da pilha
print("Pilha vazia:", pilha)  # Imprime a pilha vazia

for i in range(5):
    num = int(input("Digite um número: "))  # Solicita ao usuário que digite um número
    pilha.inserir(num)  # Insere o número na pilha
    print("Insere o valor ({0}) no topo da pilha: {1}".format(num, pilha))  # Imprime o estado atual da pilha

print("Pilha antes de inverter:")
print(pilha)  # Imprime a pilha antes de inverter

pilha.inverter()  # Inverte a pilha

print("Pilha invertida:")
print(pilha)  # Imprime a pilha invertida
