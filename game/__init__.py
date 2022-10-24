import itertools

import pygame

from . import common, settings, scenes, assets
from .renderer import Renderer
from .utils import average_blur
from .utils.assets import load_map


pygame.init()

screen = pygame.display.set_mode(
    (settings.WIDTH, settings.HEIGHT), flags=settings.FLAGS
)
surf = screen.copy()
assets.load_assets()
clock = pygame.time.Clock()
renderer = Renderer(screen)
current_scene = scenes.Gameplay()

world_map = load_map("assets/maps/map.json")

running = True
while running:
    clock.tick(settings.FPS)
    screen.fill("black")

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    for row, row_data in enumerate(world_map):
        for col, tile in enumerate(row_data):
            surf.blit(
                tile["image"], (col * settings.TILE_SIZE, row * settings.TILE_SIZE)
            )

    screen.blit(average_blur(surf, 15), (0, 0))

    pygame.display.flip()
