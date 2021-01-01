'''
ante = 10
player_chips = 100

def start():
    global ante
    ante +=200


def single_round(n):
    global ante
    ante+=10
    print(ante)

def hi():
    global ante
    start()
    single_round(ante)

hi()

'''

ante = 10
table = []
player_chips = 500
deck = ['H1', 'H3', 'J10', 'JQ', 'K10', 'S10', 'AS', 'AC', 'AJ']

play = ''
while play.lower() not in ['check', '4x', '3x']:
    play = (input("Check or 4x or 3x?: "))

while player_chips >= 3 * ante:
    try:
        if play == '3x':
            print("Player bet 3x")
            play = 3 * ante
            player_chips -= play
        else:
            play = 4 * ante
            player_chips-=play
        for c in range(5):
            table.append(deck[i])
            deck.pop(i)
                # this else would be for 4x
    except:
        continue
else:
    play = play.lower()
    if play == 'check':
        print("Player checked")
    else:
        print("Insufficient chips")

def single_round(argument, n):
    global player_chips, ante
    print(ante)
     if player_chips >= ante * argument:
     for c in range(n):
         table.append(deck[i])
         deck.pop(i)


def after_bet(argument):
    global table, deck
    table.append(deck[i])


single_round(player_chips, ante)
