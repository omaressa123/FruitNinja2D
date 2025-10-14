import pygame
import random
import os
from fruit import Fruit

class Bomb(Fruit):
    def __init__(self, x, y, speed_x, speed_y):
        """
        """
        super().__init__("bomb.png", x, y, speed_x, speed_y) # Assuming 'bomb.png' for bomb image
        self.explosion_frames = []
        for i in range(1, 6): # Assuming explosion_frame_1.png to explosion_frame_5.png
            self.explosion_frames.append(pygame.transform.scale(pygame.image.load(os.path.join("assets", f"explosion_frame_{i}.jpg")), (80, 80)))
        self.exploding = False
        self.explosion_index = 0
        self.explosion_timer = 0
        self.explosion_frame_duration = 5  # frames per explosion image

    def update(self):
        super().update() # Call parent's update for movement
        if self.exploding:
            self.update_explosion()

    def explode(self, sound):
        if not self.exploding:
            sound.play()
            self.exploding = True
            self.explosion_index = 0
            self.explosion_timer = 0

    def update_explosion(self):
        """
        Call this method every frame after explode() is triggered.
        Returns True if the explosion animation is finished, else False.
        """
        if self.exploding:
            self.explosion_timer += 1
            if self.explosion_timer >= self.explosion_frame_duration:
                self.explosion_timer = 0
                self.explosion_index += 1
                if self.explosion_index >= len(self.explosion_frames):
                    self.exploding = False
                    return True  # Animation finished
        return False

    def draw(self, screen):
        if self.exploding:
            if self.explosion_index < len(self.explosion_frames):
                frame = self.explosion_frames[self.explosion_index]
                rect = frame.get_rect(center=(self.x, self.y))
                screen.blit(frame, rect)
        else:
            if not self.sliced:
                screen.blit(self.image, self.rect)

    @staticmethod
    def spawn_random(screen_width, screen_height):
        x = random.randint(100, screen_width - 100)
        y = screen_height + 50
        speed_x = random.uniform(-4, 4)
        speed_y = random.uniform(-10, -6) # Slightly different speed for bombs
        return Bomb(x, y, speed_x, speed_y)
