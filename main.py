from pygame import *

WINDOW_SIZE = (1280, 720)

window = display.set_mode(WINDOW_SIZE)
background = transform.scale(image.load("fon.png"), WINDOW_SIZE)
display.set_caption("Лабіринт з ворогом")

clock = time.Clock()
FPS = 60

mixer.init()
mixer.music.load('jungles.ogg')
#mixer.music.play()
tp = mixer.Sound('tp.ogg')
defeat_sound = mixer.Sound('kick.ogg')

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

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()

        if keys [K_w] and self.rect.y > 0:
            self.rect.y -= 10
        if keys [K_s] and self.rect.y < WINDOW_SIZE[1] - self.rect.height:
            self.rect.y += 10
        if keys [K_a] and self.rect.x > 0:
            self.rect.x -= 10
        if keys [K_d] and self.rect.x < WINDOW_SIZE[0] - self.rect.width:
            self.rect.x += 10

class Enemy(GameSprite):
    def __init__(self, enemy_image, enemy_x, enemy_y, enemy_speed, direction='left'):
        super().__init__(enemy_image, enemy_x, enemy_y, enemy_speed)
        self.direction = direction
    def update(self):
        if self.direction == 'left':
            self.rect.x -= self.speed
        if self.direction == 'right':
            self.rect.x += self.speed
        if self.rect.x <= 0:
            self.direction = 'right'
        if self.rect.x >= WINDOW_SIZE[0] - self.rect.width:
            self.direction = 'left'

class Wall(sprite.Sprite):
    def __init__(self, width, height, x, y, color):
        self.width = width
        self.height = height
        self.color = color
        self.image = Surface((self.width, self.height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

wall_1 = Wall(300, 30, 100, 100, (0, 0, 0))

player = Player("pers.png", 150, 600, 5)
enemy = Enemy("zombi.jpg", WINDOW_SIZE[0] - 80, WINDOW_SIZE[1] / 2, 10, 'left')
ex1t = GameSprite("exit.png", 1140, 600, 0)

move = True
while move:
    for e in event.get():
        if e.type == QUIT:
            move = False

    window.blit(background, (0, 0))
    player.update()
    player.draw()
    ex1t.draw()
    enemy.update()
    enemy.draw()
    wall_1.draw()

    if sprite.collide_rect(player, wall_1) or sprite.collide_rect(player, enemy):
        player.rect.x = 150
        player.rect.y = 600
        defeat_sound.play()
    if sprite.collide_rect(player, ex1t):
        tp.play()
        time.delay(1000)
        move = False

    clock.tick(FPS)
    display.update()
