import pygame
from helpers_and_functions.constants_files.constants_menu import *


def display_text_menu(screen, x, y, text):
    font = pygame.font.SysFont('impact', round(WIDTH / 40) + round(HEIGHT / 40))
    text = font.render(text, True, (255, 255, 255))
    textRect = text.get_rect()
    textRect.center = (x, y)
    screen.blit(text, textRect)


def add_image(screen, img_path, x_pos, y_pos, width, height, background):
    if background is not None:
        # Add the image to the screen
        img = pygame.image.load(img_path)
        img.set_colorkey(background)
        img = pygame.transform.scale(img, (width, height))
        screen.blit(img, (x_pos, y_pos))
    else:
        # Add the image to the screen
        img = pygame.image.load(img_path)
        img = pygame.transform.scale(img, (width, height))
        screen.blit(img, (x_pos, y_pos))


def mouse_in_button(button, mouse_pos):
    """
    The function get button and mouse press position on screen and return True
    if mouse click on button
    :param button: Button object
        button on screen
    :param mouse_pos: tuple
        the x and y position of the mouse cursor
    :return: boolean
        True if mouse click on button, else False
    """
    if button.width > mouse_pos[0] > button.x_pos and \
            button.y_pos < mouse_pos[1] < button.height:
        return True
    return False


def display_text(screen, x, y, text):
    font = pygame.font.SysFont('bahnschrift', round(WIDTH / 70) + round(HEIGHT / 70))
    text = font.render(text, True, (255, 255, 255))
    textRect = text.get_rect()
    textRect.center = (x, y)
    screen.blit(text, textRect)
