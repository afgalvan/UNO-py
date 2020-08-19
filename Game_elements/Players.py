# Copyright (c) 2020 by Andrés Galván
from random import randint
from time import sleep
from Colors import *
from Carts import generate_carts

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


    def eat_cart(self, carts_array):
        rand_index = randint(0, len(carts_array)-1)
        remove_cart = carts_array[rand_index]

        self.hand.append(remove_cart)
        carts_array.remove(remove_cart)


    def put_cart(self, cart, carts_array, game):
        you_have_this = False

        for i in self.hand:
            if i.keypress == cart.upper():
                you_have_this = True
                save_cart = i
                
                if game.card_in_game.color == Fore.WHITE:
                    self.hand.remove(i)
                    carts_array.append(game.card_in_game)
                    game.card_in_game = i
                    return True
                
                if (i.keypress == game.card_in_game.keypress
                 or i.color == game.card_in_game.color
                 or i.color == Fore.WHITE):
                    self.hand.remove(i)
                    carts_array.append(game.card_in_game)
                    game.card_in_game = i
                    return True

        if self.kind == "Bot": return False

        if you_have_this:    
            print(save_cart.color + "\t\t({0}) <─ You can't "
            "play this card.".format(save_cart.content))
            return False     

        print("\t\t({0}) <─ You don't have "
        "this card.".format(cart))
        return False


    def fill_hand(self, carts_array):
        for i in range(7):
            self.eat_cart(carts_array)


    def show_hand(self, first):
        for i in self.hand:
            if first: sleep(0.5)
            print("\t{}".format(i), end="")
        print("\n")



class Bot(Player):
    kind = "Bot"
    
    def __str__(self):
        return "{0} bot".format(self.name)


    def bot_move(self, game, carts):        
        moved = False
        while not moved:
            for c in self.hand:
                moved = self.put_cart(c.keypress, carts, game)
                if moved:
                    print("Sweet move.")
                    break

            if not moved:
                print("Gotta eat.")
                self.eat_cart(carts)
                break
            
