import random


# The suits unicode can be found in https://www.compart.com/en/unicode/
SUITS = ['\u2663', '\u2666', '\u2665', '\u2660']
FACES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
DECK = [f'[{s}{f}]' for f in FACES for s in SUITS]
RANK = dict((DECK[i], i//4) for i in range(len(DECK)))


# War class
class War():

    # split the deck into two
    def __init__(self):
        deck = DECK.copy()
        random.shuffle(deck)
        self._deck1 = deck[:26]
        self._deck2 = deck[26:]

    # returns two decks to both players, respectively
    def getDecks(self):
        return self._deck1, self._deck2

    def turn(self, p1, p2):
