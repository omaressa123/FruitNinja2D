import pygame
import random
import sys
import os 
from fruit import Fruit
from bomb import Bomb
from effects import draw_blade, play_slice_sound
from sliced_fruit import SlicedFruit

# Initialize pygame
pygame.init()
#screen pixels
WIDTH, HEIGHT = 800, 600 
#Create The Screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Fruit Ninja 2D")

# Load assets
background = pygame.image.load(os.path.join("assets", "images.jpeg"))
background = pygame.transform.scale(background, (WIDTH, HEIGHT)) # Scale background to screen size
slice_sound = pygame.mixer.Sound(os.path.join("assets", "slice.wav")) 
bomb_sound = pygame.mixer.Sound(os.path.join("assets", "bomb.wav")) 
background_music = pygame.mixer.Sound(os.path.join("assets", "background_music.wav"))

clock = pygame.time.Clock()
font = pygame.font.Font(None, 40)

# Game variables
fruits = []
bombs = [] # Initialize bombs list
score = 0
lives = 3
blade_points = []
sliced_fruits = [] # Initialize sliced_fruits list

# Game mechanics variables
max_fruits = 3
spawn_interval = 2.0  # seconds
spawn_timer = 0
last_score_check = 0

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

def spawn_items():
    global spawn_timer
    spawn_timer += clock.get_time() / 1000.0  # Time in seconds
    if spawn_timer >= spawn_interval and len(fruits) + len(bombs) < max_fruits:
        if random.randint(0, 100) < 70:  # Higher chance to spawn fruit
            fruits.append(Fruit.spawn_random(WIDTH, HEIGHT))
        elif random.randint(0, 100) < 10:  # Lower chance to spawn bomb
            bombs.append(Bomb.spawn_random(WIDTH, HEIGHT))
        spawn_timer = 0

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
                max_fruits = 3
                spawn_interval = 2.0
                spawn_timer = 0
                last_score_check = 0
                sliced_fruits = []
            elif current_game_state == GAME_OVER and event.key == pygame.K_SPACE:
                current_game_state = GAME_PLAY
                score = 0
                lives = 3
                fruits = []
                bombs = []
                max_fruits = 3
                spawn_interval = 2.0
                spawn_timer = 0
                last_score_check = 0
                sliced_fruits = []
            elif event.key == pygame.K_ESCAPE:
                running = False

    if current_game_state == START_SCREEN:
        start_screen()
    elif current_game_state == GAME_PLAY:
        screen.blit(background, (0, 0))

        spawn_items()  # Call the new function to spawn fruits and bombs

        # Update and draw fruits
        for fruit in fruits[:]:
            fruit.update()
            fruit.draw(screen)
            if fruit.y > HEIGHT:  # If the fruit falls off the screen
                lives -= 1
                fruits.remove(fruit)
                if lives <= 0:
                    current_game_state = GAME_OVER

        # Update and draw bombs
        for bomb in bombs[:]:
            bomb.update()
            bomb.draw(screen)
            if bomb.y > HEIGHT:  # Remove bomb if it falls off screen
                bombs.remove(bomb)

        # Blade drawing and slicing
        if pygame.mouse.get_pressed()[0]:  # Left mouse button
            blade_points.append(pygame.mouse.get_pos())
            if len(blade_points) > 10:  # Keep blade trail short
                blade_points.pop(0)
        else:
            blade_points = []  # Clear blade if mouse not pressed

        draw_blade(screen, blade_points)

        # Slicing detection and scoring
        for fruit in fruits[:]:
            if fruit.check_slice(blade_points):
                score += 10
                play_slice_sound(slice_sound)
                # Instead of removing the fruit, create sliced halves
                left_half, right_half = fruit.slice()
                sliced_fruits.append(left_half)
                sliced_fruits.append(right_half)
                fruits.remove(fruit) # Remove sliced fruit immediately after creating halves

        for bomb in bombs[:]:
            if bomb.check_slice(blade_points):
                bomb.explode(bomb_sound)  # Call explode method
                current_game_state = GAME_OVER

        # Update and draw sliced fruits
        for s_fruit in sliced_fruits[:]:
            s_fruit.update()
            s_fruit.draw(screen)
            if s_fruit.y > HEIGHT:  # Remove sliced fruit if it falls off the screen
                sliced_fruits.remove(s_fruit)

        # Score-based difficulty adjustment
        if score > last_score_check:
            max_fruits += 3
            spawn_interval = max(1.0, spawn_interval - 0.2) # Minimum 1 second interval
            last_score_check = score

        # Display score and lives
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        lives_text = font.render(f"Lives: {lives}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        screen.blit(lives_text, (WIDTH - lives_text.get_width() - 10, 10))

    elif current_game_state == GAME_OVER:
        game_over_screen()

    pygame.display.flip()  # Update the full display Surface to the screen
    clock.tick(60)

pygame.quit()
sys.exit()

