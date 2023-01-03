import itertools

import pygame

from . import spritesheet, enums


class Animation:
    def __init__(self, sprite_sheet: spritesheet.AsepriteSpriteSheet):
        self._sprites = {}
        members = enums.EntityState.__members__

        for key, value in sprite_sheet.data.items():
            self._sprites[members[key.upper()]] = itertools.cycle(value)

        self._sprite = {"duration": 0}
        self.image = None
        self.state = members["IDLE"]
        self._last_time = 0

    def update(self, state=None) -> pygame.Surface:
        # if state is not None:
        #     self.state = state

        current_time = pygame.time.get_ticks()
        if current_time - self._last_time >= self._sprite["duration"] or (
            state is not None and state != self.state
        ):
            self.state = state
            self._sprite = next(self._sprites[self.state])
            self.image = self._sprite["image"]
            self._last_time = current_time

        return self.image
