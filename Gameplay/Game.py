# Copyright (c) 2020 by Andrés Galván
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



global cards
global game
global bot


cards = generate_cards()
bot = Bot("Larry")

class Game:
    def __init__(self):
        self.card_in_game = None


    def first_card(self, cards_array):
        while True:
            rand_index = randint(0, len(cards_array)-1)
            remove_card = cards_array[rand_index]
            if remove_card.kind != "Special": break
        
        self.card_in_game = remove_card
        cards_array.remove(remove_card)


    def current_card(self):
        print("\n\n\t\t\t\t", end="")
        print(self.card_in_game)
        print("\n\n\n\n\n\n\n\n\n\n")


    def show_table(self, player):
        clear_console()
        print(Fore.WHITE + Style.BRIGHT + 
        "\n\n\n\n\n\n\nBot's cards:" 
        " {0}\n\n".format(len(bot.hand)) + Style.RESET_ALL)
        
        self.current_card()
        player.show_hand()


    def new_game(self, player):
        player.hand = []
        bot.hand = []
        
        bot.fill_hand(cards)
        player.fill_hand(cards)
        
        self.first_card(cards)
        self.show_table(player)


    def players_turn(self, player):
        last_card = self.card_in_game
        move_allowed = False
        only_cards = False
        if self.card_in_game.kind == "Special": only_cards = True
        
        while not move_allowed:
            player_move = input(self.card_in_game.color + "Your turn: ")
            # player_move = "f"
            if player_move.lower() == "f":
                if (not only_cards or
                self.card_in_game.owner == player.name):
                    player.eat_card(cards)
                    return 1
                else:
                    getpass("Fishing not allowed.")
                    continue
            elif player_move.lower() == "g":
                player.loses += 1
                return 2
            elif player_move.lower() == "q":
                quit()
            
            move_allowed = player.put_card(player_move, cards, game)
            
        if last_card is self.card_in_game:
            return 3
        return 0


    def show_players_move(self):
        clear_console()
        print(Fore.WHITE + Style.BRIGHT + "\n\n\n\n\n\n\nBot's cards:" 
            " {0}\n\n".format(len(bot.hand)) + Style.RESET_ALL)
        self.current_card()
        getpass("Enter to continue...")


    def special_moves(self, target, last_card, contratack):
        contratack += 1
        if (self.card_in_game is last_card
        or self.card_in_game.keypress != last_card.keypress
        and self.card_in_game.owner != target.name):
            for i in range (contratack):
                last_card.action(target, cards)
            return 0
        return contratack

            
        
def clear_console():
    OS = system()
    if OS == "Windows":
        run("cls", shell=True)
    else:
        run("clear")


def play_game(player, contratack):
    last_card = game.card_in_game
    while True:
        user_cmd = game.players_turn(player)
        if user_cmd == 0:
            game.card_in_game.owner = player.name
            game.show_players_move()
            if game.card_in_game.keypress != "S": break
        elif user_cmd == 1: break
        elif user_cmd == 2: return None

        if last_card.kind == "Special":
            contratack = game.special_moves(player, last_card, contratack)
            if contratack == 0: break
        game.show_table(player)  
    game.show_table(player)
    
    if len(player.hand) < 1: return 0    

    last_card = game.card_in_game
    while True:
        bot_cmd = bot.bot_move(game, cards)
        if bot_cmd == 0:
            game.card_in_game.owner = bot.name
            if game.card_in_game.keypress != "S": break
        elif bot_cmd == 1: break
        
        if last_card.kind == "Special":
            contratack = game.special_moves(bot, last_card, contratack)
            if contratack == 0: break
        game.show_table(player)
    game.show_table(player)
    
    
    return contratack


def start_game(username):
    clear_console()
    
    player = Player(username)
    game.new_game(player)
    player.matches += 1
    contratack = 0
    
    while True:
        contratack = play_game(player, contratack)
        if contratack == None: break

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
