import pygame

from . import types


class Renderer:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, base=None):
        self.base = base
        self.camera = pygame.Vector2(0, 0)

    def render(self, surf: pygame.Surface, pos: types.Position, dest: pygame.Surface = None):
        if dest is None:
            dest = self.base or pygame.display.get_surface()

        if self.camera is None:
            dest.blit(surf, pos)

        elif self.camera is not None:
            if isinstance(pos, pygame.Rect):
                pos = pos.topleft
            dest.blit(surf, pos - self.camera)

    @classmethod
    def get_renderer(cls):
        return cls._instance

