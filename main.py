import pygame
import random
import sys
import os 
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
background = pygame.image.load(os.path.join("assets", "images.jpeg")) 
slice_sound = pygame.mixer.Sound(os.path.join("assets", "slice.wav")) 
#bomb_sound = pygame.mixer.Sound(os.path.join("assets", "bomb.wav")) 
background_music = pygame.mixer.Sound(os.path.join("assets", "audio BE 20251014015520.wav"))

clock = pygame.time.Clock()
font = pygame.font.Font(None, 40)

# Game variables
fruits = []
bombs = [] # Initialize bombs list
score = 0
lives = 3
blade_points = []
game_over = False

# Game states
START_SCREEN = 0
GAME_PLAY = 1
GAME_OVER = 2
current_game_state = START_SCREEN

def start_screen():
    screen.fill((0, 0, 0)) # Black background
    title_text = font.render("Fruit Ninja 2D", True, (255, 255, 255))
    instruction_text = font.render("Press SPACE to Start", True, (255, 255, 255))
    screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 3))
    screen.blit(instruction_text, (WIDTH // 2 - instruction_text.get_width() // 2, HEIGHT // 2))
    pygame.display.flip()

def game_over_screen():
    screen.fill((0, 0, 0)) # Black background
    game_over_text = font.render(f"Game Over! Score: {score}", True, (255, 255, 255))
    restart_text = font.render("Press SPACE to Restart or ESC to Quit", True, (255, 255, 255))
    screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 3))
    screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2))
    pygame.display.flip()

background_music.play(-1)  # Play background music indefinitely
# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if current_game_state == START_SCREEN and event.key == pygame.K_SPACE:
                current_game_state = GAME_PLAY
                score = 0
                lives = 3
                fruits = []
                bombs = []
            elif current_game_state == GAME_OVER and event.key == pygame.K_SPACE:
                current_game_state = GAME_PLAY
                score = 0
                lives = 3
                fruits = []
                bombs = []
                game_over = False
            elif event.key == pygame.K_ESCAPE:
                running = False

    if current_game_state == START_SCREEN:
        start_screen()
    elif current_game_state == GAME_PLAY:
        screen.blit(background, (0, 0))

        # Spawn fruits and bombs (temporary, will be moved to a function later)
        if random.randint(0, 100) < 5: # Adjust spawn rate
            fruits.append(Fruit.spawn_random(WIDTH, HEIGHT)) # Call spawn_random without image_path
        if random.randint(0, 200) < 2: # Adjust bomb spawn rate
            bombs.append(Bomb.spawn_random(WIDTH, HEIGHT))

        # Update and draw fruits
        for fruit in fruits[:]:
            fruit.update()
            fruit.draw(screen)
            if fruit.y > HEIGHT: # If the fruit falls off the screen
                lives -= 1
                fruits.remove(fruit)
                if lives <= 0:
                    current_game_state = GAME_OVER

        # Update and draw bombs
        for bomb in bombs[:]:
            bomb.update()
            bomb.draw(screen)
            if bomb.y > HEIGHT: # Remove bomb if it falls off screen
                bombs.remove(bomb)

        # Blade drawing and slicing
        if pygame.mouse.get_pressed()[0]: # Left mouse button
            blade_points.append(pygame.mouse.get_pos())
            if len(blade_points) > 10: # Keep blade trail short
                blade_points.pop(0)
        else:
            blade_points = [] # Clear blade if mouse not pressed

        draw_blade(screen, blade_points)

        # Slicing detection and scoring (moved from top level)
        for fruit in fruits[:]:
            if fruit.check_slice(blade_points):
                score += 10
                play_slice_sound(slice_sound)
                fruits.remove(fruit) # Remove sliced fruit

        for bomb in bombs[:]:
            if bomb.check_slice(blade_points):
                bomb_sound.play() # Play bomb sound on hit
                current_game_state = GAME_OVER
                game_over = True # Set game_over flag

        # Display score and lives
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        lives_text = font.render(f"Lives: {lives}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        screen.blit(lives_text, (WIDTH - lives_text.get_width() - 10, 10))

        pygame.display.flip()

    elif current_game_state == GAME_OVER:
        game_over_screen()

    clock.tick(60)

pygame.quit()
sys.exit()

