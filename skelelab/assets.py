import os

import pygame


assets = {}


def load_image(path):
    return pygame.image.load(
        os.path.join("assets/images", f"{path}.png")
    ).convert_alpha()


def load_assets():
    assets.update(
        {
            "images": {
                "skeleton": {
                    "base": load_image("skeleton/base"),
                    "walk": [
                        load_image(f"skeleton/walk/frame_{i}") for i in range(6 + 1)
                    ],
                },
                "scientist": {"base": load_image("scientist/base")},
            }
        }
    )
