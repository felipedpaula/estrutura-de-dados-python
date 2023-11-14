class No:
    def __init__(self, chave):
        self.esquerda = None
        self.direita = None
        self.valor = chave

def imprimirOrdemPorNivel(raiz):
    if raiz is None:
        return
    
    fila = []
    
    fila.append(raiz)

    while(len(fila) > 0):
        print(fila[0].valor)
        no = fila.pop(0)
        
        if no.esquerda is not None:
            fila.append(no.esquerda)
        
        if no.direita is not None:
            fila.append(no.direita)

# Programa principal para testar a função acima
# Vamos criar a seguinte árvore binária como exemplo
#         1
#       /   \
#      2     3
#     / \   / \
#    4   5 6   7

raiz = No(1)
raiz.esquerda = No(2)
raiz.direita = No(3)
raiz.esquerda.esquerda = No(4)
raiz.esquerda.direita = No(5)
raiz.direita.esquerda = No(6)
raiz.direita.direita = No(7)

imprimirOrdemPorNivel(raiz)
