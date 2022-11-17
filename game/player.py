import functools

import pygame

from . import entity, common, frect, settings, position, enums, animation, spritesheet
from .assets import assets


class Player(entity.Entity):
    def __init__(self, pos):
        super().__init__()

        self.pos = pygame.Vector2(pos)
        # self.images = assets["images"]["scientist"]
        # self.image = self.images["base"]
        sprite_sheet = spritesheet.AsepriteSpriteSheet(
            "assets/images/player/player.png"
        )
        self.animation = animation.Animation(sprite_sheet)
        self.image = sprite_sheet["idle"][0]["image"]
        self.pos_rect = frect.FRect(*self.pos, *self.image.get_size())
        self.rect = frect.FRect(*self.image.get_bounding_rect())

        self.velocity = pygame.Vector2(0, 0)
        self.x_vel = settings.PLAYER_X_VEL
        self.terminal_y = settings.PLAYER_Y_TERMINAL_VEL
        self.jump_power = settings.PLAYER_JUMP_POWER
        self.can_jump = False
        self.tiles = []

        self.state = enums.EntityState.IDLE
        self.flip_horizontal = False

    def update(self):
        dx, dy = 0, 0
        self.state = enums.EntityState.IDLE

        for event in common.events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and self.can_jump:
                    self.velocity.y = -self.jump_power

        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            dx += 1
            self.state = enums.EntityState.RUN
            self.flip_horizontal = False
        if keys[pygame.K_a]:
            dx -= 1
            self.state = enums.EntityState.RUN
            self.flip_horizontal = True

        self.velocity.x = dx * self.x_vel
        dx, dy = vel = (
            self.velocity * common.delta_time
            + 0.5 * settings.GRAVITY * common.delta_time**2
        )
        self.velocity += settings.GRAVITY * common.delta_time
        if self.velocity.y > self.terminal_y:
            self.velocity.y = self.terminal_y

        new_pos = position.Position(self.rect.center)
        cx, cy = new_pos.cx, new_pos.cy

        if vel.y < 0:
            self.state = enums.EntityState.JUMP

        self.tiles = [
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

        horizontal_projection = self.rect.move(vel.x, 0)
        vertical_projection = self.rect.move(0, vel.y)
        self.can_jump = False

        for tile in self.tiles:
            if horizontal_projection.colliderect(tile):
                vel.x = 0
            if vertical_projection.colliderect(tile):
                if dy >= 0:
                    self.can_jump = True
                    vel.y = tile.top - self.rect.bottom
                else:
                    self.state = enums.EntityState.JUMP
                    vel.y = tile.bottom - self.rect.top
                    self.velocity.y = 0

        self.pos += vel
        self.pos_rect.topleft = self.pos
        self.rect.center = self.pos_rect.center

        self.image = pygame.transform.flip(
            self.animation.update(self.state), self.flip_horizontal, False
        )

    @staticmethod
    @functools.lru_cache(maxsize=512)
    def collides(cx: int, cy: int) -> bool:
        map_ = common.collision_map
        if 0 <= cy < len(map_) and 0 <= cx < len(map_[0]):
            return map_[cy][cx]
        return True
