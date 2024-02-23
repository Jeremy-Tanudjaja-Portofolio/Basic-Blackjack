import random as rand

# TODO 1 Create a Dictionary of the available card values
CARD_VALUES = {
    "Ace": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10
}
player_value = 0
dealer_value = 0


# TODO 2 Create a function to hit a player with a card
def playerHit():
    global player_value
    hit = rand.choice(list(CARD_VALUES))
    print(f" You got {hit} with a value of {CARD_VALUES[hit]}")
    if hit == "Ace":
        choice = input("1 or 11?")
        if choice == "1":
            player_value += 1
            return
        else:
            player_value += 11
            return
    player_value = player_value + CARD_VALUES[hit]
    print(f"Your value is now {player_value}")


# TODO 3 Create a function to hit a dealer with a card, if dealer has a card value of under 17, he must deal again to himself
def dealerHit():
    global dealer_value
    hit = rand.choice(list(CARD_VALUES))
    if hit == "Ace" and dealer_value > 9:
        dealer_value += 11
        return
    else:
        dealer_value += 1
        return
    dealer_value = dealer_value + CARD_VALUES[hit]


# TODO 4 Create a function to loop through other function
def startGame():
    global player_value, dealer_value
    choice = input("Do you want to grab a card?Y|N\n").lower()
    if choice == "y":
        playerHit()
        dealerHit()
        startGame()
    else:
        while dealer_value <= 17:
            dealerHit()
        if player_value > dealer_value and player_value < 22:
            print(f"Congrats player, you've won with a score of{player_value}")
        elif dealer_value > 21:
            print(f"You've won, dealer has more than 21 value with a value of {dealer_value}")
        elif dealer_value > player_value or player_value > 21:
            print(f"Too bad you've lost, the dealer has {dealer_value} while you have {player_value}")


# TODO 5 start the game

game = True

while game:
    choice = input("Do you want to play blackjack? Y|N\n").lower()
    if choice == "y":
        print('''
         _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
                       _/ |                
                      |__/  
        ''')
        startGame()
    else:
        print("Okay")
        game = False
