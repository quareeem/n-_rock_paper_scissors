import pygame
import random
import sys
import os

from game_constants import ROCK, PAPER, SCISSORS, SCREEN_WIDTH, SCREEN_HEIGHT, LIGHT_BROWN, BEIGE
from game_objects import Object
from game_menu import main_menu
from game_utils import draw_text

# Initialize Pygame
pygame.mixer.init()
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Rock Paper Scissors")

# Load images
rock_image = pygame.transform.scale(pygame.image.load(os.path.join('images', 'rock.png')).convert_alpha(), (20, 20))
paper_image = pygame.transform.scale(pygame.image.load(os.path.join('images', 'paper.png')).convert_alpha(), (20, 20))
scissors_image = pygame.transform.scale(pygame.image.load(os.path.join('images', 'scissors.png')).convert_alpha(), (20, 20))

# Set up the font
font = pygame.font.SysFont(None, 48)
font_menu = pygame.font.SysFont(None, 36)

# Create objects
objects = []

music_on = True
music_on = main_menu(music_on, screen, font_menu)

# Load and play music
pygame.mixer.music.load('music.mp3')
if music_on:
    pygame.mixer.music.play(-1)

# Initialize Red objects
for i in range(random.randint(10, 20)):
    x = random.randint(0, SCREEN_WIDTH//3)
    y = random.randint(0, SCREEN_HEIGHT//4)
    obj = Object(x, y, ROCK)
    objects.append(obj)

# Initialize Green objects
for i in range(random.randint(10, 20)):
    x = random.randint(SCREEN_WIDTH * 0.3, 2*SCREEN_WIDTH//3)
    y = random.randint(SCREEN_HEIGHT * 0.8, SCREEN_HEIGHT)
    obj = Object(x, y, PAPER)
    objects.append(obj)

# Initialize Blue objects
for i in range(random.randint(10, 20)):
    x = random.randint(2*SCREEN_WIDTH//3, SCREEN_WIDTH)
    y = random.randint(0, SCREEN_HEIGHT//4)
    obj = Object(x, y, SCISSORS)
    objects.append(obj)

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Toggle music on/off with the M key
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m:
                music_on = not music_on
                if music_on:
                    pygame.mixer.music.unpause()
                else:
                    pygame.mixer.music.pause()

    # Reset collided_this_frame for all objects
    for obj in objects:
        obj.collided_this_frame = False

    # Move objects
    for obj in objects:
        obj.move(objects, screen)

    screen.fill(BEIGE)
    for obj in objects:
        if obj.obj_type == ROCK:
            image = rock_image
        elif obj.obj_type == PAPER:
            image = paper_image
        elif obj.obj_type == SCISSORS:
            image = scissors_image
        rect = image.get_rect()
        rect.center = (obj.x, obj.y)
        screen.blit(image, rect)

    # Update the display
    pygame.display.flip()

    # Wait for a short time to control the frame rate
    pygame.time.wait(50)

pygame.quit()
