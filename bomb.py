import pygame
from fruit import Fruit

class Bomb(Fruit):
    def __init__(self, image_path, explosion_images, x, y, speed_x, speed_y):
        """
        image_path: path to the bomb image
        explosion_images: list of paths to explosion animation frames
        """
        super().__init__(image_path, x, y, speed_x, speed_y)
        self.explosion_frames = [pygame.transform.scale(pygame.image.load(img), (80, 80)) for img in explosion_images]
        self.exploding = False
        self.explosion_index = 0
        self.explosion_timer = 0
        self.explosion_frame_duration = 5  # frames per explosion image

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
