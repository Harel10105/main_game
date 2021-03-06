WIDTH = 800
HEIGHT = 600

angles = []

images = ["images/menu_images/cup.png", "images/menu_images/dino.png", "images/menu_images/snake.png",
          "images/menu_images/dollar.png","images/menu_images/medal.png","images/menu_images/miluner.png"]

game_text = ["CUPS", "DINOSAUR", "CLASSIC SNAKE", "MILLIONAIRE","HIGH SCORES","INSTRUCTIONS"]

for i in range(0, 180, round(180 / len(images))):
    angles.append(i + round(180 / len(images) / 2))
    print(i)

RADIUS = round((WIDTH/7+HEIGHT/6)/2)
SMALL_RADIUS = round((WIDTH/33+HEIGHT/30)/2)
IMAGE_RADIUS = round((WIDTH/26+HEIGHT/22)/2)

CENTER = (WIDTH / 2, HEIGHT)

TEXT_X = round(WIDTH / 2)
TEXT_Y = HEIGHT -round(RADIUS/2)

WHITE = (255, 255, 255)

MAIN_TITLE_WIDTH = round(WIDTH*1.1)
MAIN_TITLE_HEIGHT = round(HEIGHT*1.1)
MAIN_TITLE_X = round(WIDTH/2-MAIN_TITLE_WIDTH/2)
MAIN_TITLE_Y = round(HEIGHT/4-MAIN_TITLE_HEIGHT/2)

SCORE_X = 50
SCORE_Y = 50
SCORE_HEIGHT = round((HEIGHT-SCORE_Y)/5)
SCORE_WIDTH = round((WIDTH-SCORE_X)/2)

BACK_X = WIDTH - 50
BACK_Y = 0
BACK_WIDTH = 50
BACK_HEIGHT = 50
