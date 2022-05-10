import pygame
import os

# Membuat Layar Program
pygame.init()
Tinggi_Layar = 400
Lebar_layar = 800
Layar = pygame.display.set_mode((Lebar_layar, Tinggi_Layar))

# Memasukkan Gambar Dari Assets Ke Dalam Program
# Assets Pemain : 
arah_kiri_pemain = [pygame.image.load(os.path.join("Assets/pemain", "pemain1L.png")),
        pygame.image.load(os.path.join("Assets/pemain", "pemain2L.png")),
        pygame.image.load(os.path.join("Assets/pemain", "pemain3L.png")),
        pygame.image.load(os.path.join("Assets/pemain", "pemain4L.png")),
        pygame.image.load(os.path.join("Assets/pemain", "pemain5L.png")),
        pygame.image.load(os.path.join("Assets/pemain", "pemain6L.png")),
        pygame.image.load(os.path.join("Assets/pemain", "pemain7L.png")),
        pygame.image.load(os.path.join("Assets/pemain", "pemain8L.png")),
        pygame.image.load(os.path.join("Assets/pemain", "pemain9L.png"))
        ]
arah_kanan_pemain = [pygame.image.load(os.path.join("Assets/pemain", "pemain1R.png")),
        pygame.image.load(os.path.join("Assets/pemain", "pemain2R.png")),
        pygame.image.load(os.path.join("Assets/pemain", "pemain3R.png")),
        pygame.image.load(os.path.join("Assets/pemain", "pemain4R.png")),
        pygame.image.load(os.path.join("Assets/pemain", "pemain5R.png")),
        pygame.image.load(os.path.join("Assets/pemain", "pemain6R.png")),
        pygame.image.load(os.path.join("Assets/pemain", "pemain7R.png")),
        pygame.image.load(os.path.join("Assets/pemain", "pemain8R.png")),
        pygame.image.load(os.path.join("Assets/pemain", "pemain9R.png"))
        ]

# Assets Musuh : 
arah_kiri_musuh = [pygame.image.load(os.path.join("Assets/musuh", "musuh1L.png")),
        pygame.image.load(os.path.join("Assets/musuh", "musuh2L.png")),
        pygame.image.load(os.path.join("Assets/musuh", "musuh3L.png")),
        pygame.image.load(os.path.join("Assets/musuh", "musuh4L.png")),
        pygame.image.load(os.path.join("Assets/musuh", "musuh5L.png")),
        pygame.image.load(os.path.join("Assets/musuh", "musuh6L.png")),
        pygame.image.load(os.path.join("Assets/musuh", "musuh7L.png")),
        pygame.image.load(os.path.join("Assets/musuh", "musuh8L.png")),
        pygame.image.load(os.path.join("Assets/musuh", "musuh9L.png")),
        pygame.image.load(os.path.join("Assets/musuh", "musuh10L.png")),
        pygame.image.load(os.path.join("Assets/musuh", "musuh11L.png"))
        ]
arah_kanan_musuh = [pygame.image.load(os.path.join("Assets/musuh", "musuh1R.png")),
        pygame.image.load(os.path.join("Assets/musuh", "musuh2R.png")),
        pygame.image.load(os.path.join("Assets/musuh", "musuh3R.png")),
        pygame.image.load(os.path.join("Assets/musuh", "musuh4R.png")),
        pygame.image.load(os.path.join("Assets/musuh", "musuh5R.png")),
        pygame.image.load(os.path.join("Assets/musuh", "musuh6R.png")),
        pygame.image.load(os.path.join("Assets/musuh", "musuh7R.png")),
        pygame.image.load(os.path.join("Assets/musuh", "musuh8R.png")),
        pygame.image.load(os.path.join("Assets/musuh", "musuh9R.png")),
        pygame.image.load(os.path.join("Assets/musuh", "musuh10R.png")),
        pygame.image.load(os.path.join("Assets/musuh", "musuh11R.png"))
        ]

# Assets Peluru :
gambar_peluru = pygame.transform.scale(pygame.image.load(os.path.join("Assets/peluru", "frame1.png")), (10, 10))

# Assets Background : 
gambar_background = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "forest.png")), (Lebar_layar, Tinggi_Layar))

# Assets Tower :
gambar_tower = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "tower.png")), (100,200))
