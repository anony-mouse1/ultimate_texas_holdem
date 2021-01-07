from itertools import combinations
hand = ['2H', '7S', '10S', 'JD', '2C']
hand_values = [h[:-1] for h in hand]
hand_suits = [h[-1] for h in hand]

dic = {'J':11, 'Q':12, 'K':13, 'A': 14}
hand_values = [dic.get(n, n) for n in hand_values]
hand_values = [int(i) for i in hand_values]
hand_values.sort()
print("Sorted hand:", hand_values)


def royal_flush():
    if straight() and flush():
        if int(hand_values[0]) == 10:
            return True


def straight_flush():
    return straight() and flush()


def four_of_a_kind():
    return any(hand_values.count(item) == 4 for item in hand_values)


def full_house():
    return len(set(hand_values)) == 2


def flush():
    return len(set(hand_suits)) == 1


def straight():
    return len(set(hand_values)) == 5 and (hand_values[-1] - hand_values[0] == 4)


def three_of_a_kind():
    return any(hand_values.count(item) == 3 for item in hand_values)


def two_pair():
    return len(set(hand_values)) == 3


def one_pair():
    return any(hand_values.count(item) == 2 for item in hand_values)


check_hand_dict = {10: 'royal-flush', 9: 'straight-flush', 8: 'four-of-a-kind', 7: 'full-house', 6: 'flush',
                  5: 'straight', 4: 'three-of-a-kind', 3: 'two-pair', 2: 'one-pair', 1:'high card'}


def check_hand():
    if royal_flush():
        return 10
    if straight_flush():
        return 9
    if four_of_a_kind():
        return 8
    if full_house():
        return 7
    if flush():
        return 6
    if straight():
        return 5
    if three_of_a_kind():
        return 4
    if two_pair():
        return 3
    if one_pair():
        return 2
    return 1




