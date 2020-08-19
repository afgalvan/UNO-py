# Copyright (c) 2020 by Andrés Galván
from random import randint
from getpass import getpass
from time import sleep
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


    def show_table(self, player, first):
        clear_console()
        print(Fore.WHITE + Style.BRIGHT + "\n\n\n\n\n\n\nBot's carts:" 
              " {0}\n\n".format(len(bot.hand)) + Style.RESET_ALL)
        
        self.current_cart()
        player.show_hand(first)


    def new_game(self, player):
        player.hand = []
        bot.hand = []
        
        bot.fill_hand(carts)
        player.fill_hand(carts)
        
        self.first_card(carts)
        self.show_table(player, True)
        
        
    def special_moves(self, target, last_cart, contratack):
        contratack += 1
        if (self.card_in_game is last_cart
        or self.card_in_game.keypress != last_cart.keypress):
            for i in range (contratack):
                last_cart.action(target, carts)
            return 0
        return contratack
        
        
        
def clear_console():
    OS = system()
    if OS == "Windows":
        run("cls", shell=True)
    else:
        run("clear")


def turn(player):
    move_allowed = False
    
    while not move_allowed:
        player_move = input(game.card_in_game.color + "Your turn: ")
        # player_move = "f"
        if player_move.lower() == "f":
            player.eat_cart(carts)
            return 1
        elif player_move.lower() == "g":
            player.loses += 1
            return 2
        elif player_move.lower() == "q":
            quit()
        
        move_allowed = player.put_cart(player_move, carts, game)
    return 0


def show_my_move():
    clear_console()
    print(Fore.WHITE + Style.BRIGHT + "\n\n\n\n\n\n\nBot's carts:" 
        " {0}\n\n".format(len(bot.hand)) + Style.RESET_ALL)
    game.current_cart()
    getpass("")


def play_game(player, contratack):
    last_cart = game.card_in_game
    user_cmd = turn(player)
    # user_cmd = 1
    # player.bot_move(game, carts)

    if last_cart.kind == "Special":
        contratack = game.special_moves(player, last_cart, contratack)
    game.show_table(player, False)
    
    if user_cmd == 0:
        show_my_move()
    elif user_cmd == 2:
        return 0

    last_cart = game.card_in_game
    bot.bot_move(game, carts)
    game.show_table(player, False)

    if last_cart.kind == "Special":
        contratack = game.special_moves(bot, last_cart, contratack)

    game.show_table(player, False)


def start_game(username):
    clear_console()
    
    player = Player(username)
    game.new_game(player)
    player.matches += 1
    contratack = 0
    
    while True:
        play_game(player, contratack)

        if len(bot.hand) < 1:
            winner = bot.name
            player.loses += 1
            break
        elif len(player.hand) < 1:
            winner = player.name
            player.wins += 1
            break
      
    return (player.matches, player.wins, player.loses)


game = Game()

start_game("PIPE")