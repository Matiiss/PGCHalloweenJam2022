import itertools

import pygame

from . import common, settings, scenes, assets, shader, player, group
from .renderer import Renderer
from .utils import clamp
from .utils.assets import load_map


pygame.init()

# screen = shader.ShaderDisplay(
#     (settings.WIDTH, settings.HEIGHT), (1920, 1080), "vertex.vert", "fragment.frag"
# )
screen = pygame.display.set_mode(
    (settings.WIDTH, settings.HEIGHT), flags=settings.FLAGS
)
# surf = screen.copy()
pygame.display.set_caption("DOOM")
assets.load_assets()
clock = pygame.time.Clock()
renderer = Renderer(screen)
current_scene = scenes.Gameplay()

world_map = load_map("assets/maps/map.json")
common.collision_map = list(list(data["collision"] for data in row) for row in world_map)

x, y = 32, 32
fps_font = pygame.font.Font("assets/fonts/syne_mono/regular.ttf", 12)

_player = player.Player((settings.WIDTH / 2, settings.HEIGHT / 2))
_group = group.Group()
_group.add(_player)

running = True
while running:
    common.delta_time = clock.tick(settings.FPS)
    common.actual_frames = clamp(
        common.delta_time / settings.ACTUAL_FRAME_COEFFICIENT,
        min_=settings.ACTUAL_FRAME_MIN,
        max_=settings.ACTUAL_FRAME_MAX,
    )
    screen.fill("black")

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    _group.update()
    cam = pygame.Vector2(settings.WIDTH, settings.HEIGHT) / 2 - _player.rect.center
    renderer.camera = cam

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

    # screen.overlay.blit(
    #     fps_font.render(f"FPS:{clock.get_fps():.0f}", False, "black"), (0, 0)
    # )

    pygame.display.flip()
    # screen.update()
