import pygame
import os

class SlicedFruit:
    def __init__(self, image, x, y, speed_x, speed_y):
        self.image = image # Directly use the passed image (pygame.Surface)
        self.image = pygame.transform.scale(self.image, (35, 70)) # Halved width
        self.x = x
        self.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.gravity = 0.4
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.speed_y += self.gravity
        self.rect.center = (self.x, self.y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
