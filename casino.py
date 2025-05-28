import os

class Chips:
    
    def __init__(self,total):
        self.total = total  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet

# FUNCTIONS #

def take_bet(chips):
    
    while True:
        try:
            chips.bet = int(input(f"How much do you want to bet?\n"
                        f"(You currently have {chips.total} chips)\n\n"))
        except ValueError:
            print("Invalid input. Please enter a number")
        else:
            if chips.bet > chips.total:
                print("Sorry, you don't have enough chips to place this bet!\n"
                f"Please place a bet below {chips.total} chips.")
            else:
                break
def hit(deck,hand):
    
    hand.add_card(deck.deal())
    hand.adjust_for_ace()
    
def hit_or_stand(deck,hand):
    #global playing  # to control an upcoming while loop

    while True:
        player_choice = input("Do you want to hit or stand? Type H to hit or S to stand: ")
        
        if player_choice.upper() == 'H':
            hit(deck,hand)
            return True
        elif player_choice.upper() == 'S':
            print("Player stands. Dealer is on.")
            #playing = False
            return False
        else:
            print("Sorry, wrong input. Please type 'H' or 'S'.")
            continue
        
        break

def show_some(player,dealer):
    os.system('cls')
    print("Dealer's hand:", "<CARD HIDDEN>", dealer.cards[1], sep='\n ')
    print("\n")
    print("Player's hand:", *player.cards, sep='\n ')
    print("Player's hand =",player.value,)
    print("\n")

def show_all(player,dealer):
    
    os.system('cls')
    print("Dealer's hand:", *dealer.cards, sep='\n ')
    print("Dealer's hand =",dealer.value)
    print("\n")
    print("Player's hand:", *player.cards, sep='\n ')
    print("Player's hand =",player.value) 
    print("\n")

def player_busts(player,dealer,chips):
    print("Player busts! You have lost {} chips\n".format(chips.bet))
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Congrats! You won {} chips!\n".format(chips.bet))
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Dealer busts! You won {} chips!\n".format(chips.bet))
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("Dealer wins! You lost {} chips. Hahahaha!!!\n".format(chips.bet))
    chips.lose_bet()
    
def push(player,dealer):
    pass