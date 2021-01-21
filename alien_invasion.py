import pygame

import game_functions as gf
from settings import Settings
from ship import Ship


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    ship = Ship(settings, screen)
    # 设置背景色
    pygame.display.set_caption("Alien Invasion")

    # 开始游戏的主循环
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(screen, settings, ship)


run_game()
