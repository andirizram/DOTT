import pygame
import pygame_menu
import os

pygame.init()
pygame.display.set_caption('Defense Of The Tower (DOTT) TUBES PBO RB-08')
pygame.mixer.music.load(os.path.join("Assets/audio", "main_menu.ogg"))
pygame.mixer.music.play(-1)
menu_utama = pygame.display.set_mode((800, 400))


def mulai_game():
    import game

menu = pygame_menu.Menu('Defense Of The Tower', 800, 400,
                       theme=pygame_menu.themes.THEME_ORANGE)

menu.add.button('Mulai', mulai_game)
menu.add.button('Keluar', pygame_menu.events.EXIT)

menu.mainloop(menu_utama)