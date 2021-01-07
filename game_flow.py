from itertools import combinations
from random import shuffle

# branch card




trips = 0
player_chips = 200
ante = 50
play = 0
dealer_chips = float('inf')


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

#for i in range(5):
 #   table.append(deck[i])
  #  deck.pop(i)

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
                # break
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

    round()
    #single_round(['check', '3x', '4x'])


# print(player_chips)

# global ante still works



def round():
    global player_chips, ante
    print("Your cards are:", player_cards[0], 'and', player_cards[1])



def single_round(argument):
    global player_chips, play
    play_wo_check = argument
    argument = ''
    while argument not in play_wo_check:
        argument = input(" or ".join(play_wo_check) + '?')
    play_wo_check.pop(0)
    while argument in play_wo_check:
        if player_chips >= int(play_wo_check[0][0]) * ante:
            for i in play_wo_check:
                if argument == i:
                    print("Play bet:", i)
                    argument = int(i[0]) * ante
                    player_chips -= argument
            break
        else:
            print("Insufficient chips")
            break
    else:
        print("Player Checked")
    play = argument
    for c in range(5 - len(table)):
        table.append(deck[c])
        deck.pop(c)
        print("Table: ", table)

single_round(['check', '3x', '4x'])
#just to see if it works
# check, lowest to highest


# start()



def srt():
    if player_chips > 15:
        pre()
    else:
        print("You don't have sufficient chips to play. Please refresh the game to earn your chips.")


srt()

player_hands = [*player_cards, *table]
dealer_hands = [*dealer_cards, *table]

#then you do the combinations thing
