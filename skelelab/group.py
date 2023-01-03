import pygame

from . import renderer, entity as ent, settings


class Group:
    def __init__(self):
        self._renderer = renderer.Renderer.get_renderer()
        self.entities = {}

    def add(self, entity: ent.Entity):
        self.entities[entity] = 0
        entity.groups.append(self)

    def update(self, *args, **kwargs):
        for entity in self.entities:
            entity.update(*args, **kwargs)

    def render(self, dest=None):
        for entity in self.entities:
            if hasattr(entity, "tiles") and settings.DEBUG:
                for rect in entity.tiles:
                    img = pygame.Surface((rect.width, rect.height), flags=pygame.SRCALPHA)
                    img.fill("red")
                    self._renderer.render(img, rect)
            self._renderer.render(entity.image, entity.pos, dest)
