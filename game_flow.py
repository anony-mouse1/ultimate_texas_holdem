from itertools import combinations
from random import shuffle
trips = 0
player_chips = 500
ante = 0
play = 0

cardfaces = []
suit = ['H', 'S', 'C', 'D']
royals = ['J', 'Q', 'K', 'A']
deck = []

for i in range(2, 11):
    cardfaces.append(str(i))
for j in range(4):
    cardfaces.append(royals[j])
for k in range(4):
    for l in range(13):
        card = f"{cardfaces[l]}{suit[k]}"
        deck.append(card)



def pre(player_chips, player_cards):
    print()
    print("Ultimate Texas Holdem")
    print("Your chips:", player_chips)
    while True:
        try:
            ante = int(input("Ante value: "))
            if int(ante) <= player_chips and int(ante) % 5 == 0 and int(ante) * 3 <= player_chips and int(ante) != 0:
                print("Blind value:", ante)
                break
        except:
            print("Not a valid input")
            continue

    # chips
    player_chips -= ante * 2
    print("Your chips:", player_chips)
    print("Your cards:", player_cards)
    trips = ''
    while trips not in ['y', 'n']:
        trips = (input("Optional. Trips?. (y/n): "))

    # before betting trips, make sure that they have at least 1x of their ante left in player_chips
    while trips in ['y', 'Y']:
        while True:
            try:
                trips = int(input("Trips value: "))
                if int(trips) <= player_chips and int(trips) % 5 == 0 and int(trips) != 0 and (
                        player_chips - trips >= ante):
                    player_chips -= trips
                    print ("Trips:", trips)
                    break
                else:
                    continue
            # this is for "no"
            except:
                print("Not a valid input")
                continue
    print("Your chips:", player_chips)

    # round()
    # single_round(['check', '3x', '4x'])


# print(player_chips)

# global ante still works


def single_round(argument):
    global player_chips, play
    play_wo_check = argument
    argument = ''
    while argument not in play_wo_check:
        argument = input(" or ".join(play_wo_check) + '?')
        if argument == "fold":
            print("Player folded")
            return "Fold"
    play_wo_check.pop(0)
    while argument in play_wo_check:
        if player_chips >= int(play_wo_check[0][0]) * ante:
            for p in play_wo_check:
                if argument == p:
                    print("Play bet:", p)
                    argument = int(p[0]) * ante
                    player_chips -= argument
            print("Player chips:", player_chips)
            print("\n")
            argument = play
            return argument
        else:
            print("Insufficient chips")
            return "No-chips"
    else:
        print("Player Checked")
        return "Checked"


def royal_flush(values, suits):
    if straight_flush(values, suits):
        if int(values[0]) == 10:
            return True


def straight_flush(values, suits):
    return straight(values) and flush(suits)


def four_of_a_kind(values):
    return any(values.count(item) == 4 for item in values)


def full_house(values):
    return len(set(values)) == 2


def flush(suits):
    return len(set(suits)) == 1


def straight(values):
    return len(set(values)) == 5 and (values[-1] - values[0] == 4)


def three_of_a_kind(values):
    return any(values.count(item) == 3 for item in values)


def two_pair(values):
    return len(set(values)) == 3


def one_pair(values):
    return any(values.count(item) == 2 for item in values)


def high_card(values):
    for i in values:
        if i in [11, 12, 13, 14]:
            return True


def check_hand(values, suits):
    if royal_flush(values, suits):
        return 10
    if straight_flush(values, suits):
        return 9
    if four_of_a_kind(values):
        return 8
    if full_house(values):
        return 7
    if flush(suits):
        return 6
    if straight(values):
        return 5
    if three_of_a_kind(values):
        return 4
    if two_pair(values):
        return 3
    if one_pair(values):
        return 2
    if high_card(values):
        return 1
    return 0




def find_best_hand(all_player_hands):
    all_combos = list(map(list, combinations(all_player_hands, 5)))
    best_hand = 0
    for i in all_combos:
        values = [h[:-1] for h in i]
        suits = [h[-1] for h in i]
        dic = {'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        values = [dic.get(n, n) for n in values]
        values = [int(j) for j in values]
        values.sort()
        current_hand = check_hand(values, suits)
        if current_hand > best_hand:
            best_hand = current_hand
    return best_hand


hand_dict = {10: 'royal-flush', 9: 'straight-flush', 8: 'four-of-a-kind', 7: 'full-house', 6: 'flush',
             5: 'straight', 4: 'three-of-a-kind', 3: 'two-pair', 2: 'one-pair', 1: 'high card'}

# best_hand = find_best_hand()
#player_best_hand = (hand_dict.get(find_best_hand(all_player_hands)))
#print("Player, your best hand is,", player_best_hand)
#dealer_best_hand = (hand_dict.get(find_best_hand(all_dealer_hands)))


def srt():
    while player_chips >= 15:
        while True:
            dealer_cards = []
            player_cards = []
            table = []
            shuffle(deck)
            for i in range(2):
                dealer_cards.append(deck[i])
                deck.pop(i)
                player_cards.append(deck[i])
                deck.pop(i)
            for i in range(5):
                table.append(deck[i])
                deck.pop(i)
            pre(player_chips, player_cards)
            if single_round(['check', '3x', '4x']) == play:
                print("The table: ", table)
                # //call the best hand function
            else:
                print("The table: ", table[:3])
                if single_round(['check', '2x']) == play:
                    print("The table: ", table)
                else:
                    print("The table: ", table)
                    if single_round(['fold', '1x']) == play:
                        print("The table is: ", table)  # same thing as saying return None
                    else:
                        break
            print()
            all_player_hands = [*player_cards, *table]
            all_dealer_hands = [*dealer_cards, *table]
            player_best_hand = (hand_dict.get(find_best_hand(all_player_hands)))
            print("Player, your cards are", player_cards)
            print("Player, your best hand is,", player_best_hand)
            dealer_best_hand = (hand_dict.get(find_best_hand(all_dealer_hands)))
            print("Dealer cards:", dealer_cards)
            print("Dealer's best hand is,", dealer_best_hand)
            #print(player_chips)
            #print(ante)
            break

    else:
        print("You don't have sufficient chips to play. Please refresh the game to earn your chips.")


srt()

#print(player_chips)
#print(ante)