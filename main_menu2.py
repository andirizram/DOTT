import pygame
import pygame_menu

pygame.init()
pygame.display.set_caption('Defense Of The Tower (DOTT) TUBES PBO RB-08')
menu_utama = pygame.display.set_mode((800, 400))


menu = pygame_menu.Menu('Terima Kasih Telah Bermain Game Kami :)', 800, 400,
                       theme = pygame_menu.themes.THEME_SOLARIZED,)


menu.add.button('Keluar', pygame_menu.events.EXIT)

menu.mainloop(menu_utama)