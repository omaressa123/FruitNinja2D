import pygame
import random 
import sys
from fruit import Fruit
from bomb import Bomb
from effects import draw_blade, play_slice_sound

# Initialize pygame
pygame.init()
#screen pixels
WIDTH, HEIGHT = 800, 600 
#Create The Screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Fruit Ninja 2D")

# Load assets
background = pygame.image.load("#") # location path about background photo
slice_sound = pygame.mixer.Sound("#") # location path about silce voice or sound (.wav)
bomb_sound = pygame.mixer.Sound("#") #location path about bomb voice or sound

clock = pygame.time.Clock()
font = pygame.font.Font(None, 40)


# Game variables 
fruits = []
score = 0
lives = 3
blade_points = []
