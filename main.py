import os
import casino
import playing_cards

global playing

playing = True


# THE ACTUAL SCRIPT #
os.system('cls')
print("WELCOME TO BEN'S CASINO!!\n\n")

total = int(input("How many chips do you want to buy? "))
# Set up the Player's chips  
player_chips = casino.Chips(total)

while True:
    # Print an opening statement
    os.system('cls')
    print("WELCOME TO THE BLACK JACK TABLE!!")

    # Create & shuffle the deck, deal two cards to each player

    the_deck = playing_cards.Deck()
    the_deck.shuffle()
    
    player_hand = playing_cards.Hand()
    player_hand.add_card(the_deck.deal())
    player_hand.add_card(the_deck.deal())
    
    dealer_hand = playing_cards.Hand()
    dealer_hand.add_card(the_deck.deal())
    dealer_hand.add_card(the_deck.deal())
    

    
    # Prompt the Player for their bet
    casino.take_bet(player_chips)
    
    # Show cards (but keep one dealer card hidden)
    casino.show_some(player_hand,dealer_hand)
    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        playing = casino.hit_or_stand(the_deck,player_hand)


        # Show cards (but keep one dealer card hidden)
        casino.show_some(player_hand,dealer_hand)
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            casino.player_busts(player_hand,dealer_hand,player_chips)
            break

    if player_hand.value <= 21:
        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
        while dealer_hand.value < 17:
            casino.hit(the_deck,dealer_hand)

        # Show all cards
        casino.show_all(player_hand,dealer_hand)

        # Run different winning scenarios
        if dealer_hand.value > 21:
            casino.dealer_busts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value > player_hand.value:
            casino.dealer_wins(player_hand,dealer_hand,player_chips)
        elif player_hand.value > dealer_hand.value:
            casino.player_wins(player_hand,dealer_hand,player_chips)
        else:
            casino.push(player_hand,dealer_hand)

    # Inform Player of their chips total 
    print(f"You have {player_chips.total} chips left \n")

    # Ask to play again
    if player_chips.total == 0:
       print("You have lost all your money... muhahahahaah! Bye now!!!\n") 
       break
    else:
        new_game = input("Do you want to play again? Y / N ")

        if new_game.upper() == 'Y':
            playing = True
            continue
        else:
            print("Thanks for visiting Ben's casino. Bye now!")
            break

input('\n\nPRESS ENTER TO EXIT GAME')