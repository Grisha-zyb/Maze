from pygame import *

WINDOW_SIZE = (1280, 720)
PLAYER_SIZE = (80,80)
ENEMY_SIZE = (120, 120)

window = display.set_mode(WINDOW_SIZE)
background = transform.scale(image.load("fon.png"), WINDOW_SIZE)
display.set_caption("Лабіринт з ворогом")

clock = time.Clock()
FPS = 60

move = True
while move:
    for e in event.get():
        if e.type == QUIT:
            move = False

    window.blit(background, (0, 0))

    clock.tick(FPS)
    display.update()
