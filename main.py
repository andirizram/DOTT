import pygame
import os

# Membuat Layar Program
pygame.init()
pygame.display.set_caption('Defense Of The Tower (DOTT) TUBES PBO RB-08')
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

#assets suara Peluru
pop = pygame.mixer.Sound('pop.ogg')

#Kelas Pemain
class Pemain:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velx = 10
        self.vely = 6
        self.kanan = True
        self.kiri = False
        self.IndexGambar = 0
        self.lompat = False
        self.data_peluru = []
        self.cool_down_count = 0
        # Informasi Health Pada Pemain
        self.hitbox = (self.x, self.y, 64, 64)
        self.health = 30
        self.lives = 1
        self.alive = True
        
    #def gerakan pemain berfungsi untuk membuat objek pemain dapat bergerak dengan keyboard arrow kanan dan kiri
    def gerakan_pemain(self, InputanPemain):
        if InputanPemain[pygame.K_RIGHT] and self.x <= Lebar_layar - 62:
            self.x += self.velx
            self.kanan = True
            self.kiri = False
        elif InputanPemain[pygame.K_LEFT] and self.x >= 0:
            self.x -= self.velx
            self.kanan = False
            self.kiri = True
        else:
            self.IndexGambar = 0
    
    #def draw berfungsi penentu dari gambar objek pemain yang akan ditampilkan 
    def draw(self, Layar):
        self.hitbox = (self.x + 15, self.y + 15, 30, 40)
        pygame.draw.rect(Layar, (255, 0, 0), (self.x + 15, self.y, 30, 10))
        if self.health >= 0:
            pygame.draw.rect(Layar, (0, 255, 0), (self.x + 15, self.y, self.health, 10))
        if self.IndexGambar >= 9:
            self.IndexGambar = 0
        if self.kiri:
            Layar.blit(arah_kiri_pemain[self.IndexGambar], (self.x, self.y))
            self.IndexGambar += 1
        if self.kanan:
            Layar.blit(arah_kanan_pemain[self.IndexGambar], (self.x, self.y))
            self.IndexGambar += 1
    
    #def lompat pemain berfungsi untuk membuat objek pemain dapat melompat dengan menekan keyboard space
    def lompat_pemain(self, InputanPemain):
        if InputanPemain[pygame.K_SPACE] and self.lompat is False:
            self.lompat = True
        if self.lompat:
            self.y -= self.vely * 4
            self.vely -= 1
        if self.vely < -6:
            self.lompat = False
            self.vely = 6
    
    #def arah berfungsi sebagai arah objek pemain 
    def arah(self):
        if self.kanan:
            return 1
        if self.kiri:
            return -1
    
    #def waktu tunggu peluru berfungsi sebagai cooldown dari keluarnya peluru
    def waktu_tunggu_peluru(self):
        if self.cool_down_count >= 20:
            self.cool_down_count = 0
        elif self.cool_down_count > 0:
            self.cool_down_count += 1
    
    #def menembak berfungsi untuk membuat objek dapat menembak dengan keyboard F
    def menembak(self):
        self.kena()
        self.waktu_tunggu_peluru()
        if (InputanPemain[pygame.K_f] and self.cool_down_count == 0):
            pop.play()
            peluru = Peluru(self.x, self.y, self.arah())
            self.data_peluru.append(peluru)
            self.cool_down_count = 1
        for peluru in self.data_peluru:
            peluru.gerak_musuh()
            if peluru.keluar_layar():
                self.data_peluru.remove(peluru)
    
    #def kena berfungsi ketika musuh mengenai pemain
    def kena(self):
        for musuh in data_musuh:
            for peluru in self.data_peluru:
                if musuh.hitbox[0] < peluru.x < musuh.hitbox[0] + musuh.hitbox[2] and musuh.hitbox[1] < peluru.y < \
                        musuh.hitbox[1] + musuh.hitbox[3]:
                    musuh.health -= 5
                    pemain.data_peluru.remove(peluru)

#Kelas Peluru
class Peluru:
    def __init__(self, x, y, direction):
        self.x = x + 15
        self.y = y + 25
        self.direction = direction

    def menampilkan_peluru(self):
        Layar.blit(gambar_peluru, (self.x, self.y))

    def gerak_musuh(self):
        if self.direction == 1:
            self.x += 15
        if self.direction == -1:
            self.x -= 15

    def keluar_layar(self):
        return not (self.x >= 0 and self.x <= Lebar_layar)

#Kelas musuh :
class Musuh:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.IndexGambar = 0
        # Informasi Health Pada Musuh
        self.hitbox = (self.x, self.y, 64, 64)
        self.health = 30

    def langkah_musuh(self): 
        if self.IndexGambar >= 33:
            self.IndexGambar = 0

    def draw(self, Layar):
        self.hitbox = (self.x + 20, self.y + 10, 30, 45)
        pygame.draw.rect(Layar, (255, 0, 0), (self.x + 15, self.y, 30, 10))
        if self.health >= 0:
            pygame.draw.rect(Layar, (0, 255, 0), (self.x + 15, self.y, self.health, 10))
        self.langkah_musuh()
        Layar.blit(arah_kiri_musuh[self.IndexGambar // 3], (self.x, self.y))
        self.IndexGambar += 1

    def gerak_musuh(self):
        self.kena()
        self.x -= speed

    def kena(self): 
        if pemain.hitbox[0] < musuh.x + 32 < pemain.hitbox[0] + pemain.hitbox[2] and pemain.hitbox[1] < musuh.y + 32 < \
                pemain.hitbox[1] + pemain.hitbox[3]:
            if pemain.health > 0:
                pemain.health -= 1
                if pemain.health == 0 and pemain.lives > 0:
                    pemain.lives -= 1
                    pemain.health = 30
                elif pemain.health == 0 and pemain.lives == 0:
                    pemain.alive = False

    def keluar_layar(self):
        return not (self.x >= -50 and self.x <= Lebar_layar + 50)

# Proses Utama Game : 
# Instansiasi Dari Pemain, Musuh, dan Tower : 
pemain = Pemain(250, 290)
data_musuh = []
speed = 2
kills = 0
tower_health = 5

def layar_game():
    Layar.fill((0, 0, 0))
    Layar.blit(gambar_background, (0, 0))

    # Menampilkan Pemain, Peluru, Musuh, dan Tower Pada Layar Game : 
    pemain.draw(Layar)
    for peluru in pemain.data_peluru:
        peluru.menampilkan_peluru()
    for musuh in data_musuh:
        musuh.draw(Layar)
    Layar.blit(gambar_tower, (-50, 170))

    # Health Pemain : 
    if pemain.alive == False:
        Layar.fill((0, 0, 0))
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render('Kamu Kalah, Tekan R Untuk Merestart Game!', True, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (Lebar_layar // 2, Tinggi_Layar // 2)
        Layar.blit(text, textRect)
        if InputanPemain[pygame.K_r]:
            pemain.alive = True
            pemain.lives = 1
            pemain.health = 30
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render('Lives: ' + str(pemain.lives) + ' | Tower Health: '+ str(tower_health) + ' |Kills: '+ str(kills), True, (35, 255, 0))
    Layar.blit(text, (150, 20))
    pygame.time.delay(30)
    pygame.display.update()

# Looping Pada Game : 
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # InputPemain :
    InputanPemain = pygame.key.get_pressed()

    # Menembak :
    pemain.menembak()

    # GerakanPemain :
    pemain.gerakan_pemain(InputanPemain)
    pemain.lompat_pemain(InputanPemain)

    # Data Musuh : 
    if len(data_musuh) == 0:
        musuh = Musuh(750, 300, speed)
        data_musuh.append(musuh)
        if speed <= 10:
            speed += 1
    for musuh in data_musuh:
        musuh.gerak_musuh()
        if musuh.keluar_layar() or musuh.health == 0:
            data_musuh.remove(musuh)
        if musuh.x < 50:
            data_musuh.remove(musuh)
            tower_health -= 1
        if musuh.health == 0:
            kills +=1
            
    layar_game()
