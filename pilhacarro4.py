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
        
    def busca(self, placa):
        assert self.topo, "Impossível buscar valor em pilha vazia"  # Verifica se a pilha não está vazia
        atual = self.topo
        carros_para_retirar = []
        while atual:
            if atual.dado == placa:
                print(f"Carro com placa {placa} está estacionado.")
                print(f"Carros a serem retirados para que o carro com placa {placa} possa sair: {carros_para_retirar}")
                return
            carros_para_retirar.append(atual.dado)
            atual = atual.anterior
        print(f"Carro com placa {placa} não está estacionado.")
           
pilha = Pilha()
print("Pilha vazia:", pilha)  # Imprime a pilha vazia

for i in range(5): 
    num = input("Digite a placa do carro: ")  # Solicita a entrada do usuário
    pilha.inserir(num)  # Insere o valor na pilha
    print("Insere o valor ({0}) no topo da pilha: {1}".format(num, pilha))  # Imprime o estado atual da pilha

placa_para_buscar = input("Digite a placa do carro que deseja verificar: ")
pilha.busca(placa_para_buscar)  # Realiza a busca na pilha
