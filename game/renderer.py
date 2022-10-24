import pygame

from . import types


class Renderer:
    def __init__(self, base):
        self.base = base

    def render(self, surf: pygame.Surface, pos: types.Position, dest: pygame.Surface = None):
        if dest is None:
            dest = self.base

        dest.blit(surf, pos)
