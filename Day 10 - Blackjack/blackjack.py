import random
import os

class Card:
    values = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    def cards(player_cards, dealer_cards):
        print("Your cards are: ")
        print(player_cards)
        print("Your total Sum is: " + str(Card.Suma(player_cards)))
        print("The dealers cards are: ")
    def InitialCards(player_cards, dealer_cards):
        Card.cards(player_cards, dealer_cards)
        print(dealer_cards[0])
    def DealtCards(set_cards):
        set_cards.append(random.choice(Card.values))
        set_cards.append(random.choice(Card.values))
        if Card.Suma(set_cards) == 21:
            return "Blackjack"
        elif Card.Suma(set_cards) > 21:
            return "Bust"
        else:
            return "No Blackjack"
    def Suma(set_cards):
        return sum(set_cards)
    def Change(set_cards):
        if Card.Suma(set_cards) > 21 and 11 in set_cards:
            set_cards.remove(11)
            set_cards.append(1)
    def Analysis(player_cards, dealer_cards):
        suma_player = Card.Suma(player_cards)
        suma_dealer = Card.Suma(dealer_cards)
        Card.cards(player_cards, dealer_cards)
        print(dealer_cards)
        print("The dealers total Sum is: " + str(suma_dealer))
        if suma_player == 21:
            print("You got 21! You win!")
        elif suma_dealer == 21:
            print("The dealer got 21! You lose!")
        elif suma_player > 21:
            print("You are bust! You lose!")
        elif suma_dealer > 21:
            print("The dealer is bust! You win")
        elif suma_player == suma_dealer:
            print("Draw")
        elif suma_player > suma_dealer:
            print("You win")
        elif suma_player < suma_dealer:
            print("You lose")
        game()



class Dealer:
    def CardsForDealer(dealer_cards, player_cards):
        print("The dealer grab 2 cards")
        BJ = Card.DealtCards(dealer_cards)
        if BJ == "Blackjack" or BJ == "Bust":
            Card.Analysis(player_cards, dealer_cards)
    def ExtraCardForDealer(dealer_cards):
        print("The dealer got an extra card because his sum is less than 17")
        dealer_cards.append(random.choice(Card.values))
        Card.Change(dealer_cards)


class Player:
    def CardsForPlayer(player_cards, dealer_cards):
        print("The dealer gave you 2 cards")
        BJ = Card.DealtCards(player_cards)
        if BJ == "Blackjack" or BJ == "Bust":
            Card.Analysis(player_cards, dealer_cards)
    def ExtraCardForPlayer(player_cards, dealer_cards):
        if Card.Suma(dealer_cards) < 17:
            Dealer.ExtraCardForDealer(dealer_cards)
        player_cards.append(random.choice(Card.values))
        Card.Change(player_cards)


def game():
    play = True
    while play == True:
        more_cards = True
        dealer_cards = []
        player_cards = []
        print("\nmWelcome to blackjack")
        choice = input("would you like to play? (y/n) ")
        os.system("cls")
        if choice == "y":
            print("The cards will be dealt to you and the dealer")
            Dealer.CardsForDealer(dealer_cards, player_cards)
            Player.CardsForPlayer(player_cards, dealer_cards)
            Card.InitialCards(player_cards, dealer_cards)
            while more_cards == True:
                if input("Would you like another card? (y/n) ") == "y":
                    Player.ExtraCardForPlayer(player_cards, dealer_cards)
                    Card.InitialCards(player_cards, dealer_cards)
                    if Card.Suma(player_cards) > 21 or Card.Suma(player_cards) == 21:
                        Card.Analysis(player_cards, dealer_cards)
                elif Card.Suma(dealer_cards) < 17:
                    while Card.Suma(dealer_cards) < 17:
                        Dealer.ExtraCardForDealer(dealer_cards)
                        Card.InitialCards(player_cards, dealer_cards)
                    if Card.Suma(dealer_cards) > 21:
                        Card.Analysis(player_cards, dealer_cards)
                    more_cards = False
                else:
                    more_cards = False
            Card.Analysis(player_cards, dealer_cards)
        elif choice == "n":
            print("Goodbye")
            play = False
        else:
            print("invalid input")

game()
