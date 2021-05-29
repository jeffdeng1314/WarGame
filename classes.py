import random


# The suits unicode can be found in https://www.compart.com/en/unicode/
SUITS = ['\u2663', '\u2666', '\u2665', '\u2660']
FACES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
DECK = [f'[{s}{f}]' for f in FACES for s in SUITS]
RANK = dict((DECK[i], i//4) for i in range(len(DECK)))


# class Card:
#     def __init__(self):
#         self.

# War class
class War:

    # split the deck into two
    def __init__(self):
        deck = DECK.copy()
        self.shuffle(deck)
        # private variables
        self.__deck1 = deck[:26]
        self.__deck2 = deck[26:]

        # holds the cards when played
        self.__stack = []

    # returns two decks to both players, respectively
    def getDecks(self):
        return self.__deck1, self.__deck2

    # randomly shuffles a deck
    def shuffle(self, deck):
        random.shuffle(deck)

    # for each turn
    def turn(self, deckP1, deckP2):
        if len(deckP1) == 0 or len(deckP2) == 0:
            return self.gg(deckP1, deckP2)

        cardP1, cardP2 = deckP1.pop(0), deckP2.pop(0)
        rankP1, rankP2 = RANK[cardP1], RANK[cardP2]

        self.__stack.append(cardP1)
        self.__stack.append(cardP2)

        if rankP1 > rankP2:
            print(self.play(len(deckP1), len(deckP2),
                  cardP1, cardP2) + self.status(player=1))
            deckP1 += self.__stack
            self.__stack = []

        elif rankP1 < rankP2:
            print(self.play(len(deckP1), len(deckP2),
                  cardP1, cardP2) + self.status(player=2))
            deckP2 += self.__stack
            self.__stack = []

        else:
            print(self.play(len(deckP1), len(deckP2),
                  cardP1, cardP2) + self.status(war=True))
            if not self.warTime(deckP1, deckP2):
                return self.gg(deckP1, deckP2)

        return True

    # prints out the status when the game is over
    def gg(self, deckP1, deckP2):
        if len(deckP1) == 0:
            if len(deckP2) == 0:
                print("The game is a tie! GG y'all")

            else:
                print("Player 2 wins! GG bois")
        else:
            print("Player 1 wins! GG bois")

        print(
            f"Deck remaining for player 1: {len(deckP1)} | player 2: {len(deckP2)} | on the stack: {self.__stack}")
        return False

    # both cards with equal values, war time!
    def warTime(self, deckP1, deckP2):

        # each player puts down 3 cards, facing down. \u2327: https://www.compart.com/en/unicode/U+2327
        for _ in range(3):
            if len(deckP1) == 0 or len(deckP2) == 0:
                return False

            self.__stack.append(deckP1.pop(0))
            self.__stack.append(deckP2.pop(0))
            print(self.play(len(deckP1), len(deckP2), '\u2327', '\u2327') +
                  f"Both players put down a card facing down")
        return True

    # use to print out the cards that are played in console

    def play(self, deck1Len, deck2Len, cardP1, cardP2):
        return(
            f"({deck1Len})Player 1: {cardP1: <8}|{' ': <3}({deck2Len})Player 2: {cardP2:<8}")

    # use to print out the status of the current round in the console
    def status(self, player=0, war=False):
        if war:
            return(f"Tie! It's war time!!")

        return (f"Player {player} takes all the cards.")
