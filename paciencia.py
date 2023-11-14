import random

# Representa um baralho padrão de 52 cartas
class Deck:
    suits = ['Coração', 'Ouro', 'Paus', 'Espada']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    
    def __init__(self):
        self.cards = [(value, suit) for suit in self.suits for value in self.values]

    def shuffle(self):
        random.shuffle(self.cards)

# Inicia o jogo de paciência
def start_solitaire():
    # Cria e embaralha o baralho
    deck = Deck()
    deck.shuffle()

    # Cria as pilhas iniciais para o jogo de paciência
    solitaire_piles = [[] for _ in range(8)]

    # Distribui as cartas nas 7 primeiras pilhas
    for i in range(7):
        solitaire_piles[i].append(deck.cards.pop())

    # Coloca o restante das cartas na oitava pilha
    solitaire_piles[7].extend(deck.cards)

    # Exibe a configuração inicial da mesa
    for i, pile in enumerate(solitaire_piles):
        if pile:
            print(f"Pilha {i+1}: {pile[-1]}")
        else:
            print(f"Pilha {i+1}: Vazia")

# Chama a função para iniciar o jogo
start_solitaire()
