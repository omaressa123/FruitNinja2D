import pygame
from fruit import Fruit

class Bomb(Fruit):
    def __init__(self, image_path, x, y, speed_x, speed_y):
        super().__init__(image_path, x, y, speed_x, speed_y)

    def explode(self, sound):
        sound.play()
