import pygame

class Fruit:
    def __init__(self, image_path, x, y, speed_x, speed_y):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.x = x
        self.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.gravity = 0.4
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def move(self):
        """Move fruit with gravity."""
        self.x += self.speed_x
        self.y += self.speed_y
        self.speed_y += self.gravity
        self.rect.center = (self.x, self.y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
