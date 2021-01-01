from itertools import combinations
from random import shuffle

# card branch
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
shuffle(deck)
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

player_hands = [*player_cards, *table]
dealer_hands = [*dealer_cards, *table]

trips = 0
player_chips = 50
ante = 0
trips = 0
player_chips = 500
dealer_chips = float('inf')


# technically speaking, there is no real 'dealer chips'... it will always be technically..infinity


def pre():
    global player_chips, ante, trips
    print("Ultimate Texas Holdem")
    print("Your chips:", player_chips)
    while True:
        try:
            ante = int(input("Ante value: "))
            if int(ante) <= player_chips and int(ante) % 5 == 0 and int(ante) * 3 <= player_chips and int(ante) != 0:
                print("Blind value:", ante)
                return ante
                #break
        except:
            print("Not a valid input")
            continue

    # chips
    player_chips -= ante * 2
    print("Your chips:", player_chips)
    trips = ''
    while trips.lower() not in ['y', 'n']:
        trips = (input("Optional. Trips?. (y/n): "))

    # before betting trips, make sure that they have at least 1x of their ante left in player_chips
    while trips in ['y', 'Y']:
        while True:
            try:
                trips = int(input("Trips value: "))
                if int(trips) <= player_chips and int(trips) % 5 == 0 and int(trips) != 0 and (
                        player_chips - trips >= ante):
                    player_chips -= trips
                    return trips, player_chips
                    # break
                    # or i could use return...nah
                else:
                    continue

            # this is for "no"
            except:
                print("Not a valid input")
                continue
    print("Your chips:", player_chips)


# print(player_chips)
# prints same both times (reference line 83)


# global ante still works

def start():
    if player_chips >= 15:
        pre()
    else:
        print("You don't have sufficient chips to play. Please refresh the game to earn your chips.")


start()
print("Your cards are:", player_cards[0], 'and', player_cards[1])

player_decision = ''
while player_decision.lower() not in ['check', '4x', '3x']:
    player_decision = (input("Check or 4x or 3x?: "))

while player_chips >= 3 * ante:
    try:
        if player_decision == '3x':
            print("Player bet 3x")

        # if player_chips >= ante * 3:
        # elif player_decision == '4x':
        else:
            #this else would be for 4x
            # if player_chips >= ante * 4:
            for i in range(5):
                table.append(deck[i])
                deck.pop(i)
    except:
        continue
else:
    player_decision= player_decision.lower()
    if player_decision=='check':
        print("Player checked")
    else:
        print("Insufficient chips")


# print(player_chips)

def single_round(argument, n):
    if player_chips >= ante * argument:
        for c in range(n):
            table.append(deck[i])
            deck.pop(i)
    else:
        print("Insufficient chips")


def after_bet(argument):
    global table, deck
    table.append(deck[i])

print(ante)
print(trips)

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
