import sys

import pygame


def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # 向右移动飞船
                ship.right = True
            elif event.key == pygame.K_LEFT:
                ship.left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.right = False
            elif event.key == pygame.K_LEFT:
                ship.left = False

def update_screen(screen, settings, ship):
    screen.fill(settings.bg_color)
    ship.blitme()
    pygame.display.flip()
