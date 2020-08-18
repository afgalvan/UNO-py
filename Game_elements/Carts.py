#!/usr/bin/env python3
from random import randint
from Colors import *


class StandardCarts:
    def __init__(self, index, color):
        self.content = index
        self.color = color
    
    def __str__(self):
        return self.color + "|{0}|".format(self.content)


class PlusFour:
    def __init__(self):
        self.content = "+4"
        self.color = Back.BLACK
        self.aspect = Style.BRIGHT
        
    def __str__(self):
        return self.color + self.aspect + "|{0}|".format(self.content) + Style.RESET_ALL


class PlusFour:
    def __init__(self):
        self.content = Fore.GREEN + "(" + Fore.BLUE + + "\\" + "C" + "/" + ")"
        self.color = Back.BLACK
        self.aspect = Style.BRIGHT
        
    def __str__(self):
        return self.color + self.aspect + "|{0}|".format(self.content) + Style.RESET_ALL

class Reverse:
    def __init__(self, color):
        self.content = "^v"
        self.color = color
    
    def __str__(self):
        return self.color + "|{0}|".format(self.content)

   
class Skip:
    def __init__(self, color):
        self.content = "Ø"
        self.color = color
        
    def __str__(self):
        return self.color + "|{0}|".format(self.content)

        
class PlusTwo:
    def __init__(self, color):
        self.content = "+2"
        self.color = color
        
    def __str__(self):
        return self.color + "|{0}|".format(self.content)




def generate_carts():
    create_carts = [cart for cart in range(0, 10)] * 2
    create_carts = shuffle_cards(create_carts)
    cart_colors = [Fore.RED, Fore.BLUE, Fore.GREEN, Fore.YELLOW]
    cards_array = []
    for i in create_carts:
        for j in cart_colors:
            new = StandardCarts(i, j)
            cards_array.append(new)
    
    return cards_array


def shuffle_cards(cards_array):
    cards_quantity = len(cards_array)
    
    for i in range(cards_quantity-1, 0 , -1):
        rand_index = randint(0, cards_quantity-1)
        cards_array[rand_index], cards_array[i] = cards_array[i], cards_array[rand_index]
        
    return cards_array
