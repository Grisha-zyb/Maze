from pygame import *

WINDOW_SIZE = (1280, 720)

window = display.set_mode(WINDOW_SIZE)
background = transform.scale(image.load("fon.png"), WINDOW_SIZE)
display.set_caption("Лабіринт з ворогом")

clock = time.Clock()
FPS = 60

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (80,80))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

player = GameSprite("pers.png", 150, 600, 5)
enemy = GameSprite("zombi.jpg", WINDOW_SIZE[0] - 80, WINDOW_SIZE[1] / 2, 20)
ex1t = GameSprite("exit.png", 1140, 600, 0)

move = True
while move:
    for e in event.get():
        if e.type == QUIT:
            move = False

    window.blit(background, (0, 0))
    player.draw()
    ex1t.draw()
    enemy.draw()

    clock.tick(FPS)
    display.update()
