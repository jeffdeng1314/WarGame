from classes import War


def main():
    war = War()

    player1, player2 = war.getDecks()

    print(player1)


if __name__ == '__main__':
    main()
