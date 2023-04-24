import pygame

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, 1, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)

def draw_title(surface, title, font_size, x, y, color=(255, 255, 255)):
    title_font = pygame.font.SysFont(None, font_size)
    title_text = title_font.render(title, 1, color)
    title_rect = title_text.get_rect()
    title_rect.center = (x, y)
    surface.blit(title_text, title_rect)