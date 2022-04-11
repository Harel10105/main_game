from helpers_and_functions.constants_files.constants_menu import WIDTH,HEIGHT

GRID_SIZE = 25
GRID_WIDTH = WIDTH / GRID_SIZE
GRID_HEIGHT = HEIGHT / GRID_SIZE

CLOCK_FPS = 100

UP = "UP"
DOWN = "DOWN"
LEFT = "LEFT"
RIGHT = "RIGHT"

DIRECTION_DICT = {UP: [0,-1],
                  DOWN: [0,1],
                  LEFT: [-1,0],
                  RIGHT: [1,0]}

BACKGROUND_COLOR = (20, 20, 20)
START_BACKGROUND_COLOR = (10, 10, 10)
SNAKE_COLOR = (108, 187, 60)

GRID_MID = (int(GRID_WIDTH / 2), int(GRID_HEIGHT / 2))
SNAKE_STARTING_LOC = (10, 10)
GAME_SPEED = 10