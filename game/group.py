from . import renderer, entity as ent


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
            self._renderer.render(entity.image, entity.pos, dest)
