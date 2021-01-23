import pygame
from pygame.sprite import Group

import game_functions as gf
from game_stats import GameStats
from settings import Settings
from ship import Ship


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    ship = Ship(settings, screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    aliens = Group()
    # 设置背景色
    pygame.display.set_caption("Alien Invasion")
    gf.create_fleet(settings, screen, aliens, ship)
    stats = GameStats(settings)

    # 开始游戏的主循环
    while True:
        gf.check_events(settings, screen, ship, bullets)
        bullets.update()
        ship.update()
        gf.update_bullets(settings, screen, ship, aliens, bullets)
        gf.update_aliens(settings, stats, screen, bullets, aliens, ship)
        gf.update_screen(screen, settings, ship, bullets, aliens)


run_game()
