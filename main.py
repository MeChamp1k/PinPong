import pygame

win = pygame.display.set_mode((600, 500))  # Исправлено: добавлены скобки для кортежа
clock = pygame.time.Clock()

back = ((0, 220, 255))# Исправлено: добавлены скобки для кортежа цвета


class GameSprite(pygame.sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(player_image), (wight, height)) #вместе 55,55 - параметры
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_r(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.y < 345:
            self.rect.y += self.speed
    def update_l(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[pygame.K_s] and self.rect.y < 345:
            self.rect.y += self.speed


racket1 = Player('racket.png', 30, 200, 4, 50, 150)
racket2 = Player('racket.png', 520, 200, 4, 50, 150)
ball = GameSprite('tenis_ball.png', 200, 200, 4, 50, 50)



is_game = True


while is_game:
    win.fill(back)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Исправлено: добавлен отступ
            is_game = False


    ball.rect.x += speed_x
    ball.rect.y += speed_y
    
    if ball.rect.y > 450 or ball.rect.y < 50:
        speed_y *= -1

    if pygame.sprite.collide_rect(racket1, ball) or pygame.sprite.collide_rect(racket2, ball):
        speed_x *= -1


    racket1.update_l()

    racket2.update_r()

    racket1.reset()
    racket2.reset()
    ball.reset()

    
    pygame.display.update()
    clock.tick(40)