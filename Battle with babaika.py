from pygame import *
from random import randint
from time import time as timer

# створюємо віконце
win_width = 700
win_height = 500
display.set_caption("Shooter")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))

# створюємо спрайти
ship = Player(img_hero, 5, win_height - 100, 80, 100, 10)
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed,width,heigth):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(width,heigth))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.x = player_x

    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))


        


font.init()
font1 = font.Font(None, 80)
win = font1.render('YOU WIN!', True, (255, 255, 255))
lose = font1.render('YOU LOSE!', True, (180, 0, 0))
font2 = font.Font(None, 36)

img_back = "forest.jpg"  # фон гри
img_hero = "hero.png"  # герой
img_bullet = "bullet.png"
img_enemy = "enemy.png"

back = (200,255,255)
win_width = 600
win_height = 500
window = display.set_mode((win_width,win_height))
window.fill(back)

game = True
finish = False
clock = time.Clock()
FPS = 60

run = True  # прапорець скидається кнопкою закриття вікна

rel_time = False  # прапор, що відповідає за перезаряджання

num_fire = 0
        #подія натискання на пробіл - спрайт стріляє
elif e.type == KEYDOWN:
    if e.key == K_SPACE:
if num_fire >= 5 and rel_time == False : #якщо гравець зробив 5 пострілів
    last_time = timer() #засікаємо час, коли це сталося
    rel_time = True #ставимо прапор перезарядки

# клас спрайта-ворога
class Enemy(GameSprite):
    # рух ворога
    def update(self):
        self.rect.y += self.speed
        global lost
        # зникає, якщо дійде до краю екрана
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            lost = lost + 1

class Bullet(GameSprite):
    # рух ворога
    def update(self):
        self.rect.y += self.speed
        # зникає, якщо дійде до краю екрана
        if self.rect.y < 0:
            self.kill()

bullets = sprite.Group()

finish = False
# Основний цикл гри:
run = True  # прапорець скидається кнопкою закриття вікна
rel_time = False  # прапор, що відповідає за перезаряджання
num_fire = 0 

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP]and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN]and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_w]and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s]and self.rect.y < win_height - 80:
            self.rect.y += self.speed
        # перезарядка #

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

        display.update()
        clock.tick(FPS)