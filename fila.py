class Fila:
    # Cria uma fila vazia
    def __init__(self):
        self._items = list()

    # Se a fila estiver vazia retorna True, senão retorna False
    def estaVazia(self):
        return len(self) == 0

    # Retorna quantos elementos tem na fila
    def __len__(self):
        return len(self._items)

    # Insere um elemento na fila
    def enfileira(self, item):
        self._items.append(item)

    # Remove e retorna o primeiro elemento da fila
    def desinfileira(self):
        assert not self.estaVazia(), "Fila vazia!"
        return self._items.pop(0)

