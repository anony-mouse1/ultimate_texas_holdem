from itertools import combinations

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
# shuffle(deck)
# print(deck)
# f string works with different data types (i.e. str & int)

table = ['3S', '2C', '10D', '6S', '9D']
player_cards = ['5C', '5D']
dealer_cards = ['3C', '4S']
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
        trips = (input("Optional. Trips?. Type y or n: "))
    while trips in ['y', 'Y']:
        trips = (input("Trips value: "))

        while not int(trips) % 5 == 0:
            trips = input('Trips value: ')

    ante = int(ante)
    blinds = int(blinds)
    trips = int(trips)


##deal cards


start()

'''
def check_hand():
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
