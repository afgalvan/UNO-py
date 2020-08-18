#!/usr/bin/env python3
from random import randint
from getpass import getpass
from platform import system
from subprocess import run
import sys
try:
    sys.path.append("../Game_elements")
    from Players import *
except:
    sys.path.append("Game_elements")
    from Players import *



global carts
global game
global bot


carts = generate_carts()
bot = Bot("Larry")

class Game:
    def __init__(self):
        self.card_in_game = None


    def first_card(self, carts_array):
        rand_index = randint(0, len(carts_array)-1)
        remove_cart = carts_array[rand_index]
        
        self.card_in_game = remove_cart
        carts_array.remove(remove_cart)


    def current_cart(self):
        print("\n\n\t\t\t\t", end="")
        print(self.card_in_game)
        print("\n\n\n\n\n\n\n\n\n\n")


    def show_table(self, player):
        print(Fore.WHITE + Style.BRIGHT + "\n\n\n\n\n\n\nBot's carts:" 
              "{0}\n\n".format(len(bot.hand)) + Style.RESET_ALL)
        
        self.current_cart()
        player.show_hand()


    def new_game(self, player):
        bot.fill_hand(carts)
        player.fill_hand(carts)
        
        self.first_card(carts)
        self.show_table(player)


def start_game():
    OS = system()
    if OS == "Windows":
        run("cls", shell=True)
    else:
        run("clear")
        
    player1 = Player("Andres")
    game.new_game(player1)


game = Game()
start_game()