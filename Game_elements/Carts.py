# Copyright (c) 2020 by Andrés Galván
from random import randint
from Colors import *


class StandardCarts:
    def __init__(self, index, color):
        self.keypress = index
        self.kind = "Numeric"
        self.content = index
        self.color = color
    
    def __str__(self):
        return self.color + "|{0}|".format(self.content)


class PlusFour:
    def __init__(self):
        self.keypress = "+4"
        self.content = "+4"
        self.kind = "Special"
        self.color = Fore.WHITE
        self.aspect = Fore.WHITE + Back.BLACK + Style.BRIGHT
        
    def __str__(self):
        return self.aspect + "|{0}|".format(self.content) + Style.RESET_ALL
    
    def action(self, player, carts):
        for each in range(4):
            player.eat_cart(carts)


class ColorChange:
    def __init__(self):
        self.keypress = "C"
        self.content = Fore.GREEN + "|" + Fore.BLUE + "\\" + Fore.WHITE + "C" + Fore.RED +  "/" + Fore.YELLOW + "|"
        self.kind = "Special"
        self.color = Fore.WHITE
        self.aspect = Back.BLACK + Style.BRIGHT
        
    def __str__(self):
        return self.aspect + "{0}".format(self.content) + Style.RESET_ALL
    
    def action(self, game, color_desired):
        pass
    #     game.card_in_game.color = color_desired

class Reverse:
    def __init__(self, color):
        self.keypress = "R"
        self.content = "^v"
        self.kind = "Special"
        self.color = color
    
    def __str__(self):
        return self.color + "|{0}|".format(self.content)
    
    def action(self, game, color_desired):
        pass


   
class Skip:
    def __init__(self, color):
        self.keypress = "S"
        self.content = "(/)"
        self.kind = "Special"
        self.color = color
        
    def __str__(self):
        return self.color + "|{0}|".format(self.content)
    
    def action(self, game, color_desired):
        pass

        
class PlusTwo:
    def __init__(self, color):
        self.keypress = "+2"
        self.content = "+2"
        self.kind = "Special"
        self.color = color
        
    def __str__(self):
        return self.color + "|{0}|".format(self.content)

    def action(self, player, carts):
        for each in range(2):
            player.eat_cart(carts)


def generate_carts():
    create_carts = [cart for cart in range(1, 10)] * 2
    create_carts.append(0)
    cart_colors = [Fore.RED, Fore.BLUE, Fore.GREEN, Fore.YELLOW]
    cards_array = []
    
    for i in create_carts:
        for j in cart_colors:
            new = StandardCarts(str(i), j)
            cards_array.append(new)
            
    for i in range(2):
        cc = ColorChange()
        cards_array.append(cc)
        cards_array.append(cc)
        
        pf = PlusFour()
        cards_array.append(pf)
        cards_array.append(pf)
        
        for j in cart_colors:
            pt = PlusTwo(j)
            sk = Skip(j)
            rv = Reverse(j)
            
            cards_array.append(pt)
            cards_array.append(sk)
            cards_array.append(rv)
            
    cards_array = shuffle_cards(cards_array)
    
    return cards_array


def shuffle_cards(cards_array):
    cards_quantity = len(cards_array)
    
    for i in range(cards_quantity-1, 0 , -1):
        rand_index = randint(0, cards_quantity-1)
        cards_array[rand_index], cards_array[i] = cards_array[i], cards_array[rand_index]
        
    return cards_array

# carts = generate_carts()
# print(len(carts))
# for i in carts:
#     print(i, end = " - ")
# print()