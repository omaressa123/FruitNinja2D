import pygame

def draw_blade(screen, points):
    """Draws the slicing trail following the mouse."""
    if len(points) > 1:
        pygame.draw.lines(screen, (255, 255, 255), False, points, 3)

def play_slice_sound(sound):
    """Plays the slicing sound effect."""
    sound.play()
