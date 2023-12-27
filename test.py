import random

SUITE = ['H', 'D', 'S', 'C']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']


class Hand:
    def __init__(self):
        self.card_deck = self.create_deck()
        self.shuffle_deck()

    def create_deck(self):
        deck = []
        card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                       '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        for suite in range(len(SUITE)):
            for rank in range(len(RANKS)):
                value = card_values[RANKS[rank]]
                card = {'suite': SUITE[suite],
                        'rank': RANKS[rank], 'value': value}
                deck.append(card)
        return deck

    def shuffle_deck(self):
        random.shuffle(self.card_deck)

    def deal_cards(self):
        half = len(self.card_deck) // 2
        player_hand = self.card_deck[:half]
        computer_hand = self.card_deck[half:]
        return player_hand, computer_hand


hand = Hand()

player_hand, computer_hand = hand.deal_cards()


def print_hand(hand):
    for card in hand:
        print(f'{card["rank"]} of {card["suite"]}')


def print_c_hand(hand):
    for card in hand:
        print(f'{card["rank"]} of {card["suite"]}')


print("Ręka gracza:")
print_hand(player_hand)
print("Ręka Komputera:")
print_c_hand(computer_hand)


class Game():
    def __init__(self, player_hand, computer_hand):
        self.player_hand = player_hand
        self.computer_hand = computer_hand
        self.table_cards = []

    def play(self):
        if not self.player_hand or not self.computer_hand:
            return ("Nie można już grać któraś z rąk jest pusta")

        player_card = self.player_hand.pop(0)
        computer_card = self.computer_hand.pop(0)
        self.table_cards.extend([player_card, computer_card])

        print(f'{player_card} vs {computer_card}')

        if player_card['value'] > computer_card['value']:
            self.player_hand.append(player_card)
            self.player_hand.append(computer_card)
            print("Wygrałeś")

        elif player_card['value'] < computer_card['value']:
            self.computer_hand.append(player_card)
            self.computer_hand.append(computer_card)
            print("Wygrał Komputer")
        else:
            print("Wojna!")
            if len(self.player_hand) < 2 or len(self.computer_hand) < 2:
                return ("Nie można kontynuować wojny, któraś z rąk jest za krótka")
            self.table_cards.extend(
                [self.player_hand.pop(0), self.computer_hand.pop(0)])
            return self.play()
