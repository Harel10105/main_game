WIDTH = 700
HEIGHT = 500

angles = []

images = ["images/menu_images/cup.png", "images/menu_images/dino.png", "images/menu_images/snake.png",
          "images/menu_images/miluner.png"]

game_text = ["CUPS", "DINOSAUR", "CLASSIC SNAKE", "MILLIONAIRE"]

for i in range(0, 180, round(180 / len(images))):
    angles.append(i + round(180 / len(images) / 2))
    print(i)

RADIUS = round((WIDTH/7+HEIGHT/6)/2)
SMALL_RADIUS = round((WIDTH/33+HEIGHT/30)/2)
IMAGE_RADIUS = round((WIDTH/25+HEIGHT/22)/2)

CENTER = (WIDTH / 2, HEIGHT)

TEXT_X = round(WIDTH / 2)
TEXT_Y = HEIGHT -round(RADIUS/2)

WHITE = (255, 255, 255)

MAIN_TITLE_WIDTH = round(WIDTH*1.1)
MAIN_TITLE_HEIGHT = round(HEIGHT*1.1)
MAIN_TITLE_X = round(WIDTH/2-MAIN_TITLE_WIDTH/2)
MAIN_TITLE_Y = round(HEIGHT/4-MAIN_TITLE_HEIGHT/2)
