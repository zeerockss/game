from classes.Player import Player
from initial_rooms import rooms
import pygame
import tkinter

root = tkinter.Tk()

pygame.init()

display = pygame.display.set_mode(
    (root.winfo_screenwidth(), root.winfo_screenheight()))

pygame.display.set_caption('Untitled')

running = True
while running:
    pygame.time.delay(100)

    for event in pygame.event.get():
        print(event, event.type)
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

# intro_text = [
#     '''You have been travelling for hours. Your mother is taking you to a scrapyard to buy
#     a project car that your father wants you to build with him - from the frame up.'''
# ]


# def print_help():
#     print('''
#         Help Menu
#         Options (type these commands):
#         \t"HP" or "HEALTH" to view your health,
#         \t"H" or "HELP" to view this screen again,
#         \tor "Q" or "QUIT" to quit the game.
#     ''')


# print(intro_text[0])


# player = Player(input('Enter your name: '), rooms['intro'])

# print_help()

# global running
# running = True


# while running:
#     room = player.room

#     def quit_game():
#         print('Thanks for playing!')
#         global running
#         running = False

#     commands = {
#         'q': quit_game,
#         'quit': quit_game,
#         'h': print_help,
#         'help': print_help,
#         'hp': player.print_health,
#         'health': player.print_health,
#     }

#     command = input('\nWhat would you like to do? ').lower()

#     if command in commands:
#         commands[command]()
#     else:
#         print(f'Unable to recognize "{command}".')
