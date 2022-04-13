import math

import pygame.draw
from pygame import mixer

from helpers_and_functions.function_helpers import *
from helpers_and_functions.Buttons import *
from games.cups import Cups
from games.dino import Dino
from games.snake import Snake
from games.millioner import Millioner
from highs import display_high_scores
from information import  display_information

pygame.init()
mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
buttons_position = []
buttons_list = []

add_image(screen, "images/menu_images/background.png", 0, 0, WIDTH, HEIGHT, None)
running = True
chose = -1
mixer.music.load("music/hub_music/Super Mario Party OST - Main Theme.wav")
mixer.music.play(-1)
while running:
    add_image(screen, "images/menu_images/background.png", 0, 0, WIDTH, HEIGHT, None)
    add_image(screen, "images/menu_images/title2.jpg", MAIN_TITLE_X, MAIN_TITLE_Y, MAIN_TITLE_WIDTH, MAIN_TITLE_HEIGHT,(0,0,0))
    for i in range(len(angles)):
        if i == 4 or i == 5:
            color = (235, 183, 52)
            color2 = (191, 143, 21)
        else:
            color = (51, 255, 221)
            color2 = (72, 119, 111)
        angle = 270 - angles[i]
        horizontal = math.sin(math.radians(angle)) * RADIUS * 2
        vertical = math.cos(math.radians(angle)) * RADIUS * 2

        cords = pygame.mouse.get_pos()
        if CENTER[0] + horizontal - SMALL_RADIUS * 2 < cords[0] < CENTER[0] + horizontal + SMALL_RADIUS * 2 and CENTER[1]\
                + vertical - SMALL_RADIUS * 2 < cords[1] < CENTER[1] + vertical + SMALL_RADIUS * 2:
            pygame.draw.circle(screen, color, (CENTER[0] + horizontal, CENTER[1] + vertical), SMALL_RADIUS * 3,
                               0)
            pygame.draw.circle(screen, color2, (CENTER[0] + horizontal, CENTER[1] + vertical), SMALL_RADIUS * 3,
                               3)
            if images[i] != "":
                add_image(screen, images[i], CENTER[0] + horizontal - round(IMAGE_RADIUS * 1.5),
                          CENTER[1] + vertical - round(IMAGE_RADIUS * 1.5), IMAGE_RADIUS * 3, IMAGE_RADIUS * 3, WHITE)

            display_text_menu(screen, TEXT_X, TEXT_Y, game_text[i])
        else:
            pygame.draw.circle(screen, color, (CENTER[0] + horizontal, CENTER[1] + vertical), SMALL_RADIUS * 2,
                               0)
            pygame.draw.circle(screen, color2, (CENTER[0] + horizontal, CENTER[1] + vertical), SMALL_RADIUS * 2,
                               3)
            if images[i] != "":
                add_image(screen, images[i], CENTER[0] + horizontal - IMAGE_RADIUS, CENTER[1] + vertical - IMAGE_RADIUS,
                          IMAGE_RADIUS * 2, IMAGE_RADIUS * 2, WHITE)
        buttons_position.append((CENTER[0] + horizontal - 2 * SMALL_RADIUS, CENTER[1] + vertical - 2 * SMALL_RADIUS))

    for pos in buttons_position:
        button = Button(pos[0], pos[1], 4 * SMALL_RADIUS, 4 * SMALL_RADIUS)
        #pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(pos[0], pos[1], 4 * SMALL_RADIUS, 4 * SMALL_RADIUS))
        buttons_list.append(button)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for i in range(len(buttons_list)):
                if mouse_in_button(buttons_list[i], pos):
                    chose = i
                    break

    if chose == 0:
        mixer.music.pause()
        game = Cups(screen)
        game.home_screen()
        mixer.music.load("music/hub_music/Super Mario Party OST - Main Theme.wav")
        mixer.music.play(-1)
        chose = -1
    if chose == 1:
        mixer.music.pause()
        game = Dino(screen)
        game.home_screen()
        mixer.music.load("music/hub_music/Super Mario Party OST - Main Theme.wav")
        mixer.music.play(-1)
        chose = -1
    if chose == 2:
        mixer.music.pause()
        game = Snake(screen)
        game.start_menu()
        mixer.music.load("music/hub_music/Super Mario Party OST - Main Theme.wav")
        mixer.music.play(-1)
        chose = -1
    if chose == 3:
        mixer.music.pause()
        game = Millioner(screen)
        mixer.music.load("music/hub_music/Super Mario Party OST - Main Theme.wav")
        mixer.music.play(-1)
        chose = -1
    if chose == 4:
        f = open("games/game_files/high_milioner", "r")
        line = f.readlines()
        millionaire = line[-1]
        f = open("games/game_files/high_dino", "r")
        line = f.readlines()
        dinosaur = line[-1]
        f = open("games/game_files/high_cups", "r")
        line = f.readlines()
        cups = line[-1]
        f = open("games/game_files/high_snake.txt", "r")
        line = f.readlines()
        snake = line[-1]
        score_list = [["cups", cups],["dinosaur",dinosaur],["snake",snake],["millionaire",millionaire]]
        display_high_scores(score_list)
    if chose == 5:
        display_information(screen)
    pygame.display.update()
pygame.quit()
