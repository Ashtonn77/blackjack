def take_bet(chips):

    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet?__"))
        except:
            print("I'm sorry that's an invalid bet...integers only")
        else:
            if chips.bet > chips.total:
                print("Sorry, you seem to be a little short on chips! You have {} chips available".format(
                    chips.total))
            else:
                print("Bet recieved")
                break


def hit(deck, hand):

    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing  # to control an upcoming while loop

    while True:

        x = input("Hit or Stand? Enter h or s__")

        if x[0].lower() == 'h':
            hit(deck, hand)

        elif x[0] == 's':
            print("player stands...Dealers turn")
            playing = False

        else:
            print("Sorry, I didn't understand your input. Enter h or s only")
            continue

        break


'''
def show_some(player, dealer):

    pass


def show_all(player, dealer):

    pass
'''


def player_busts(player, dealer, chips):
    print("PLAYER BUST")
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print("PLAYER WINS")
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print("DEALER BUST...PLAYER WINS")
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print("DEALER WINS")
    chips.lose_bet()


def push(player, dealer):
    print("Dealer and Player Tie! PUSH")
