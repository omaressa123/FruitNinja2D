import pygame
import random
import os
from sliced_fruit import SlicedFruit

class Fruit:
    def __init__(self, image_path, x, y, speed_x, speed_y):
        self.image = pygame.image.load(os.path.join("assets", image_path)) # Use os.path.join
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.x = x
        self.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.gravity = 0.4
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.sliced = False
        self.fruit_type = image_path.split('.')[0] # e.g., "apple", "banana"

    def update(self):
        """Move fruit with gravity."""
        self.x += self.speed_x
        self.y += self.speed_y
        self.speed_y += self.gravity
        self.rect.center = (self.x, self.y)

    def draw(self, screen):
        if not self.sliced:
            screen.blit(self.image, self.rect)

    def slice(self):
        # Create two half-fruits
        half_width = self.image.get_width() // 2
        half_height = self.image.get_height()

        # Create left half
        left_half_image = self.image.subsurface((0, 0, half_width, half_height))
        # Create right half - flip it to simulate a clean cut
        right_half_image = self.image.subsurface((half_width, 0, half_width, half_height))

        # Determine initial speeds for the sliced halves
        # They should diverge from the original fruit's trajectory
        speed_x_left = self.speed_x - random.uniform(2, 4)
        speed_x_right = self.speed_x + random.uniform(2, 4)
        speed_y_halves = self.speed_y - random.uniform(2, 4) # Give an upward thrust

        # Create SlicedFruit objects
        sliced_left = SlicedFruit(left_half_image, self.x - half_width // 2, self.y, speed_x_left, speed_y_halves)
        sliced_right = SlicedFruit(right_half_image, self.x + half_width // 2, self.y, speed_x_right, speed_y_halves)

        return sliced_left, sliced_right

    def check_slice(self, blade_points):
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
    def spawn_random(screen_width, screen_height):
        fruit_images = ["apple.png", "banana.png", "sandia.png"] # Example fruit images
        chosen_image = random.choice(fruit_images)
        x = random.randint(100, screen_width - 100)
        y = screen_height - 20  # Start slightly above the bottom
        speed_x = random.uniform(-4, 4)
        speed_y = random.uniform(-14, -10) # Increased upward speed
        return Fruit(chosen_image, x, y, speed_x, speed_y)

