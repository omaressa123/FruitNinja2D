import pygame
import random

#Slicing Trail Effect 
def draw_blade(screen, points):
    """Draws the slicing trail following the mouse."""
    if len(points) > 1:
        pygame.draw.lines(screen, (255, 255, 255), False, points, 3)

# Slicing Sound Effect 
def play_slice_sound(sound):
    """Plays the slicing sound effect."""
    sound.play()

# Particle Animation for Slicing 
class SliceParticle:
    def __init__(self, pos, color=(255,255,255)):
        self.x, self.y = pos
        self.radius = random.randint(2, 5)
        self.color = color
        self.life = random.randint(10, 20)
        self.vx = random.uniform(-2, 2)
        self.vy = random.uniform(-2, -0.5)

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.vy += 0.15  # gravity
        self.life -= 1

    def draw(self, screen):
        if self.life > 0:
            pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

def spawn_slice_particles(pos, count=8, color=(255,255,255)):
    """Creates a list of SliceParticle objects at the given position."""
    return [SliceParticle(pos, color) for _ in range(count)]
