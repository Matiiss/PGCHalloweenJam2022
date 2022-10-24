from . import renderer


class Group:
    def __init__(self):
        self.entities = {}

    def add(self, entity):
        self.entities[entity] = 0
        entity.groups.append(self)

    def update(self, *args, **kwargs):
        for entity in self.entities:
            entity.update(*args, **kwargs)

    def render(self, dest):
        for entity in self.entities:
            renderer.render(entity.image, entity.pos, dest)
