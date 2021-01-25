# ultimate_texas_holdem
# RELEASE NOTES 
#V1
Version 1
This version will have:
Ante
Trips
Play
Blind
All three traditional betting rounds
Fold
Shows best hand out of 7 cards (table and player cards)
Handles most exception errors for user input (if you write wrong type() or the wrong type of int)

Few things to keep in mind:
This version doesn’t support exact measurements for best hand. If dealer and player have the same type of card, then the chips automatically go to the dealer. 
This version doesn’t support:
Payouts. It’s the traditional game, except without any money returned, so no losses or wins. 
Winner of same type of card: for instance, if the dealer and player both have a flush, in my next version, the payout will go to the player. So, the player has the nudge over same type of cards. 
#V1.1
In this version, payouts ARE given. Refer to official UTH documentation for exact payouts and rules. Working on modifying the code to make it less lengthy and re-use functions efficiently. 
In this version, the type of card is solely based on the rank of card. In other words, if both player and dealer have a flush, it will automatically be a tie, regardless if the player (for instance) has a higher rank of flush. ONLY rank of card is taken into account when comparing the dealer's and player's hand. 

Future Updates:
convert into classes to avoid using globals
