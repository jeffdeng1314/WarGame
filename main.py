from classes import War


def main():
    war = War()

    player1, player2 = war.getDecks()

    while war.turn(player1, player2):
        continue


if __name__ == '__main__':
    main()
