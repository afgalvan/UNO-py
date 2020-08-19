# Copyright (c) 2020 by Andrés Galván
import webbrowser
import sys

try:
    sys.path.append("../Gameplay")
    from Game import *
    from Random_color import *
    from Users_management import *
except:
    sys.path.append("Gameplay")
    from Game import *
    from Random_color import *
    from Users_management import *



def main_menu():
    clear_console()
    menu_choice = input(color_change() + """
    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    ┃                                                                     ┃
    ┃                                 UNO.                                ┃
    ┃                                                                     ┃
    ┃           A python terminal game based on UNO card game.            ┃
    ┃                                                                     ┃
    ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
    ┃                                                                     ┃
    ┃    1 - Start new match                                              ┃
    ┃    2 - See player stats                                             ┃
    ┃    3 - See top players                                              ┃
    ┃    4 - Credits                                                      ┃
    ┃                                                                     ┃
    ┃    E - Exit                                                         ┃
    ┃                                                                     ┃
    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
        >> """)
    
    if menu_choice == "1": new_match()
    elif menu_choice == "2": players_stats()
    elif menu_choice == "3": top_players()
    elif menu_choice == "4": credits_menu()
    elif menu_choice.lower() == "e": clear_console(); quit()
    else: main_menu()


def new_match():
    clear_console()
    
    users_choice = input(color_change() + """
    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    ┃                                                                     ┃
    ┃                          Start new match.                           ┃
    ┃                                                                     ┃
    ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
    ┃                                                                     ┃
    ┃    1 - New user                                                     ┃
    ┃    2 - Load user                                                    ┃
    ┃    3 - Back to menu                                                 ┃
    ┃                                                                     ┃
    ┃    E - Exit                                                         ┃
    ┃                                                                     ┃
    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
        >> """)
    
    if users_choice == "1": username = create_user()
    elif users_choice == "2": username = load_user()
    elif users_choice == "3": main_menu()
    elif users_choice.lower() == "e": clear_console(); quit()
    else: new_match()
    
    game_status = start_game(username)
    g = game_status
    save_stats(username, g[0], g[1], g[2])
    new_match()


def players_stats():
    clear_console()
    pass


def top_players():
    clear_console()
    pass


def credits_menu():
    URL = "https://github.com/JuniorWriter/UNO-py"
    
    clear_console()
    credits_choice = input(Fore.WHITE + """
    ╔═════════════════════════════════════════════════════════════════════════╗
    ║                                                                         ║
    ║                                Credits.                                 ║
    ║                                                                         ║
    ╠═════════════════════════════════════════════════════════════════════════╣
    ║                                                                         ║
    ║  This program was made by Andrés Galvan, the only dependency used is    ║
    ║  the Colorama library that, for making this game compatible in all      ║
    ║  desktop platform, it was downloaded and add it as a custom module,     ║
    ║  but all rights are reserved for Jonathan Hartley. All other game       ║
    ║  components were made by Andrés Galván.                                 ║
    ║                                                                         ║
    ╠═════════════════════════════════════════════════════════════════════════╣
    ║                                                                         ║
    ║    1 - Go to repository                                                 ║
    ║    2 - Return to main menu                                              ║
    ║                                                                         ║
    ║                                                                         ║
    ║                                                                         ║
    ║  Copyright (c) 2020 by Andrés Galván                                    ║
    ║                                                                         ║
    ╚═════════════════════════════════════════════════════════════════════════╝
        >> """)
    if credits_choice == "1": webbrowser.open(URL); main_menu()
    elif credits_choice == "2": main_menu()
    else: credits_menu()
