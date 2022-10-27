import pygame


# window settings
WIDTH, HEIGHT = 320 * 3, 180 * 3
FLAGS = pygame.SCALED

# clock settings
FPS = 60
ACTUAL_FRAME_COEFFICIENT = 16
ACTUAL_FRAME_MIN = 0.5
ACTUAL_FRAME_MAX = 3

# tile settings
TILE_SIZE = 32

# physics
GRAVITY = pygame.Vector2(0, 5)
