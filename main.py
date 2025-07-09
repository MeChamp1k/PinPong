import pygame

win = pygame.display.set_mode((700, 500))  # Исправлено: добавлены скобки для кортежа
clock = pygame.time.Clock()

win.fill((0, 220, 255))  # Исправлено: добавлены скобки для кортежа цвета

is_game = True
#阿萨的官方太热
while is_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Исправлено: добавлен отступ
            is_game = False
    pygame.display.update()
    clock.tick(40)