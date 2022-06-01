import pygame
import pygame_menu
import os

pygame.init()
pygame.display.set_caption('Defense Of The Tower (DOTT) TUBES PBO RB-08')
menu_utama = pygame.display.set_mode((800, 400))
pygame.mixer.music.stop()
pygame.mixer.music.unload()
pygame.mixer.music.load(os.path.join("Assets/audio", "death_sound.ogg"))
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)


menu = pygame_menu.Menu('Terima Kasih Telah Bermain Game Kami :)', 800, 400,
                       theme = pygame_menu.themes.THEME_SOLARIZED,)


menu.add.button('Keluar', pygame_menu.events.EXIT)

menu.mainloop(menu_utama)
