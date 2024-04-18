from pygame import *
import pygame

class GameSprite(sprite.Sprite):

    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()

        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class GameSprite2(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        self.image = transform.scale(image.load(player_image), (100, 100))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset2(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class GameSprite3(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        self.image = transform.scale(image.load(player_image), (100, 11))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset3(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed

        if keys[K_SPACE]:
            player.rect.y -= 10

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

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height

        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))

        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        
win_width = 700
win_height = 500

window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load("forest.jpg"), (win_width, win_height))

player = Player('hero(i).png', 5, 300, 4)
final = GameSprite('caveportal.png', win_width - 80, win_height - 140   , 0)


walltexture = GameSprite2('ground.jpg', 0, win_height - 80, 0)
walltexture2 = GameSprite2('ground.jpg', 100, win_height - 80, 0)

line1 = GameSprite3('line.png', 0, win_height - 80, 0)
line2 = GameSprite3('line.png', 100, win_height - 80, 0)


voidl = GameSprite2('voidnessleft.png', 200, win_height - 100, 0)
voidr = GameSprite2('voidnessright.png', 300, win_height - 100, 0)
walltexture5 = GameSprite2('dirt.png', 400, win_height - 80, 0)
voidhostle = GameSprite2('voidness.png', 500, win_height - 100, 0)
voidhostle2 = GameSprite2('voidness.png',0, win_height - 300, 0)
walltexture8 = GameSprite2('dirt.png', 400, win_height - 180, 0)


walltexture7 = GameSprite2('ground.jpg', 600, win_height - 80, 0)
walltexture9 = GameSprite2('ground.jpg', 400, win_height - 440, 0)
walltexture10 = GameSprite2('ground.jpg', 200, win_height - 280, 0)
walltexture11 = GameSprite2('ground.jpg', 100, win_height - 280, 0)
walltexture12 = GameSprite2('ground.jpg', 100, win_height - 480, 0)
walltexture13 = GameSprite2('ground.jpg', 200, win_height - 480, 0)
walltexture14 = GameSprite2('ground.jpg', 300, win_height - 480, 0)
line7 = GameSprite3('line.png', 600, win_height - 80, 0)
line9 = GameSprite3  ('line.png', 400, win_height - 440, 0)
line10 = GameSprite3('line.png', 200, win_height - 280, 0)
line11 = GameSprite3('line.png', 100, win_height - 280, 0)
line12 = GameSprite3('line.png', 100, win_height - 480, 0)
line13 = GameSprite3('line.png', 200, win_height - 480, 0)
line14 = GameSprite3('line.png', 300, win_height - 480, 0)
line15 = GameSprite3('line.png', 200, win_height - 480, 0)
line16 = GameSprite3('line.png', 200, win_height - 480, 0)



walltexture15 = GameSprite2('dirt.png', 400, win_height - 280, 0)
walltexture16 = GameSprite2('dirt.png', 400, win_height - 340, 0)
walltexture17 = GameSprite2('ground.jpg', 200, win_height - 480, 0)
walltexture18 = GameSprite2('ground.jpg', 300, win_height - 480, 0)


game = True
finish = False
clock = time.Clock()
FPS = 60

font.init()
font = font.Font(None, 70)
win = font.render('YOU WIN!', True, (255, 215, 0))
lose = font.render('YOU LOSE!', True, (180, 0, 0))


fly = True

while game:

    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.blit(background, (0, 0))
    
    #if sprite.collide_rect(player, voidl) or sprite.collide_rect(player, voidr) or sprite.collide_rect(player, voidhostle) or sprite.collide_rect(player, voidhostle2):
        #finish = True

 
        player.update()

        player.reset()
        final.reset()
       
        walltexture.reset2()
        walltexture2.reset2()
        line1.reset3()
        line2.reset3()
        line7.reset3()
        line9.reset3()
        line10.reset3()
        line11.reset3()
        line12.reset3()
        line13.reset3()
        line14.reset3()
        line15.reset3()
        line16.reset3()



        voidl.reset2() 
        voidr.reset2()
        walltexture5.reset2()
        voidhostle.reset2()
        voidhostle2.reset2()
        walltexture7.reset2()
        walltexture8.reset2()
        walltexture9.reset2()
        walltexture10.reset2()
        walltexture11.reset2()
        walltexture12.reset2()
        walltexture13.reset2()
        walltexture14.reset2()
        walltexture15.reset2()
        walltexture16.reset2()
        walltexture17.reset2()
        walltexture18.reset2()

    if fly:
        player.rect.y +=3


    if sprite.collide_rect(player, line1) or sprite.collide_rect(player, line2) or sprite.collide_rect(player, line7) or sprite.collide_rect(player, line9) or sprite.collide_rect(player, line10) or sprite.collide_rect(player, line11) or sprite.collide_rect(player, line12) or sprite.collide_rect(player, line13) or sprite.collide_rect(player, line14) or sprite.collide_rect(player, line15) or sprite.collide_rect(player, line16):
        fly = False
    else:
        fly = True




    if sprite.collide_rect(player, final):
        #finish = True
        #window.blit(win, (200, 200))
        background = transform.scale(image.load("cave.png"), (win_width, win_height))
        window.blit(background, (0, 0))
        walltexture = GameSprite2('caveground.png', 0, win_height - 80, 0)
        walltexture2 = GameSprite2('caveground.png', 100, win_height - 80, 0)
        voidl = GameSprite2('lava.png', 200, win_height - 100, 0)
        voidr = GameSprite2('lava.png', 300, win_height - 100, 0)
        walltexture5 = GameSprite2('caveground.png', 400, win_height - 80, 0)
        voidhostle = GameSprite2('lava.png', 200, win_height - 300, 0)
        voidhostle2 = GameSprite2('lava.png',0, win_height - 300, 0)
        walltexture7 = GameSprite2('caveground.png', 600, win_height - 80, 0)
        walltexture8 = GameSprite2('caveground.png', 500, win_height - 80, 0)
        final = GameSprite('caveboss.png', win_width - 80, win_height - 140   , 0)
        walltexture9 = GameSprite2('caveground.png', 500, win_height - 380, 0)
        walltexture10 = GameSprite2('caveground.png', 200, win_height - 260, 0)
        walltexture11 = GameSprite2('caveground.png', 100, win_height - 260, 0)
        walltexture12 = GameSprite2('caveground.png', 300, win_height - 260, 0)
        walltexture13 = GameSprite2('caveground.png', 200, win_height - 460, 0)
        walltexture14 = GameSprite2('caveground.png', 0, win_height - 460, 0)
        walltexture15 = GameSprite2('caveground.png', 500, win_height - 180, 0)
        walltexture16 = GameSprite2('caveground.png', 500, win_height - 280, 0)
        walltexture17 = GameSprite2('caveground.png', 300, win_height - 460, 0)
        walltexture18 = GameSprite2('caveground.png', 400, win_height - 460, 0)
                                                                   
        line1 = GameSprite3('line.png', 0, win_height - 80, 0)
        line2 = GameSprite3('line.png', 100, win_height - 80, 0)
        line7 = GameSprite3('line.png', 400, win_height - 80, 0)
        line9 = GameSprite3 ('line.png', 500, win_height - 380, 0)
        line10 = GameSprite3('line.png', 200, win_height - 260, 0)
        line11 = GameSprite3('line.png', 100, win_height - 260, 0)
        line12 = GameSprite3('line.png', 300, win_height - 260, 0)
        line13 = GameSprite3('line.png', 200, win_height - 460, 0)
        line14 = GameSprite3('line.png', 0, win_height - 460, 0)
        line15 = GameSprite3('line.png', 300, win_height - 460, 0)
        line16 = GameSprite3('line.png', 400, win_height - 460, 0)




    
        walltexture.reset2()
        walltexture8.reset2()

    display.update()
    clock.tick(FPS)