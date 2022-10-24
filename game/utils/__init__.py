import pygame
import cv2


def average_blur(surf: pygame.Surface, size: int):
    array = pygame.surfarray.array3d(surf)
    array[:, :, :] = cv2.blur(array, (size, size))  # NOQA
    return pygame.surfarray.make_surface(array)
