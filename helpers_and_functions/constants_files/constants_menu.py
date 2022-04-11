WIDTH = 600
HEIGHT = 600

angles = []

images = ["images/menu_images/cup.png", "images/menu_images/dino.png", "images/menu_images/snake.png",
          "images/menu_images/miluner.png"]

game_text = ["CUPS", "DINOSAUR", "CLASSIC SNAKE", "MILLIONAIRE"]

for i in range(0, 180, round(180 / len(images))):
    angles.append(i + round(180 / len(images) / 2))
    print(i)

RADIUS = 100
SMALL_RADIUS = 15
IMAGE_RADIUS = 20

CENTER = (WIDTH / 2, HEIGHT)

TEXT_X = WIDTH / 2
TEXT_Y = HEIGHT / 5 * 4

WHITE = (255, 255, 255)
