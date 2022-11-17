import itertools

import pygame

from . import common, settings, scenes, assets, shader, player, group
from .renderer import Renderer
from .utils import clamp
from .utils.assets import load_map


pygame.init()

if settings.USE_SHADERS:
    screen = shader.ShaderDisplay(
        (settings.WIDTH, settings.HEIGHT), (1920, 1080), "vertex.vert", "fragment.frag"
    )
else:
    screen = pygame.display.set_mode(
        (settings.WIDTH, settings.HEIGHT), flags=settings.FLAGS
    )

common.overlay = pygame.Surface(
    (settings.WIDTH, settings.HEIGHT), flags=pygame.SRCALPHA
)

common.screen = screen

pygame.display.set_caption("DOOM")
assets.load_assets()
clock = pygame.time.Clock()
renderer = Renderer(screen)
current_scene = scenes.Gameplay()

world_map = load_map("assets/maps/map.json")
common.collision_map = list(
    list(data["collision"] for data in row) for row in world_map
)

x, y = 32, 32
fps_font = pygame.font.Font("assets/fonts/syne_mono/regular.ttf", 12)

_player = player.Player((settings.WIDTH / 2, settings.HEIGHT / 2))
_group = group.Group()
_group.add(_player)

running = True
while running:
    dt_ms = clock.tick(settings.FPS)
    common.delta_time = dt_ms / 1000
    common.delta_time = clamp(common.delta_time, 0.008, 0.042)
    screen.fill("#3c280d")

    events = pygame.event.get()
    common.events = events
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    _group.update()
    cam = (
        _player.rect.center
        - pygame.Vector2(settings.WIDTH, settings.HEIGHT) / 2
        - renderer.camera
    ) * 0.05
    renderer.camera += round(cam.x), round(cam.y)
    # renderer.camera.x, renderer.camera.y = clamp(
    #     renderer.camera.x, 0, len(world_map[0]) * settings.TILE_SIZE - settings.WIDTH
    # ), clamp(
    #     renderer.camera.y, 0, len(world_map) * settings.TILE_SIZE - settings.HEIGHT
    # )

    for row, row_data in enumerate(world_map):
        for col, tile in enumerate(row_data):
            renderer.render(
                tile["image"],
                (col * settings.TILE_SIZE, row * settings.TILE_SIZE),
            )

    # renderer.render(assets.assets["images"]["skeleton"]["base"], (x, y))
    # renderer.render(assets.assets["images"]["scientist"]["base"], (x, y + 32))

    _group.render()

    # pygame.draw.circle(screen, "red", (settings.WIDTH / 2, settings.HEIGHT / 2), 5)

    if settings.USE_SHADERS:
        screen.overlay.blit(
            fps_font.render(f"FPS:{clock.get_fps():.0f}", False, "black"), (0, 0)
        )
    else:
        screen.blit(fps_font.render(f"FPS:{clock.get_fps():.0f}", False, "black"), (0, 0))

    if settings.USE_SHADERS:
        screen.update()
    else:
        pygame.display.flip()
