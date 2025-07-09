import pygame

win = pygame.display.set_mode((700, 500))  # Исправлено: добавлены скобки для кортежа
clock = pygame.time.Clock()

win.fill((0, 220, 255))  # Исправлено: добавлены скобки для кортежа цвета


class GameSprite(pygame.sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
       super().__init__()
       self.image = pygame.transform.scale(pygame.image.load(player_image), (wight, height)) #вместе 55,55 - параметры
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y





is_game = True


while is_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Исправлено: добавлен отступ
            is_game = False
    pygame.display.update()
    clock.tick(40)