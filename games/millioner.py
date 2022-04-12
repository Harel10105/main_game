from tkinter import Tk

import pygame
from pygame import mixer
from tkinter import *
from PIL import ImageTk, Image
from helpers_and_functions.constants_files.constants_millioner import *
from games.class_helpers.Question import *
from helpers_and_functions.buttons_to_use.buttons_to_use_millioner import *
from helpers_and_functions.function_helpers import *
import time


class Millioner():
    def __init__(self, screen):
        self.menu(screen)

    def player_win(self, screen):
        mixer.init()
        mixer.music.set_volume(0.7)
        mixer.music.load("music/millioner_music/winMusic.mp3")
        mixer.music.play(loops=-1)
        add_image(screen, "images/millioner_images/winwin.png", 0, 0, WIDTH, HEIGHT, None)
        add_image(screen, "images/millioner_images/exitLogo.png", round(WIDTH / 50), round(HEIGHT / 8),
                  round(WIDTH / 14.28),
                  round(HEIGHT / 16), PINK)
        player_closed = False
        while not player_closed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    player_closed = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if mouse_in_button(exitButton, mouse_pos):
                        player_closed = True
            pygame.display.update()

    def player_lose(self, screen):
        mixer.init()
        mixer.music.set_volume(0.7)
        mixer.music.load("music/millioner_music/wrong answer.mp3")
        mixer.music.play()
        add_image(screen, "images/millioner_images/loser.png", 0, 0, WIDTH, HEIGHT, None)
        add_image(screen, "images/millioner_images/exitLogo.png", round(WIDTH / 50), round(HEIGHT / 8),
                  round(WIDTH / 14.28),
                  round(HEIGHT / 16), PINK)
        player_closed = False
        while not player_closed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    player_closed = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if mouse_in_button(exitButton, mouse_pos):
                        player_closed = True
            pygame.display.update()

    def change_lights(self, screen, mode):
        cur_height_lights = 0
        pointer = True
        clock = pygame.time.Clock()
        finish = False
        if mode:
            beginning_high = -round(HEIGHT / 8)
        else:
            beginning_high = 0
        while not finish:
            screen.fill(BLUE)
            add_image(screen, "images/millioner_images/exitLogo.png", round(WIDTH / 50), round(HEIGHT / 8),
                      round(WIDTH / 14.28),
                      round(HEIGHT / 16), PINK)
            add_image(screen, "images/millioner_images/logo.png", WIDTH / 2 - round(WIDTH / 5),
                      HEIGHT / 2 - round(HEIGHT / 4),
                      round(WIDTH / 2.5), round(HEIGHT / 2), PINK)
            if pointer:
                add_image(screen, "images/millioner_images/lights_stand.png", 0, beginning_high - cur_height_lights,
                          WIDTH,
                          round(HEIGHT / 8),
                          None)
            else:
                add_image(screen, "images/millioner_images/lights_stand2.png", 0, beginning_high - cur_height_lights,
                          WIDTH,
                          round(HEIGHT / 8),
                          None)

            pointer = not pointer
            if not mode:
                if cur_height_lights < round(HEIGHT / 8):
                    cur_height_lights += round(HEIGHT / 80)
                else:
                    finish = True
            else:
                if cur_height_lights > -round(HEIGHT / 8):
                    cur_height_lights -= round(HEIGHT / 80)
                else:
                    finish = True
            pygame.display.update()
            clock.tick(REFRESH_RATE)
        return pointer

    def start_pop_up(self, screen):
        background_image = "images/millioner_images/back.jpg"
        background_load = pygame.image.load(background_image)
        background_load = pygame.transform.scale(background_load, (WIDTH, HEIGHT))

        question_block_image = "images/millioner_images/quiestion_block.png"
        question_block_load = pygame.image.load(question_block_image)
        question_block_load = pygame.transform.scale(question_block_load, (QUESTION_BLOCK_WIDTH, QUESTION_BLOCK_HEIGHT))

        fifty_button_image = "images/millioner_images/even_better_fifty.png"
        fifty_button_load = pygame.image.load(fifty_button_image)
        fifty_button_load = pygame.transform.scale(fifty_button_load, (HELP_BUTTON_WIDTH, HELP_BUTTON_HEIGHT))

        switch_button_image = "images/millioner_images/switch.png"
        switch_button_load = pygame.image.load(switch_button_image)
        switch_button_load = pygame.transform.scale(switch_button_load, (HELP_BUTTON_WIDTH, HELP_BUTTON_HEIGHT))

        screen.blit(background_load, (0, 0))
        for i in range(HEIGHT, HEIGHT - QUESTION_BLOCK_HEIGHT, -round(HEIGHT / 160)):
            screen.blit(question_block_load, ((WIDTH - QUESTION_BLOCK_WIDTH) / 2, i))
            pygame.display.update()
            time.sleep(0.03)

        add_image(screen, "images/millioner_images/exitLogo.png", round(WIDTH / 50), round(HEIGHT / 8),
                  round(WIDTH / 14.28),
                  round(HEIGHT / 16), PINK)
        add_image(screen, "images/millioner_images/level_board_icon.png", WIDTH - round(WIDTH / 10),
                  HEIGHT - round(HEIGHT / 8),
                  round(WIDTH / 10), round(HEIGHT / 8), PINK)

        screen.blit(fifty_button_load, (FIFTY_BUTTON_WIDTH_LOC, FIFTY_BUTTON_HEIGHT_LOC))

        screen.blit(switch_button_load, (SWITCH_BUTTON_WIDTH_LOC, SWITCH_BUTTON_HEIGHT_LOC))

    def display_questions(self, screen, question, answers):
        display_text(screen, QUESTION_LOCATION_WIDTH, QUESTION_LOCATION_HEIGHT, question)

        display_text(screen, ANSWER1_LOCATION_WIDTH, ANSWER1_LOCATION_HEIGHT, answers[0])

        display_text(screen, ANSWER2_LOCATION_WIDTH, ANSWER2_LOCATION_HEIGHT, answers[1])

        display_text(screen, ANSWER3_LOCATION_WIDTH, ANSWER3_LOCATION_HEIGHT, answers[2])

        display_text(screen, ANSWER4_LOCATION_WIDTH, ANSWER4_LOCATION_HEIGHT, answers[3])

    def display_right(self, screen, place, isAble_fifty_fifty, isAble_change_question, question, only):
        mixer.init()
        if only:
            mixer.music.load("music/millioner_music/correct answer.mp3")
            mixer.music.set_volume(0.7)
            mixer.music.play()
            add_image(screen, "images/millioner_images/back.jpg", 0, 0, WIDTH, HEIGHT, None)
            add_image(screen, "images/millioner_images/exitLogo.png", round(WIDTH / 50), round(HEIGHT / 8),
                      round(WIDTH / 14.28),
                      round(HEIGHT / 16), PINK)
            add_image(screen, "images/millioner_images/quiestion_block.png", (WIDTH - QUESTION_BLOCK_WIDTH) / 2,
                      HEIGHT - QUESTION_BLOCK_HEIGHT,
                      QUESTION_BLOCK_WIDTH, QUESTION_BLOCK_HEIGHT, None)
            add_image(screen, "images/millioner_images/level_board_icon.png", WIDTH - round(WIDTH / 10),
                      HEIGHT - round(HEIGHT / 8),
                      round(WIDTH / 10), round(HEIGHT / 8), PINK)
            if not isAble_fifty_fifty:
                add_image(screen, "images/millioner_images/dark_fifty.png", FIFTY_BUTTON_WIDTH_LOC,
                          FIFTY_BUTTON_HEIGHT_LOC,
                          HELP_BUTTON_WIDTH, HELP_BUTTON_HEIGHT, None)
            else:
                add_image(screen, "images/millioner_images/even_better_fifty.png", FIFTY_BUTTON_WIDTH_LOC,
                          FIFTY_BUTTON_HEIGHT_LOC,
                          HELP_BUTTON_WIDTH, HELP_BUTTON_HEIGHT, None)
            if not isAble_change_question:
                add_image(screen, "images/millioner_images/dark_switch.png", SWITCH_BUTTON_WIDTH_LOC,
                          SWITCH_BUTTON_HEIGHT_LOC,
                          HELP_BUTTON_WIDTH, HELP_BUTTON_HEIGHT, None)
            else:
                add_image(screen, "images/millioner_images/switch.png", SWITCH_BUTTON_WIDTH_LOC,
                          SWITCH_BUTTON_HEIGHT_LOC,
                          HELP_BUTTON_WIDTH, HELP_BUTTON_HEIGHT, None)
            add_image(screen, "images/millioner_images/level_board_icon.png", WIDTH - round(WIDTH / 10),
                      HEIGHT - round(HEIGHT / 8),
                      round(WIDTH / 10), round(HEIGHT / 8), PINK)
        right_image = "images/millioner_images/right.png"
        right_load = pygame.image.load(right_image)
        right_load = pygame.transform.scale(right_load, (ANSWER_BOX_SIZE_WIDTH, ANSWER_BOX_SIZE_HEIGHT))
        if place == 1:
            screen.blit(right_load,
                        (ANSWER1_LOCATION_WIDTH + BOX_MARGIN_WIDTH, ANSWER1_LOCATION_HEIGHT + BOX_MARGIN_HEIGHT))
        elif place == 2:
            screen.blit(right_load,
                        (ANSWER2_LOCATION_WIDTH + BOX_MARGIN_WIDTH, ANSWER2_LOCATION_HEIGHT + BOX_MARGIN_HEIGHT))
        elif place == 3:
            screen.blit(right_load,
                        (ANSWER3_LOCATION_WIDTH + BOX_MARGIN_WIDTH, ANSWER3_LOCATION_HEIGHT + BOX_MARGIN_HEIGHT))
        elif place == 4:
            screen.blit(right_load,
                        (ANSWER4_LOCATION_WIDTH + BOX_MARGIN_WIDTH, ANSWER4_LOCATION_HEIGHT + BOX_MARGIN_HEIGHT))
        self.display_questions(screen, question.get_question(), question.get_possible_answers())
        pygame.display.update()
        time.sleep(5.0)
        if only:
            mixer.music.stop()

    def display_wrong(self, screen, place, isAble_fifty_fifty, isAble_change_question, question):
        add_image(screen, "images/millioner_images/back.jpg", 0, 0, WIDTH, HEIGHT, None)
        add_image(screen, "images/millioner_images/exitLogo.png", round(WIDTH / 50), round(HEIGHT / 8),
                  round(WIDTH / 14.28),
                  round(HEIGHT / 16), PINK)
        add_image(screen, "images/millioner_images/quiestion_block.png", (WIDTH - QUESTION_BLOCK_WIDTH) / 2,
                  HEIGHT - QUESTION_BLOCK_HEIGHT,
                  QUESTION_BLOCK_WIDTH, QUESTION_BLOCK_HEIGHT, None)
        if not isAble_fifty_fifty:
            add_image(screen, "images/millioner_images/dark_fifty.png", FIFTY_BUTTON_WIDTH_LOC, FIFTY_BUTTON_HEIGHT_LOC,
                      HELP_BUTTON_WIDTH, HELP_BUTTON_HEIGHT, None)
        else:
            add_image(screen, "images/millioner_images/even_better_fifty.png", FIFTY_BUTTON_WIDTH_LOC,
                      FIFTY_BUTTON_HEIGHT_LOC,
                      HELP_BUTTON_WIDTH, HELP_BUTTON_HEIGHT, None)
        if not isAble_change_question:
            add_image(screen, "images/millioner_images/dark_switch.png", SWITCH_BUTTON_WIDTH_LOC,
                      SWITCH_BUTTON_HEIGHT_LOC,
                      HELP_BUTTON_WIDTH, HELP_BUTTON_HEIGHT, None)
        else:
            add_image(screen, "images/millioner_images/switch.png", SWITCH_BUTTON_WIDTH_LOC, SWITCH_BUTTON_HEIGHT_LOC,
                      HELP_BUTTON_WIDTH, HELP_BUTTON_HEIGHT, None)
        add_image(screen, "images/millioner_images/level_board_icon.png", WIDTH - round(WIDTH / 10),
                  HEIGHT - round(HEIGHT / 8),
                  round(WIDTH / 10), round(HEIGHT / 8), PINK)
        right_image = "images/millioner_images/wrong.png"
        right_load = pygame.image.load(right_image)
        right_load = pygame.transform.scale(right_load, (ANSWER_BOX_SIZE_WIDTH, ANSWER_BOX_SIZE_HEIGHT))
        if place == 1:
            screen.blit(right_load,
                        (ANSWER1_LOCATION_WIDTH + BOX_MARGIN_WIDTH, ANSWER1_LOCATION_HEIGHT + BOX_MARGIN_HEIGHT))
        elif place == 2:
            screen.blit(right_load,
                        (ANSWER2_LOCATION_WIDTH + BOX_MARGIN_WIDTH, ANSWER2_LOCATION_HEIGHT + BOX_MARGIN_HEIGHT))
        elif place == 3:
            screen.blit(right_load,
                        (ANSWER3_LOCATION_WIDTH + BOX_MARGIN_WIDTH, ANSWER3_LOCATION_HEIGHT + BOX_MARGIN_HEIGHT))
        elif place == 4:
            screen.blit(right_load,
                        (ANSWER4_LOCATION_WIDTH + BOX_MARGIN_WIDTH, ANSWER4_LOCATION_HEIGHT + BOX_MARGIN_HEIGHT))
        self.display_right(screen, question.get_right_answer_number(), isAble_fifty_fifty, isAble_change_question,
                           question,
                           False)

    def progressionScreen(self, currLevel):
        img_dic = {1: "images/millioner_images/board1000.png", 2: "images/millioner_images/board2000.png",
                   3: "images/millioner_images/board5000.png", 4: "images/millioner_images/board10000.png",
                   5: "images/millioner_images/board25000.png",
                   6: "images/millioner_images/board50000.png", 7: "images/millioner_images/board100000.png",
                   8: "images/millioner_images/board250000.png",
                   9: "images/millioner_images/board500000.png", 10: "images/millioner_images/board1000000.png"}
        if 0 < currLevel < 11:
            root = Tk()
            canvas = Canvas(root, width=round(WIDTH / 2.8), height=round(HEIGHT / 2.8))
            canvas.pack()
            image = Image.open(img_dic.pop(currLevel))
            img = image.resize((round(WIDTH / 2.8), round(HEIGHT / 2.8)), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(img)
            canvas.create_image(20, 20, anchor=NW, image=img)
            root.mainloop()

    def menu(self, screen):
        mixer.init()
        screen.fill(BLUE)
        add_image(screen, "images/millioner_images/exitLogo.png", round(WIDTH / 50), round(HEIGHT / 8),
                  round(WIDTH / 14.28),
                  round(HEIGHT / 16), PINK)
        add_image(screen, "images/millioner_images/logo.png", WIDTH / 2 - round(WIDTH / 5), HEIGHT / 2 - round(HEIGHT / 4),
                  round(WIDTH / 2.5), round(HEIGHT / 2), PINK)
        mixer.music.set_volume(0.7)
        mixer.music.load("music/millioner_music/Main Theme.mp3")
        pygame.mixer.music.play(loops=-1)
        player_closed = False
        pointer = True
        clock = pygame.time.Clock()
        while not player_closed:
            if pointer:
                add_image(screen, "images/millioner_images/lights_stand.png", 0, 0, WIDTH, round(HEIGHT / 8), None)
            else:
                add_image(screen, "images/millioner_images/lights_stand2.png", 0, 0, WIDTH, round(HEIGHT / 8), None)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    player_closed = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if mouse_in_button(exitButton, mouse_pos):
                        player_closed = True
                    if mouse_in_button(start_new_gameButton, mouse_pos):
                        pointer = self.change_lights(screen, False)
                        self.game(screen)
                        screen.fill(BLUE)
                        add_image(screen, "images/millioner_images/exitLogo.png", round(WIDTH / 50), round(HEIGHT / 8),
                                  round(WIDTH / 14.28),
                                  round(HEIGHT / 16), PINK)
                        add_image(screen, "images/millioner_images/logo.png", WIDTH / 2 - round(WIDTH / 5),
                                  HEIGHT / 2 - round(HEIGHT / 4), round(WIDTH / 2.5), round(HEIGHT / 2), PINK)
                        pointer = self.change_lights(screen, True)
                        self.menu(screen)
                        player_closed = True
            print(1)
            pointer = not pointer
            pygame.display.update()
            clock.tick(REFRESH_RATE)
        mixer.music.stop()

    def game(self, screen):
        mixer.init()
        level = 0
        inLevel = False
        mixer.music.set_volume(0.7)
        mixer.music.load("music/millioner_music/lets play.mp3")
        mixer.music.play()
        counter = 21
        time_to_show = 5.0
        chose = 0
        timer_event = pygame.USEREVENT + 1
        pygame.time.set_timer(timer_event, 1000)

        self.start_pop_up(screen)
        # display_right(screen, 1)

        background_image = "images/millioner_images/back.jpg"
        background_load = pygame.image.load(background_image)
        background_load = pygame.transform.scale(background_load, (WIDTH, HEIGHT))

        question_block_image = "images/millioner_images/quiestion_block.png"
        question_block_load = pygame.image.load(question_block_image)
        question_block_load = pygame.transform.scale(question_block_load, (QUESTION_BLOCK_WIDTH, QUESTION_BLOCK_HEIGHT))

        # Show timer
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(round(WIDTH / 1.17), round(HEIGHT / 44.44), round(WIDTH / 8.33),
                                                        round(HEIGHT / 6.66)))
        pygame.display.flip()
        text = str(counter).rjust(3)
        display_text(screen, round(WIDTH / 1.09), round(HEIGHT / 16), "Time left:")
        display_text(screen, round(WIDTH / 1.09), round(HEIGHT / 8.88), text)

        isWin = False
        player_closed = False
        w = True
        inLevel = False
        isAble_50_50 = True
        isAble_change_question = True
        notAnswered = True
        is_able_to_click = True
        while not player_closed:
            w = True
            if not isAble_50_50:
                add_image(screen, "images/millioner_images/dark_fifty.png", FIFTY_BUTTON_WIDTH_LOC,
                          FIFTY_BUTTON_HEIGHT_LOC,
                          HELP_BUTTON_WIDTH, HELP_BUTTON_HEIGHT, None)
            if not isAble_change_question:
                add_image(screen, "images/millioner_images/dark_switch.png", SWITCH_BUTTON_WIDTH_LOC,
                          SWITCH_BUTTON_HEIGHT_LOC,
                          HELP_BUTTON_WIDTH, HELP_BUTTON_HEIGHT, None)
            if not inLevel:
                level += 1
                if level < 11 and chose == 0:
                    is_able_to_click = True
                    notAnswered = True
                    inLevel = True
                    question = Question(level)
                    screen.blit(background_load, (WIDTH, HEIGHT))
                    screen.blit(question_block_load,
                                ((WIDTH - QUESTION_BLOCK_WIDTH) / 2, HEIGHT - QUESTION_BLOCK_HEIGHT))
                    self.display_questions(screen, question.get_question(), question.get_possible_answers())
                    counter = question.get_max_time()
                    time_to_show = question.get_max_show()
            else:
                if chose != 0:
                    is_able_to_click = False
                    notAnswered = False
                    counter = 100
                    print(1)
                    mixer.music.load("music/millioner_music/final answer.mp3")
                    mixer.music.play()
                    print(time_to_show)
                    time.sleep(time_to_show)
                    mixer.music.stop()
                    if chose == question.get_right_answer_number():
                        self.display_right(screen, chose, isAble_50_50, isAble_change_question, question, True)
                        inLevel = False
                        chose = 0
                    else:
                        self.display_wrong(screen, chose, isAble_50_50, isAble_change_question, question)
                        player_closed = True
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    w = True
                    player_closed = True
                if event.type == pygame.MOUSEBUTTONDOWN and is_able_to_click:
                    mouse_pos = pygame.mouse.get_pos()
                    print(mouse_pos)
                    if mouse_in_button(exitButton, mouse_pos):
                        w = True
                        player_closed = True
                    if mouse_in_button(answer1_button, mouse_pos):
                        chose = 1
                        if level == 10:
                            w = True
                            player_closed = True
                    if mouse_in_button(answer2_button, mouse_pos):
                        chose = 2
                        if level == 10:
                            w = True
                            player_closed = True
                    if mouse_in_button(answer3_button, mouse_pos):
                        chose = 3
                        if level == 10:
                            w = True
                            player_closed = True
                    if mouse_in_button(answer4_button, mouse_pos):
                        chose = 4
                        if level == 10:
                            w = True
                            player_closed = True
                    if mouse_in_button(progress_bar, mouse_pos):
                        w = False
                        chose = 0
                        self.progressionScreen(level)
                    if mouse_in_button(help_fifty_fifty_button, mouse_pos) and isAble_50_50 and notAnswered:
                        answers = question.get_50_50()
                        print(answers)
                        screen.blit(question_block_load,
                                    ((WIDTH - QUESTION_BLOCK_WIDTH) / 2, HEIGHT - QUESTION_BLOCK_HEIGHT))
                        self.display_questions(screen, question.get_question(), answers)
                        isAble_50_50 = False
                    if mouse_in_button(help_change_question_button,
                                       mouse_pos) and isAble_change_question and notAnswered:
                        question.get_other_question()
                        new_question = question.get_question()
                        new_answers = question.get_possible_answers()
                        screen.blit(question_block_load,
                                    ((WIDTH - QUESTION_BLOCK_WIDTH) / 2, HEIGHT - QUESTION_BLOCK_HEIGHT))
                        self.display_questions(screen, new_question, new_answers)
                        isAble_change_question = False
                        counter = question.get_max_time()
                        time_to_show = question.get_max_show()

                if event.type == timer_event:
                    counter -= 1
                    # Show timer
                    pygame.draw.rect(screen, (0, 0, 0),
                                     pygame.Rect(round(WIDTH / 1.17), round(HEIGHT / 44.44), round(WIDTH / 8.33),
                                                 round(HEIGHT / 6.66)))
                    pygame.display.flip()
                    text = str(counter).rjust(3)
                    display_text(screen, round(WIDTH / 1.09), round(HEIGHT / 16), "Time left:")
                    display_text(screen, round(WIDTH / 1.09), round(HEIGHT / 8.88), text)
                    print(counter)
                    if counter == 0:
                        w = True
                        player_closed = True
            if level == 10 and chose == question.get_right_answer_number():
                counter = 100
                print(1)
                mixer.music.load("music/millioner_music/final answer.mp3")
                mixer.music.play()
                print(time_to_show)
                time.sleep(time_to_show)
                mixer.music.stop()
                self.display_right(screen, chose, isAble_50_50, isAble_change_question, question, True)
                isWin = True
                player_closed = True
            elif level == 10 and chose != question.get_right_answer_number() and chose != 0:
                counter = 100
                print(1)
                mixer.music.load("music/millioner_music/final answer.mp3")
                mixer.music.play()
                print(time_to_show)
                time.sleep(time_to_show)
                mixer.music.stop()
                self.display_wrong(screen, chose, isAble_50_50, isAble_change_question, question)
                player_closed = True
                w = True

            pygame.display.update()
            if not w:
                player_closed = False
        print(isWin)

        if isWin:
            self.player_win(screen)
        else:
            self.player_lose(screen)
        print("thank you for playing!")
