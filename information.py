import pygame
from helpers_and_functions.function_helpers import  add_image
from helpers_and_functions.constants_files.constants_menu import WIDTH, HEIGHT
pygame.init()
def display_information(screen):
    screen.fill((255,255,255))
    pygame.display.flip()
    add_image(screen, "images/info_images/board.png", 0,0, WIDTH, HEIGHT, (255,255,255))

