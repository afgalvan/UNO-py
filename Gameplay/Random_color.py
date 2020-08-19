from random import choice
import sys
try:
    sys.path.append("../Game_elements")
    from Colors import *
except:
    sys.path.append("Game_elements")
    from Colors import *
    
def color_change():
    color_list = [Fore.RED, Fore.BLUE, Fore.GREEN, Fore.YELLOW]
    return choice(color_list)
