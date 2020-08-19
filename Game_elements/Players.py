# Copyright (c) 2020 by Andrés Galván
from random import randint
from getpass import getpass
from Colors import *
from Cards import generate_cards

class Player:
    kind = "User"
    wins = 0
    matches = 0
    loses = 0
    

    def __init__(self, name):
        self.name = name
        self.hand = []


    def __str__(self):
        return "{0}".format(self.name)


    def eat_card(self, cards_array):
        rand_index = randint(0, len(cards_array)-1)
        remove_card = cards_array[rand_index]

        self.hand.append(remove_card)
        cards_array.remove(remove_card)


    def put_card(self, card, cards_array, game):
        you_have_this = False
        
        if (game.card_in_game.kind == "Special"
        and game.card_in_game.owner != self.name):
            if card != game.card_in_game.keypress:
                return True

        for i in self.hand:
            if i.keypress == card.upper():
                you_have_this = True
                save_card = i
                
                if (i.keypress == game.card_in_game.keypress
                or i.color == game.card_in_game.color
                or i.color == Fore.WHITE
                or game.card_in_game.color == Fore.WHITE):
                    self.hand.remove(i)
                    cards_array.append(game.card_in_game)
                    game.card_in_game = i
                    return True

        if self.kind == "Bot": return False

        if you_have_this:    
            print(save_card.color + "\t\t({0}) <─ You can't "
            "play this card.".format(save_card.content))
            return False     

        print("\t\t({0}) <─ You don't have "
        "this card.".format(card))
        return False


    def fill_hand(self, cards_array):
        for i in range(7):
            self.eat_card(cards_array)


    def show_hand(self):
        for i in self.hand:
            print("\t{}".format(i), end="")
        print("\n")



class Bot(Player):
    kind = "Bot"
    
    def __str__(self):
        return "{0} bot".format(self.name)


    def bot_move(self, game, cards):
        last_card = game.card_in_game      
        moved = False
        while not moved:
            for c in self.hand:
                moved = self.put_card(c.keypress, cards, game)
                if moved:
                    break

            if not moved:
                self.eat_card(cards)
                return 1
        if last_card is game.card_in_game: return 2
        return 0
