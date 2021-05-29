import random
from classes import War


def main():
    war = War()

    player1, player2 = war.getDecks()

    while war.turn(player1, player2):

        if random.randint(1, 50) == 20:
            print(f"\n{' ': <15}SHUFFLE TIME\n")
            war.shuffle(player1)
            war.shuffle(player2)


if __name__ == '__main__':
    main()
