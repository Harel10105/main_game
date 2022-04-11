from helpers_and_functions.Buttons import Button
from helpers_and_functions.constants_files.constants_millioner import *

exitButton = Button(round(WIDTH/50), round(HEIGHT/8), round(WIDTH/14.287), round(HEIGHT/16))
start_new_gameButton = Button(WIDTH / 2 - round(WIDTH/5), HEIGHT / 2 - round(HEIGHT/4), round(WIDTH/2.5), round(HEIGHT/2))
progress_bar = Button(WIDTH - 100, HEIGHT - 100, 100, 100)
answer1_button = Button(ANSWER1_LOCATION_WIDTH + BOX_MARGIN_WIDTH, ANSWER1_LOCATION_HEIGHT + BOX_MARGIN_HEIGHT,
                        ANSWER_BOX_SIZE_WIDTH, ANSWER_BOX_SIZE_HEIGHT)
answer2_button = Button(ANSWER2_LOCATION_WIDTH + BOX_MARGIN_WIDTH, ANSWER2_LOCATION_HEIGHT + BOX_MARGIN_HEIGHT,
                        ANSWER_BOX_SIZE_WIDTH, ANSWER_BOX_SIZE_HEIGHT)
answer3_button = Button(ANSWER3_LOCATION_WIDTH + BOX_MARGIN_WIDTH, ANSWER3_LOCATION_HEIGHT + BOX_MARGIN_HEIGHT,
                        ANSWER_BOX_SIZE_WIDTH, ANSWER_BOX_SIZE_HEIGHT)
answer4_button = Button(ANSWER4_LOCATION_WIDTH + BOX_MARGIN_WIDTH, ANSWER4_LOCATION_HEIGHT + BOX_MARGIN_HEIGHT,
                        ANSWER_BOX_SIZE_WIDTH, ANSWER_BOX_SIZE_HEIGHT)
help_fifty_fifty_button = Button(FIFTY_BUTTON_WIDTH_LOC, FIFTY_BUTTON_HEIGHT_LOC, HELP_BUTTON_WIDTH, HELP_BUTTON_HEIGHT)
help_change_question_button = Button(SWITCH_BUTTON_WIDTH_LOC, SWITCH_BUTTON_HEIGHT_LOC, HELP_BUTTON_WIDTH,
                                     HELP_BUTTON_HEIGHT)