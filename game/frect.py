import pygame

from ._types import Position


class FRect:
    def __init__(self, x: float = 0, y: float = 0, width: float = 0, height: float = 0):
        self.x, self.y = x, y
        self.width, self.height = width, height

    def move(self, x_change, y_change):
        return FRect(self.x + x_change, self.y + y_change, self.width, self.height)

    def colliderect(self, other):
        return (
            self.x < other.x + other.width
            and self.x + self.width > other.x
            and self.y < other.y + other.height
            and self.y + self.height > other.y
        )

    @property
    def center(self):
        return self.x + self.width / 2, self.y + self.height / 2

    @center.setter
    def center(self, value: Position):
        x, y = value
        self.x = x - self.width / 2
        self.y = y - self.height / 2

    @property
    def topleft(self):
        return self.x, self.y

    @topleft.setter
    def topleft(self, value: Position):
        self.x, self.y = value

    @property
    def top(self):
        return self.y

    @property
    def bottom(self):
        return self.y + self.height

    @bottom.setter
    def bottom(self, y):
        self.y = y - self.height

    @property
    def centerx(self):
        return self.x + self.width / 2

    @property
    def centery(self):
        return self.y + self.height / 2

    def __str__(self):
        return f"<{self.__class__.__name__}({self.x, self.y, self.width, self.height})>"
