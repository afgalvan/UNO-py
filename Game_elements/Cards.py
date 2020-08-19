# Copyright (c) 2020 by Andrés Galván
from random import randint
from Colors import *


class StandardCards:
    def __init__(self, index, color):
        self.owner = ""
        self.keypress = index
        self.kind = "Numeric"
        self.content = index
        self.color = color
    
    def __str__(self):
        return self.color + "|{0}|".format(self.content)


class Special:
    kind = "Special"
    owner = ""


class PlusFour(Special):
    def __init__(self):
        self.keypress = "+4"
        self.content = "+4"
        self.color = Fore.WHITE
        self.aspect = Fore.WHITE + Back.BLACK + Style.BRIGHT
        
    def __str__(self):
        return self.aspect + "|{0}|".format(self.content) + Style.RESET_ALL
    
    def action(self, player, cards):
        for each in range(4):
            player.eat_card(cards)


class ColorChange(Special):
    def __init__(self):
        self.keypress = "C"
        self.content = Fore.GREEN + "|" + Fore.BLUE + "\\" + Fore.WHITE + "C" + Fore.RED +  "/" + Fore.YELLOW + "|"
        self.color = Fore.WHITE
        self.aspect = Back.BLACK + Style.BRIGHT
        
    def __str__(self):
        return self.aspect + "{0}".format(self.content) + Style.RESET_ALL
    
    def action(self, player, cards):
        if player.kind == "User":
            while True:
                desired_color = input("Enter de letter of your color: ")
                if desired_color.lower() in ["r", "b", "g", "y"]:
                    break
            return desired_color

class Reverse(Special):
    def __init__(self, color):
        self.keypress = "R"
        self.content = "^v"
        self.color = color
    
    def __str__(self):
        return self.color + "|{0}|".format(self.content)
    
    def action(self, game, color_desired):
        pass


   
class Skip(Special):
    def __init__(self, color):
        self.keypress = "S"
        self.content = "(/)"
        self.color = color
        
    def __str__(self):
        return self.color + "|{0}|".format(self.content)
    
    def action(self, player, cards):
        return 

        
class PlusTwo(Special):
    def __init__(self, color):
        self.keypress = "+2"
        self.content = "+2"
        self.color = color
        
    def __str__(self):
        return self.color + "|{0}|".format(self.content)

    def action(self, player, cards):
        for each in range(2):
            player.eat_card(cards)


def generate_cards():
    create_cards = [card for card in range(1, 10)] * 2
    create_cards.append(0)
    card_colors = [Fore.RED, Fore.BLUE, Fore.GREEN, Fore.YELLOW]
    cards_array = []
    
    for i in create_cards:
        for j in card_colors:
            new = StandardCards(str(i), j)
            cards_array.append(new)
            
    for i in range(2):
        cc = ColorChange()
        # cards_array.append(cc)
        # cards_array.append(cc)
        
        pf = PlusFour()
        cards_array.append(pf)
        cards_array.append(pf)
        
        for j in card_colors:
            pt = PlusTwo(j)
            sk = Skip(j)
            rv = Reverse(j)
            
            cards_array.append(pt)
            cards_array.append(sk)
            # cards_array.append(rv)
            
    cards_array = shuffle_cards(cards_array)
    
    return cards_array


def shuffle_cards(cards_array):
    cards_quantity = len(cards_array)
    
    for i in range(cards_quantity-1, 0 , -1):
        rand_index = randint(0, cards_quantity-1)
        cards_array[rand_index], cards_array[i] = cards_array[i], cards_array[rand_index]
        
    return cards_array
