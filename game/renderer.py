import pygame

from . import types


class Renderer:
    def __init__(self, base=None):
        self.base = base
        self.camera = None

    def render(self, surf: pygame.Surface, pos: types.Position, dest: pygame.Surface = None):
        if dest is None:
            dest = self.base or pygame.display.get_surface()

        if self.camera is None:
            dest.blit(surf, pos)

        elif self.camera is not None:
            if isinstance(pos, pygame.Rect):
                pos = pos.topleft
            dest.blit(surf, self.camera + pos)
