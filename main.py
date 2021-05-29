import random
from classes import War


def main():
    war = War()

    player1, player2 = war.getDecks()

    counter = 0
    while war.turn(player1, player2):
        counter += 1

        if counter == 30:
            print(f"\n{' ': <15}SHUFFLE TIME\n")
            war.shuffle(player1)
            war.shuffle(player2)
            counter = 0


if __name__ == '__main__':
    main()
