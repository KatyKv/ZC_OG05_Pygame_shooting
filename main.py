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

icon = pygame.image.load('./img/icon_shoot.png')
pygame.display.set_icon(icon)
target_img = pygame.image.load('./img/target.png')
target_width = 80
target_height = 80
target_x, target_y = new_target_place(target_width, target_height)
color = (random.randint(0, 255),
         random.randint(0, 255),
         random.randint(0, 255))

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
                target_x, target_y = new_target_place(target_width, target_height)


    screen.blit(target_img, (target_x, target_y))




    pygame.display.update()
pygame.quit()