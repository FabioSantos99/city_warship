# C
import pygame

COLOR_ORANGE = (255, 128, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW = (255, 255, 128)

# M
MENU_OPTION = ("NEW GAME 1P",
               "NEW GAME 2P - COOPERATIVE",
               "NEW GAME 2P - COMPETITIVE",
               "EXIT")

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324

# E
EVENT_ENEMY = pygame.USEREVENT + 1

ENTITY_SPEED = {'city0': 0,
                'city1': 1,
                'city2': 1,
                'city3': 3,
                'city4': 8,
                'city5': 6,
                'Player1': 3,
                'Player2': 3,
                'Enemy1': 1,
                'Enemy2': 2,
                }

ENTITY_HEALTH = {'city0': 999,
                 'city1': 999,
                 'city2': 999,
                 'city3': 999,
                 'city4': 999,
                 'city5': 999,
                 'Player1': 300,
                 'Player2': 300,
                 'Enemy1': 200,
                 'Enemy2': 200,
                 }

PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                   'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                   'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                    'Player2': pygame.K_d}
