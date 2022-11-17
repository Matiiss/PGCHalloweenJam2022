import pygame


# window settings
_SIZE_MULTIPLIER = 2
WIDTH, HEIGHT = 320 * _SIZE_MULTIPLIER, 180 * _SIZE_MULTIPLIER
FLAGS = pygame.SCALED

USE_SHADERS = False

# clock settings
FPS = 30 * 2

# tile settings
TILE_SIZE = 32

# physics
GRAVITY = pygame.Vector2(0, 900)

PLAYER_X_VEL = 200
PLAYER_Y_TERMINAL_VEL = 400
PLAYER_JUMP_POWER = 100 * 3.7

# debugging
DEBUG = True
