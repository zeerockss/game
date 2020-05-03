from classes.Player import Player
from initial_rooms import rooms

intro_text = [
    '''You have been travelling for hours. Your mother is taking you to a scrapyard to buy 
    a project car that your father wants you to build with him - from the frame up.'''
]

intro_commands = {}


def intro():
    player = Player(rooms['intro'])

    return player
