from email.mime import image
import pygame
import random


WIDTH = 800
HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
ORANGE = (255, 255, 0)
RED = (255, 0, 0)

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SHOOTER")
clock = pygame.time.Clock()


def draw_text(surface, texto, size, x, y):
    font = pygame.font.SysFont("serif", size)
    text_surface = font.render(texto, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.center = x, y
    surface.blit(text_surface, text_rect)


def draw_shield_bar(surface, x, y, percentaje):
    BAR_LENGHT= 100
    BAR_HEIGHT = 10
    fill = (percentaje / 100) * BAR_LENGHT
    if 30 < percentaje <= 50 :
        color = ORANGE
    elif percentaje <= 30 :
        color = RED
    else :
        color = GREEN
    border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
    fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surface, color, fill, border_radius= 3)
    pygame.draw.rect(surface, WHITE, border, 2, border_radius= 3)


class Bullet(pygame.sprite.Sprite):

    def __init__(self, x) -> None:
        super().__init__()
        print(x)
        self.image = pygame.image.load(r"assets\laser1.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        #self.rect.x = player.rect.left + player.rect.width // 2 - self.rect.width // 2
        self.rect.centerx = x
        print(self.rect.centerx)
        self.rect.y = player.rect.top

    def update(self):
        self.rect.y += -10
        if self.rect.bottom < 0:
            self.kill()


class Player(pygame.sprite.Sprite):

    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.image.load("assets\player.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH//2
        self.rect.bottom = HEIGHT+10
        self.speed_x = 0
        self.speed_y = 0
        self.shield = 100

    def update(self):
        self.speed_x = 0
        self.speed_y = 0

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.speed_x = -5
        if key[pygame.K_RIGHT]:
            self.speed_x = 5
        if key[pygame.K_UP]:
            self.speed_y = -5
        if key[pygame.K_DOWN]:
            self.speed_y = 5

        # if key[pygame.K_SPACE]:
        #     self.shoot()

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > HEIGHT+10:
            self.rect.bottom = HEIGHT+10
        if self.rect.top < HEIGHT // 2:
            self.rect.top = HEIGHT // 2

    def shoot(self):
        bullet = Bullet(self.rect.centerx)
        all_sprites.add(bullet)
        bullets.add(bullet)
        laser_sound.play()


class Enemigos(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = random.choice(meteoro_img)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-140, -100)
        self.speed_y = random.randrange(1, 5)
        self.speed_x = random.randrange(-4, 4)

    def update(self):
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x

        if self.rect.top > HEIGHT + 10 or self.rect.right < 0 or self.rect.left > WIDTH + 10:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-140, -100)
            self.speed_y = random.randrange(1, 5)
            self.speed_x = random.randrange(-4, 4)


class Explosion(pygame.sprite.Sprite):
    
    def __init__(self, center) -> None:
        super().__init__()
        self.image = explosion_anim[0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_anim):
                self.kill()
            else :
                center = self.rect.center
                self.image = explosion_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

meteoro_img = []
path_img = ["assets/meteorGrey_big1.png", "assets/meteorGrey_big2.png", "assets/meteorGrey_big3.png", "assets/meteorGrey_big4.png",
            "assets/meteorGrey_med1.png", "assets/meteorGrey_med2.png", "assets/meteorGrey_small1.png", "assets/meteorGrey_small2.png",
            "assets/meteorGrey_tiny1.png", "assets/meteorGrey_tiny2.png"]

for img in path_img:
    meteoro_img.append(pygame.image.load(img).convert())

# fondo
background = pygame.image.load(r"assets\background.png").convert()

#EXPLOSIONES IMAGENES
explosion_anim = []
for i in range(9) :
    file = r"assets\regularExplosion0{}.png".format(i)
    img = pygame.image.load(file).convert()
    img.set_colorkey(BLACK)
    img_scale = pygame.transform.scale(img, (70, 70))
    explosion_anim.append(img_scale)


# cargar sonidos
laser_sound = pygame.mixer.Sound(r"assets\assets_laser5.ogg")
explosion_sound = pygame.mixer.Sound(r"assets\assets_explosion.wav")
pygame.mixer.music.load(r"assets\assets_music.ogg")
pygame.mixer.music.set_volume(0.6)
pygame.mixer.music.play(loops=-1)

'-----------------------------------------  '
all_sprites = pygame.sprite.Group()
list_enemigos = pygame.sprite.Group()
bullets = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

for i in range(15):
    meteoro = Enemigos()
    all_sprites.add(meteoro)
    list_enemigos.add(meteoro)


running = True
score = 0

while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    all_sprites.update()

    hits = pygame.sprite.groupcollide(list_enemigos, bullets, True, True)
    for hit in hits:
        score += 10
        meteoro = Enemigos()
        all_sprites.add(meteoro)
        list_enemigos.add(meteoro)
        explosion = Explosion(hit.rect.center)
        all_sprites.add(explosion)
        explosion_sound.play()

    hits = pygame.sprite.spritecollide(player, list_enemigos, True)
    if hits:
        player.shield -= 10
        meteoro = Enemigos()
        all_sprites.add(meteoro)
        list_enemigos.add(meteoro)
        if player.shield <= 0 :
            running = 0
        

    screen.blit(background, [0, 0])
    all_sprites.draw(screen)

    draw_text(screen, str(score), 25, WIDTH//2, 40)
    draw_shield_bar(screen, 5, 5, player.shield)

    pygame.display.flip()


pygame.quit()
