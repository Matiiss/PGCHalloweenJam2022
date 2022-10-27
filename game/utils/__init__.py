import pygame
import cv2
import numpy


def average_blur(surf: pygame.Surface, size: int, dest=None) -> pygame.Surface | None:
    array = numpy.zeros((*surf.get_size(), 4), "int")
    array[:, :, :3] = pygame.surfarray.pixels3d(surf)
    array[:, :, 3] = pygame.surfarray.pixels_alpha(surf)
    array = cv2.blur(array, (size, size))  # NOQA
    surf = pygame.surfarray.make_surface(array[:, :, :3]).convert_alpha()
    pygame.surfarray.pixels_alpha(surf)[:] = array[:, :, 3]
    return surf


def cut_circle(surf, radius, pos=None):
    surf = surf.convert_alpha()
    alpha_mask = surf.copy()
    pygame.draw.circle(alpha_mask, (255, 255, 255, 0), pos or pygame.Vector2(surf.get_size()) / 2, radius)
    pygame.surfarray.pixels_alpha(surf)[:] = pygame.surfarray.pixels_alpha(alpha_mask)
    return surf


def clamp(value: float, min_: float, max_: float) -> float:
    return max(min_, min(value, max_))
