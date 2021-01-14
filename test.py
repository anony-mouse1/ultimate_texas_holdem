from itertools import combinations


table = ['3C', '4C', '2C', '6C', '8D']
player_cards = ['10C', 'JC']
player_hand = [*table, *player_cards]


def royal_flush(player_values, player_suits):
    if straight_flush(player_values, player_suits):
        return int(player_values[0]) == 10


def straight_flush(player_values, player_suits):
    return straight(player_values) and flush(player_suits)


def four_of_a_kind(player_values):
    return any(player_values.count(item) == 4 for item in player_values)


def full_house(player_values):
    return len(set(player_values)) == 2


def flush(player_suits):
    return len(set(player_suits)) == 1


def straight(player_values):
    return len(set(player_values)) == 5 and (player_values[-1] - player_values[0] == 4)


def three_of_a_kind(player_values):
    return any(player_values.count(item) == 3 for item in player_values)


def two_pair(player_values):
    return len(set(player_values)) == 3


def one_pair(player_values):
    return any(player_values.count(item) == 2 for item in player_values)


def high_card(player_values):
    for i in player_values:
        if i in [11, 12, 13, 14]:
            return True


def check_hand(player_values, player_suits):
    if royal_flush(player_values, player_suits):
        return 10
    if straight_flush(player_values, player_suits):
        return 9
    if four_of_a_kind(player_values):
        return 8
    if full_house(player_values):
        return 7
    if flush(player_suits):
        return 6
    if straight(player_values):
        return 5
    if three_of_a_kind(player_values):
        return 4
    if two_pair(player_values):
        return 3
    if one_pair(player_values):
        return 2
    if high_card(player_values):
        return 1
    return 0


hand_dict = {10: 'royal-flush', 9: 'straight-flush', 8: 'four-of-a-kind', 7: 'full-house', 6: 'flush',
                   5: 'straight', 4: 'three-of-a-kind', 3: 'two-pair', 2: 'one-pair', 1: 'high card'}


def find_best_hand():
    all_combos = list(map(list, combinations(player_hand, 5)))

    for i in all_combos:
        player_values = [h[:-1] for h in i]
        player_suits = [h[-1] for h in i]
        dic = {'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        player_values = [dic.get(n, n) for n in player_values]
        player_values = [int(j) for j in player_values]
        player_values.sort()
        current_hand = check_hand(player_values, player_suits)
        current_hand = hand_dict.get(current_hand)
        print("Hand:", i, 'Type: ', current_hand)


find_best_hand()