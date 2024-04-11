from pygame import *
import pygame
'''Необхідні класи'''

# клас-батько для спрайтів
class GameSprite(sprite.Sprite):
    # конструктор класу
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        # кожен спрайт повинен зберігати властивість image - зображення
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        # кожен спрайт повинен зберігати властивість rect - прямокутник, в який він вписаний
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        # Jump Together!
        self.jump_height = 10
        self.is_jumping = False
        self.jump_velocity = 0
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class GameSprite2(sprite.Sprite):
    # конструктор класу
    def __init__(self, player_image, player_x, player_y, player_speed):

        # кожен спрайт повинен зберігати властивість image - зображення
        self.image = transform.scale(image.load(player_image), (100, 100))
        self.speed = player_speed
        # кожен спрайт повинен зберігати властивість rect - прямокутник, в який він вписаний
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        # Jump Together!
        self.jump_height = 15
        self.is_jumping = False
        self.jump_velocity = 0
    def reset2(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

# клас-спадкоємець для спрайту-гравця (керується стрілками)
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed

        if keys[K_SPACE] and not self.is_jumping:
            self.is_jumping = True
            self.jump_velocity = self.jump_height

        if self.is_jumping:
            self.jump_velocity -= 0.3
            self.rect.y -= self.jump_velocity
            if self.jump_velocity <= 0:
                self.is_jumping = False
                self.jump_velocity = 0
        if not self.is_jumping and self.rect.y < win_height - 80:
            self.rect.y += self.speed
        
        if not sprite.collide_rect(self, walltexture):
            self.rect.y += self.speed 
        else:
            self.rect.y = walltexture.rect.top - self.rect.height + 1

        #if not sprite.collide_rect(self, walltexture2):
        #    self.rect.y += self.speed 
        #else:
        #    self.rect.y = walltexture2.rect.top - self.rect.height + 1
#
        #if not sprite.collide_rect(self, walltexture5):
        #    self.rect.y += self.speed 
        #else:
        #    self.rect.y = walltexture5.rect.top - self.rect.height + 1        
# клас-спадкоємець для спрайта-ворога (переміщається сам)
class Enemy(GameSprite):
    direction = "left"

    def update(self):
        if self.rect.x <= 470:
            self.direction = "right"
        if self.rect.x >= win_width - 85:
            self.direction = "left"

        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

# клас для спрайтів-перешкод
class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        # картинка стіни - прямокутник потрібних розмірів та кольору
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        # кожен спрайт повинен зберігати властивість rect - прямокутник
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        #draw.rect(window, (self.color_1, self.color_2, self.color_3), (self.rect.x, self.rect.y, self.width, self.height))


# Ігрова сцена:
win_width = 700
win_height = 500

window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load("forest.jpg"), (win_width, win_height))
#walltexture = transform.scale(image.load("ground.jpg"), (150, 150))

# Персонажі гри:
player = Player('hero(i).png', 5, win_height - 80, 4)
monster = Enemy('New Piskel.png', win_width - 80, 280, 2)
final = GameSprite('caveportal.png', win_width - 120, win_height - 140   , 0)
walltexture = GameSprite2('ground.jpg', 0, win_height - 80, 0)
walltexture2 = GameSprite2('ground.jpg', 100, win_height - 80, 0)
voidl = GameSprite2('voidnessleft.png', 200, win_height - 100, 0)
voidr = GameSprite2('voidnessright.png', 300, win_height - 100, 0)
walltexture5 = GameSprite2('ground.jpg', 400, win_height - 80, 0)
voidhostle = GameSprite2('voidness.png', 500, win_height - 100, 0)
walltexture7 = GameSprite2('ground.jpg', 600, win_height - 80, 0)


# Time Clock
game = True
finish = False
clock = time.Clock()
FPS = 60

# написи
font.init()
font = font.Font(None, 70)
win = font.render('YOU WIN!', True, (255, 215, 0))
lose = font.render('YOU LOSE!', True, (180, 0, 0))




while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.blit(background, (0, 0))
 
        player.update()
        monster.update()

        player.reset()
        monster.reset()
        final.reset()
        walltexture.reset2()
        walltexture2.reset2()
        voidl.reset2()
        voidr.reset2()
        walltexture5.reset2()
        voidhostle.reset2()
        walltexture7.reset2()


    # Ситуація "Програш"
        #finish = True
        #window.blit(lose, (200, 200))

    # Ситуація "Перемога"
    if sprite.collide_rect(player, final):
        #finish = True
        #window.blit(win, (200, 200))
        background = transform.scale(image.load("cave.png"), (win_width, win_height))
        window.blit(background, (0, 0))
        walltexture = GameSprite2('ground.jpg', 0, win_height - 80, 0)
        walltexture.reset2()

    display.update()
    clock.tick(FPS)