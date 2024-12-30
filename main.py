import pygame
import random

def new_target_place(object_width, object_height):
    x = random.randint(0, SCREEN_WIDTH - object_width)
    y = random.randint(0, SCREEN_HEIGHT - object_height)
    return x, y

pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Игра - Сбей мишень')

pygame.font.init()
font = pygame.font.SysFont('Arial', 36)

icon = pygame.image.load('./img/icon_shoot.png')
pygame.display.set_icon(icon)
target_img = pygame.image.load('./img/target.png')
target_width = 80
target_height = 80
target_x, target_y = new_target_place(target_width, target_height)
boom_img = pygame.image.load('./img/boom.png')

color = (random.randint(0, 255),
         random.randint(0, 255),
         random.randint(0, 255))
times_to_win = 5
count_hit = 0
count_miss = 0
text_color = 'white'


last_move_time = pygame.time.get_ticks()
move_interval = 1000 # В миллисекундах = 1 сек
show_boom = False
boom_start_time = 0
boom_interval = 500

running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if (target_x <= mouse_x <= target_x + target_width and
                target_y <= mouse_y <= target_y + target_height):
                show_boom = True
                boom_start_time = pygame.time.get_ticks()
                count_hit += 1
            else:
                count_miss += 1


    current_time = pygame.time.get_ticks()
    if show_boom:
        screen.blit(boom_img, (target_x, target_y))
        if current_time - boom_start_time >= boom_interval:
            show_boom = False
            target_x, target_y = new_target_place(target_width, target_height)
            last_move_time = pygame.time.get_ticks()
    else:
        if current_time - last_move_time > move_interval:
            target_x, target_y = new_target_place(target_width, target_height)
            last_move_time = current_time

    if not show_boom:
        screen.blit(target_img, (target_x, target_y))

    if count_hit == 0 and count_miss == 0:
        text = f'Привет! Сбей пчелу {times_to_win} раз!'
    else:
        text = f'Попал: {count_hit}, промазал: {count_miss}.'
    text_surface = font.render(text, True, text_color)
    screen.blit(text_surface, (5, 5))

    if count_hit == times_to_win:
        pygame.display.flip()
        pygame.time.delay(5000)
        running = False

    pygame.display.flip()
pygame.quit()