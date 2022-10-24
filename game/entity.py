class Entity:
    def __init__(self, *args, **kwargs):
        self.groups = []

    def update(self, *args, **kwargs):
        pass

    def kill(self):
        for group in self.groups:
            del group.sprites[self]
