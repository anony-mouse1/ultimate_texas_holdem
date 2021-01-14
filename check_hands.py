from itertools import combinations

# dic = {'J': 11, 'Q': 12, 'K': 13, 'A': 14}
# values = [dic.get(n, n) for n in values]
# values = [int(i) for i in values]
# values.sort()
# print("Sorted hand:", values)

table = ['AC', 'KC', 'QC', '6D', '9D']
player_cards = ['JC', '10C']
player_hand = [*table, *player_cards]


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


player_best_hand = 0


def find_best_hand():
    global player_best_hand

    all_combos = list(map(list, combinations(player_hand, 5)))
    for h in all_combos:
        values = [h[:-1] for h in h]
        suits = [h[-1] for h in h]
        dic = {'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        values = [dic.get(n, n) for n in values]
        values = [int(j) for j in values]
        values.sort()
        current_hand = check_hand(values, suits)
        if current_hand > player_best_hand:
            player_best_hand = current_hand
    return player_best_hand


hand_dict = {10: 'royal-flush', 9: 'straight-flush', 8: 'four-of-a-kind', 7: 'full-house', 6: 'flush',
                   5: 'straight', 4: 'three-of-a-kind', 3: 'two-pair', 2: 'one-pair', 1: 'high card'}

#best_hand = find_best_hand()
player_best_hand = (hand_dict.get(find_best_hand()))
print("Player, your best hand is,", player_best_hand)
