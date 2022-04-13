import pygame
from helpers_and_functions.constants_files.constants_menu import *
from helpers_and_functions.function_helpers import *

def display_text_high(screen, x, y, text):
    font = pygame.font.SysFont('bahnschrift', round(WIDTH / 30) + round(HEIGHT / 30))
    text = font.render(text, True, (0, 0, 0))
    textRect = text.get_rect()
    textRect.topleft = (x, y)
    screen.blit(text, textRect)


def display_high_scores(score_list):
    score_list.insert(0,["GAME", "SCORE"])
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    add_image(screen,"images/scores.jpg",0,0,WIDTH,HEIGHT,None)
    for i in range(len(score_list)):
        for j in range(len(score_list[i])):
            display_text_high(screen, SCORE_WIDTH*j+SCORE_X, SCORE_HEIGHT*i+SCORE_Y,str(score_list[i][j]))
            if j != 0:
                pygame.draw.line(screen,(0,0,0),(SCORE_WIDTH*j+SCORE_X - 20, SCORE_Y),(SCORE_WIDTH*j+SCORE_X - 20, HEIGHT-SCORE_Y),2)
        if i != 0:
            pygame.draw.line(screen, (0, 0, 0), (SCORE_X, SCORE_HEIGHT * i + SCORE_Y - 20),( WIDTH - SCORE_X, SCORE_HEIGHT * i + SCORE_Y - 20), 2)

