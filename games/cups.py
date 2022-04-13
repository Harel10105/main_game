import random
import time

from pygame import mixer

from helpers_and_functions.function_helpers import *
from helpers_and_functions.buttons_to_use.buttons_to_use_cups import *


class Cups:
    def __init__(self, screen):
        pygame.init()
        mixer.init()
        self.screen = screen
        self.screen.fill(BACKGROUND_COLOR)
        self.current_y_cup = CUP_Y
        self.ball_pos = 0
        self.finish_movement = True
        self.finish_switches = False
        self.switch_counter = 0
        self.first_cup_x = FIRST_CUP_START_X
        self.second_cup_x = SECOND_CUP_START_X
        self.third_cup_x = THIRD_CUP_START_X
        self.posList = [self.first_cup_x, self.second_cup_x, self.third_cup_x]
        self.posList2 = [FIRST_CUP_START_X, SECOND_CUP_START_X, THIRD_CUP_START_X]
        self.from_point = 0
        self.to_point = 0
        self.choose = -1
        self.finish_animation = False
        self.level = 10
        self.playlist = ["music/cups_music/Botanic Panic.wav", "music/cups_music/Carnival Kerfuffle.wav",
                         "music/cups_music/Cuphead OST - Floral Fury [Music].wav",
                         "music/cups_music/Cuphead OST - Hurry Up [Music].wav",
                         "music/cups_music/One Hell of a Time.wav"]

    def home_screen(self):
        fin = False
        while not fin:
            self.screen.fill(BACKGROUND_COLOR)
            add_image(self.screen, "images/cups_images/start_button.png.crdownload", START_BUTTON_X, START_BUTTON_Y,
                      START_BUTTON_WIDTH, START_BUTTON_HEIGHT, None)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    fin = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if mouse_in_button(start_button, pos):
                        self.game_screen()
                        self.__init_game()
                        self.level = 10
            pygame.display.flip()

    def __init_game(self):
        self.current_y_cup = CUP_Y
        self.ball_pos = random.randint(1, 3)
        self.finish_movement = True
        self.switch_counter = 0
        self.first_cup_x = FIRST_CUP_START_X
        self.second_cup_x = SECOND_CUP_START_X
        self.third_cup_x = THIRD_CUP_START_X
        self.posList = [self.first_cup_x, self.second_cup_x, self.third_cup_x]
        self.posList2 = [FIRST_CUP_START_X, SECOND_CUP_START_X, THIRD_CUP_START_X]
        self.finish_switches = False
        self.from_point = 0
        self.to_point = 0
        self.choose = -1
        self.finish_animation = False

    def __go_to(self, from_point, to_point):
        finish = 0
        if self.posList[self.from_point - 1] < self.posList2[self.to_point - 1]:
            if self.posList[from_point - 1] < self.posList2[to_point - 1] - self.level:
                self.posList[from_point - 1] += self.level
                print(self.posList)
            else:
                finish += 1

            if self.posList[to_point - 1] > self.posList2[from_point - 1] + self.level:
                self.posList[to_point - 1] -= self.level
            else:
                finish += 1
        else:
            if self.posList[from_point - 1] > self.posList2[to_point - 1] + self.level:
                self.posList[from_point - 1] -= self.level
                print(self.posList)
            else:
                finish += 1
            if self.posList[to_point - 1] < self.posList2[from_point - 1] - self.level:
                self.posList[to_point - 1] += self.level
            else:
                finish += 1
        if finish == 2:
            print("------")
            print(self.ball_pos)
            print(self.switch_counter)
            self.posList = [FIRST_CUP_START_X, SECOND_CUP_START_X, THIRD_CUP_START_X]
            self.switch_counter += 1
            self.finish_movement = True

    def __draw_game(self, start):
        demo_y_cups = self.current_y_cup
        x_ball = self.ball_pos
        self.screen.fill(BACKGROUND_COLOR)
        if start:
            if demo_y_cups >= DOWN_CUP_HEIGHT and not self.finish_switches:
                x_ball = -WIDTH
                if self.finish_movement and self.switch_counter < 10:
                    self.finish_movement = False
                    self.from_point = random.randint(1, 3)
                    self.to_point = random.randint(1, 3)
                    while self.to_point == self.from_point:
                        self.to_point = random.randint(1, 3)
                    if self.to_point == self.ball_pos:
                        self.ball_pos = self.from_point
                    elif self.from_point == self.ball_pos:
                        self.ball_pos = self.to_point
                elif not self.finish_movement:
                    print(self.posList2)
                    self.__go_to(self.from_point, self.to_point)
                else:
                    self.finish_switches = True
            elif not self.finish_switches:
                demo_y_cups += 2
                if self.ball_pos == 1:
                    x_ball = FIRST_CUP_BALL_X
                elif self.ball_pos == 2:
                    x_ball = SECOND_CUP_BALL_X
                else:
                    x_ball = THIRD_CUP_BALL_X
                self.current_y_cup += 2
            else:
                demo_y_cups -= 2
                if demo_y_cups > CUP_Y and self.choose != -1:
                    self.current_y_cup = demo_y_cups
                    if self.ball_pos == 1:
                        x_ball = FIRST_CUP_BALL_X
                    elif self.ball_pos == 2:
                        x_ball = SECOND_CUP_BALL_X
                    else:
                        x_ball = THIRD_CUP_BALL_X
                elif demo_y_cups <= CUP_Y:
                    self.finish_animation = True
                if self.choose == -1:
                    x_ball = -WIDTH
            if self.switch_counter == 10:
                self.finish_switches = True

        add_image(self.screen, "images/cups_images/start.png", START_NEW_ROUND_X, START_NEW_ROUND_Y,
                  START_NEW_ROUND_WIDTH,
                  START_NEW_ROUND_HEIGHT, (0, 0, 0))
        add_image(self.screen, "images/cups_images/cuphead.jpg", x_ball, BALL_Y, BALL_WIDTH, BALL_HEIGHT, None)
        add_image(self.screen, "images/cups_images/cup.jpg", self.posList[0], self.current_y_cup, CUP_WIDTH,
                  CUP_HEIGHT, (0, 0, 0))
        add_image(self.screen, "images/cups_images/cup.jpg", self.posList[1], self.current_y_cup, CUP_WIDTH,
                  CUP_HEIGHT, (0, 0, 0))
        add_image(self.screen, "images/cups_images/cup.jpg", self.posList[2], self.current_y_cup, CUP_WIDTH,
                  CUP_HEIGHT, (0, 0, 0))
        display_text(self.screen, round(WIDTH / 7), round(HEIGHT / 8), "your score is: " + str(self.level - 9))

    def game_screen(self):
        mixer.music.load(self.playlist[0])
        mixer.music.play()
        tmp = self.playlist.pop(0)
        self.playlist.append(tmp)
        pygame.mixer.music.queue(self.playlist[0])
        # setting up an end event which host an event
        # after the end of every song
        end_music = pygame.USEREVENT + 1
        mixer.music.set_endevent(end_music)
        refresh_rate = REFRESH_RATE
        start = False
        finish = False
        clock = pygame.time.Clock()
        while not finish:
            mixer.music.queue(self.playlist[0])
            tmp = self.playlist.pop(0)
            self.playlist.append(tmp)
            self.__draw_game(start)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finish = True
                    mixer.music.pause()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if mouse_in_button(new_round_button, pos) and not start:
                        self.ball_pos = random.randint(1, 3)
                        start = True
                    if mouse_in_button(first_cup_button, pos) and self.finish_switches:
                        self.choose = 1
                        add_image(self.screen, "images/cups_images/arrow.png", FIRST_CUP_START_X, CUP_Y , CUP_WIDTH, CUP_HEIGHT, (255,255,255))
                        pygame.display.update()
                        time.sleep(2)
                    if mouse_in_button(second_cup_button, pos) and self.finish_switches:
                        self.choose = 2
                        add_image(self.screen, "images/cups_images/arrow.png", SECOND_CUP_START_X, CUP_Y, CUP_WIDTH, CUP_HEIGHT, (255,255,255))
                        pygame.display.update()
                        time.sleep(2)
                    if mouse_in_button(third_cup_button, pos) and self.finish_switches:
                        self.choose = 3
                        add_image(self.screen, "images/cups_images/arrow.png", THIRD_CUP_START_X, CUP_Y, CUP_WIDTH, CUP_HEIGHT, (255,255,255))
                        pygame.display.update()
                        time.sleep(2)
                    if event.type == end_music:
                        mixer.music.queue(self.playlist[0])
                        tmp = self.playlist.pop(0)
                        self.playlist.append(tmp)

            if self.choose == self.ball_pos and self.choose != -1 and self.finish_animation:
                add_image(self.screen, "images/cups_images/win.jpg", FEEDBACK_X, FEEDBACK_Y, FEEDBACK_WIDTH,
                          FEEDBACK_HEIGHT, (255,255,255))
                pygame.display.update()
                time.sleep(2)
                start = False
                self.__init_game()
                self.level += 1


            elif self.choose != self.ball_pos and self.choose != -1 and self.finish_animation:
                add_image(self.screen, "images/cups_images/loss.jpg", FEEDBACK_X, FEEDBACK_Y, FEEDBACK_WIDTH,
                          FEEDBACK_HEIGHT, (255,255,255))
                pygame.display.update()
                time.sleep(2)
                finish = True
                mixer.music.pause()

            pygame.display.update()
            clock.tick(refresh_rate)
