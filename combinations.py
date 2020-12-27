
from itertools import combinations
cardfaces = []
suits= ['H', 'S', 'C', 'D']
royals= ['J', 'Q', 'K', 'A']
deck = []

for i in range(2, 11):
    cardfaces.append(str(i))

for j in range(4):
    cardfaces.append(royals[j])
for k in range (4):
    for l in range(13):
        card = f"{cardfaces[l]}{suits[k]}"
        deck.append(card)
#shuffle(deck)
print (deck)
#f string works with different data types (i.e. str & int)

table = ['3S', '2C', '10D', '6S', '9D']
player_cards = ['5C', '5D']
dealer_cards = ['3C', '4S']
player_hands = [*player_cards, *table]
# or you can do player_cards + table
# this still returns a list
dealer_hands = [*dealer_cards, *table]


##card types
def royal_flush():
    pass


def straight_flush():
    if flush() and straight():
        return True


def four_of_a_kind():
    pass


def full_house():
    pass


def flush():
    pass


def straight():
    pass


def three_of_a_kind():
    pass


def two_pair():
    pass


def pair():
    pass


def high_card():
    pass


best_hand = 0


def dealer():
    for hand in list(map(list, combinations(dealer_hands, 5))):
        pass

def player():
    for hand in list(map(list, combinations(player_hands, 5))):
        pass
