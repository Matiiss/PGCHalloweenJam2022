import math

import pygame

from . import entity, common, frect, settings, position
from .assets import assets


class Player(entity.Entity):
    def __init__(self, pos):
        super().__init__()

        self.pos = pygame.Vector2(pos)
        self.images = assets["images"]["scientist"]
        self.image = self.images["base"]
        self.rect = frect.FRect(*self.pos, *self.image.get_size())

        self.velocity = pygame.Vector2(0, 0)

    def update(self):
        dx, dy = 0, 0
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            dx += 1
        if keys[pygame.K_a]:
            dx -= 1
        if keys[pygame.K_SPACE]:
            self.velocity.y = -10

        self.velocity.x = dx
        vel = (
            self.velocity * common.actual_frames
            + 1 / 2 * settings.GRAVITY * common.actual_frames**2
        )
        new_pos = position.Position(self.rect.center + vel)
        cx, cy = new_pos.cx, new_pos.cy

        tiles = [
            pygame.Rect(
                cx * settings.TILE_SIZE,
                cy * settings.TILE_SIZE,
                settings.TILE_SIZE,
                settings.TILE_SIZE,
            )
            for cx, cy in (
                (cx - 1, cy - 1),
                (cx, cy - 1),
                (cx + 1, cy - 1),
                (cx + 1, cy),
                (cx + 1, cy + 1),
                (cx, cy + 1),
                (cx - 1, cy + 1),
                (cx - 1, cy),
            )
            if self.collides(cx, cy)
        ]
        # if not tiles:
        #     return

        horizontal_projection = self.rect.move(vel.x, 0)
        vertical_projection = self.rect.move(0, vel.y)

        for tile in tiles:
            if horizontal_projection.colliderect(tile):
                vel.x = 0
            if vertical_projection.colliderect(tile):
                if vel.y > 0:
                    bot = math.ceil(vertical_projection.bottom)
                    print(tile.y, bot, bot - tile.y)
                    vel.y = bot - tile.y
                    # if vel.y < 1:
                    #     vel.y = 0
                    print(vel)

        self.pos += vel
        self.velocity += settings.GRAVITY * common.actual_frames
        if self.velocity.y > 10:
            self.velocity.y = 10

        self.rect.topleft = self.pos

    # @functools.lru_cache(maxsize=512)
    def collides(self, cx: int, cy: int) -> bool:
        map_ = common.collision_map
        if 0 <= cy < len(map_) and 0 <= cx < len(map_[0]):
            return map_[cy][cx]
        return True
