import pygame
import random

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
        self.sliced = False

    def move(self):
        """Move fruit with gravity."""
        self.x += self.speed_x
        self.y += self.speed_y
        self.speed_y += self.gravity
        self.rect.center = (self.x, self.y)

    def draw(self, screen):
        if not self.sliced:
            screen.blit(self.image, self.rect)

    def check_sliced(self, blade_points):
        """
        Check if the fruit has been sliced by the blade.
        blade_points: list of (x, y) tuples representing the blade's path.
        Returns True if sliced, False otherwise.
        """
        if self.sliced:
            return False
        for point in blade_points:
            if self.rect.collidepoint(point):
                self.sliced = True
                return True
        return False

    @staticmethod
    def spawn_random(image_path, screen_width, screen_height):
        """
        Spawn a fruit at a random position at the bottom of the screen
        with a random upward velocity and random horizontal speed.
        """
        x = random.randint(100, screen_width - 100)
        y = screen_height + 50
        speed_x = random.uniform(-4, 4)
        speed_y = random.uniform(-12, -8)
        return Fruit(image_path, x, y, speed_x, speed_y)

