# WarGame

War card game program
This is a game of **probability**

Ref: https://en.wikipedia.org/wiki/War_(card_game)

There is a lot of variation to the game, but in this program, we will stick with the following rules:

1. Two players with 26 cards for each person.
2. The goal is to be the first player to win all 52 cards.
3. At each round, both players will put down one card facing up. The player with the higher card takes both of the cards and moves them to their stack.
4. If two cards are played with equal value, hence 'war', both players place the next three cards face down and then another card face-up (Which goes back to step 3).
   And if both cards have equual value again, repeat with another set of face-up/down cards, and so on.
5. Card rank (highest first) A K Q J 10 9 8 7 6 5 4 3 2. The suits are ignored.

_Instructions_
I have some unicode characters like heart and spade implemented in this program, so please run this program in a supported console (like the terminal console in VS Code).
Please refer to: https://wiki.python.org/moin/PrintFails
This program is written in Python3, please enter the following command to run this program:
python3 main.py


**Assumptions**
1. Two players are equally distributed with randomly shuffled decks (26 cards per deck).
2. Since suits are ignored, we only care about the cards by their values.
3. Both players are being played by the program; human interactions/interference are invalid.
4. Both decks will be shuffled by random chance during gameplay.


**Format**
1. The status of the game will be printed at each round and the layout would be:
   _(# of cards remaining)player 1: [card being played] | (# of cards remaining)Player2: [card being played] <round status>_


**Corner Cases**
1. Since the game is being played by the computer, there's no human interactions involved. However, while I was developing this program, I realized that there will be times where the program would run into an infinite loop (cards on stack are appended at the end of the deck, and there's a possiblity where the same cards are appended in the same position repeatedly). In order to remove this corner case, I have to shuffle the decks once in a while. I implemented a feature where both decks will get shuffled in a random chance (1/50) at each round.


**If Given More Time**
1. If I was given more time to work on this program, I would:
   a. Have a better object oriented design for this program like classes for card and deck.
   b. Implement human interaction features like a user can shuffle one's deck whenever.
   c. Possibly implement more variations of this game like putting down n card/s facing down instead of 3. The n can be determined by the user.
   d. Implement a score board for both players, so we can keep track of the amount of wins/losses/total games 
