from itertools import combinations
from random import shuffle
#card branch
cardfaces = []
suits = ['H', 'S', 'C', 'D']
royals = ['J', 'Q', 'K', 'A']
deck = []

for i in range(2, 11):
    cardfaces.append(str(i))

for j in range(4):
    cardfaces.append(royals[j])
for k in range(4):
    for l in range(13):
        card = f"{cardfaces[l]}{suits[k]}"
        deck.append(card)
#shuffle(deck)
dealer_cards = []
player_cards = []
table = []
for i in range(2):
    dealer_cards.append(deck[i])
    deck.pop(i)
    player_cards.append(deck[i])
    deck.pop(i)

for i in range(5):
    table.append(deck[i])
    deck.pop(i)

# f string works with different data types (i.e. str & int)

player_hands = [*player_cards, *table]
# or you can do player_cards + table
# this still returns a list
dealer_hands = [*dealer_cards, *table]

ante = 0
blinds = 0
trips = 0
player_chips = 500
dealer_chips = 500


# convert them to integers in the end
def start():
    global player_chips, ante, blinds, trips
    while True:
        try:
            ante = int(input("Ante value: "))
            if int(ante) <= player_chips and int(ante) % 5 == 0:
                break
            #else:
             #   print("Please select a valid number")
        except:
            #print("Not a valid input")
            continue
#also have to make sure that after the bet, the user has at least 1x of their bet
#check that user has at least 1x of their bet before running the game
# if not, send msg saying u don't have enough chips. restart game to play again.
    while trips not in ['y', 'n', 'Y', 'N']:
        trips = ''
        trips = (input("Optional. Trips?. (y/n): "))

    while trips in ['y', 'Y']:
        while True:
            try:
                    trips = int(input("Trips value: "))
                    if int(trips) <= player_chips and int(trips) % 5 == 0:
                        break
                    else:
                        continue

                #this is for "no"
            except:
                print("Not a valid input")
                print(trips)
                continue

    print(player_cards)


##deal cards


start()

print(ante)
#prints 10

'''
def check_ hand():
    ##card types


def royal_flush(hand):
    pass


def straight_flush(hand):
    if flush(hand) and straight(hand):
        return True


def four_of_a_kind(hand):
    pass


def full_house(hand):
    pass


def flush(hand):
    pass


def straight(hand):
    pass


def three_of_a_kind(hand):
    pass


def two_pair(hand):
    pass


def pair(hand):
    pass


def high_card(hand):
    pass


best_hand = 0


def dealer():
    for hand in list(map(list, combinations(dealer_hands, 5))):
        pass


def player():
    for hand in list(map(list, combinations(player_hands, 5))):
        pass
'''
