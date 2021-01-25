trips = 5
ante = 20
player_chips = 400
play = 40

player_best_hand = 2
dealer_best_hand = 5


trips_payout = {4: trips * 4, 5: trips * 6, 6: trips * 7, 7: trips * 9, 8: trips * 31, 9: trips * 41, 10: trips * 51}
blind_payout = {5: ante * 2, 6: ante * 2.5, 7: ante * 4, 8: ante * 11, 9: ante * 51, 10: ante * 501}


def payouts(player_best_hand, dealer_best_hand):
    global player_chips
    payout= 0
    if dealer_best_hand > 1:
        print("Dealer qualifies...")  # this just means if dealer hand qualifies
        if dealer_best_hand > player_best_hand:
            print("Darn... the dealer beat you!!")
            pass
        elif dealer_best_hand < player_best_hand:
            print("Great moves! You beat the dealer!!")
            player_chips += ante * 2
            player_chips += play * 2
            print("Ante payout is...", ante * 2)
            print("Play payout is...", play * 2)
            player_chips += blind_payout.get(player_best_hand, ante)
            print("Blind Payout is...", blind_payout.get(player_best_hand, ante))
        else:
            print("A tie!!!")
            print("Ante, blind and play will be returned back to player")
            player_chips += ante * 2  # so then its ante and blind together
            player_chips += play

            # this is pushing back
    else:
        print("Dealer does not qualify...")  # if dealer doesn't qualify
        print("Ante is returned...")
        player_chips += ante  # ante bet is returned
        if dealer_best_hand > player_best_hand:
            print("Darn... the dealer beat you!!")
            pass
        elif dealer_best_hand < player_best_hand:
            print("Great moves! You beat the dealer!!")
            player_chips += play * 2
            print("Play Payout:", play * 2)
            player_chips += blind_payout.get(player_best_hand, ante)
            print("Blind Payout is...", blind_payout.get(player_best_hand, ante))
        else:
            print("A tie!!!")
            print("Blind and play will be returned back to player")
            player_chips += ante  # return blind back to player
            player_chips += play
    if trips != 'n':
        player_chips += trips_payout.get(player_best_hand, 0)
        print("Trips payout is...", trips_payout.get(player_best_hand, 0))
    print("Player, your final chips of the round:", player_chips)


payouts(player_best_hand, dealer_best_hand)

