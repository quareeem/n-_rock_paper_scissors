import pygame
import sys

from game_constants import SCREEN_WIDTH, SCREEN_HEIGHT, LIGHT_BROWN, BEIGE, DARK_BROWN
from game_utils import draw_title, draw_text

# def main_menu(music_on):
#     # ... (the content of main_menu() function remains the same)
#     return music_on


def main_menu(music_on, screen, font_menu):

    # Create menu buttons
    start_button = pygame.Rect(SCREEN_WIDTH // 2 - 80, SCREEN_HEIGHT // 3, 150, 50)
    music_button = pygame.Rect(SCREEN_WIDTH // 2 - 80, SCREEN_HEIGHT // 2, 150, 50)
    exit_button = pygame.Rect(SCREEN_WIDTH // 2 - 80, SCREEN_HEIGHT * 2 // 3, 150, 50)

    running = True
    while running:
        screen.fill(LIGHT_BROWN)
        draw_title(screen, "Rock Paper Scissors", 60, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 6)


        # Draw menu buttons
        pygame.draw.rect(screen, BEIGE, start_button)
        draw_text("Start", font_menu, DARK_BROWN, screen, start_button.x + 40, start_button.y + 10)
        pygame.draw.rect(screen, BEIGE, music_button)
        draw_text("Music: " + ("On" if music_on else "Off"), font_menu, DARK_BROWN, screen, music_button.x + 20, music_button.y + 10)
        pygame.draw.rect(screen, BEIGE, exit_button)
        draw_text("Exit", font_menu, DARK_BROWN, screen, exit_button.x + 50, exit_button.y + 10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if start_button.collidepoint(mouse_pos):
                    running = False
                elif music_button.collidepoint(mouse_pos):
                    music_on = not music_on
                elif exit_button.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()
    return music_on
