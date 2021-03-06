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
gambar_tower = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "tower.png")), (100,230))
restart = pygame.image.load(os.path.join("Assets", "background_restart.jpg"))

# Assets Musik : 
pygame.mixer.music.stop()
pygame.mixer.music.unload() 
pygame.mixer.music.load(os.path.join("Assets/audio", "game_sound.ogg"))
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

health_berkurang = pygame.mixer.Sound(os.path.join("Assets/audio", "kalah_sound.ogg"))
musuh_terkena = pygame.mixer.Sound(os.path.join("Assets/audio", "mengalahkan_sound.ogg"))
kena = pygame.mixer.Sound(os.path.join("Assets/audio", "hit.ogg"))


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
        if self.cool_down_count >= 12:
            self.cool_down_count = 0
        elif self.cool_down_count > 0:
            self.cool_down_count += 1
    
    #def menembak berfungsi untuk membuat objek dapat menembak dengan keyboard F
    def menembak(self, hit):
        self.kena(hit)
        self.waktu_tunggu_peluru()
        if (InputanPemain[pygame.K_f] and self.cool_down_count == 0):
            kena.play()
            pygame.mixer.Sound.set_volume(kena,0.1)
            peluru = Peluru(self.x, self.y, self.arah())
            self.data_peluru.append(peluru)
            self.cool_down_count = 1
        for peluru in self.data_peluru:
            peluru.gerak_musuh()
            if peluru.keluar_layar():
                self.data_peluru.remove(peluru)
    
    #def kena berfungsi ketika musuh mengenai pemain
    def kena(self, hit):
        for musuh in data_musuh:
            for peluru in self.data_peluru:
                if musuh.hitbox[0] < peluru.x < musuh.hitbox[0] + musuh.hitbox[2] and musuh.hitbox[1] < peluru.y < \
                        musuh.hitbox[1] + musuh.hitbox[3]:
                    musuh.health -= hit
                    musuh_terkena.play()
                    pygame.mixer.Sound.set_volume(musuh_terkena,0.1)
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
    darah_musuh = 30
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.IndexGambar = 0
        # Informasi Health Pada Musuh
        self.hitbox = (self.x, self.y, 64, 64)
        self.health = Musuh.darah_musuh

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
                pygame.mixer.Sound.set_volume(health_berkurang,0.1)
                health_berkurang.play()
                if pemain.health == 0 and pemain.lives > 0:
                    pemain.lives -= 1
                    pygame.mixer.Sound.set_volume(health_berkurang,0.1)
                    health_berkurang.play()
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
    global tower_health
    global speed
    global kills
    global data_musuh
    global pemain
    Layar.fill((0, 0, 0))
    Layar.blit(gambar_background, (0, 0))

    # Menampilkan Pemain, Peluru, Musuh, dan Tower Pada Layar Game : 
    pemain.draw(Layar)
    for peluru in pemain.data_peluru:
        peluru.menampilkan_peluru()
    for musuh in data_musuh:
        musuh.draw(Layar)
    Layar.blit(gambar_tower, (-50, 170))

    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render('Lives: ' + str(pemain.lives) + ' | Tower Health: '+ str(int(tower_health * 100 / 5)) + '% |Kills: '+ str(kills) , True, (35, 255, 0))
    Layar.blit(text, (150, 20))
    
    # Health Pemain : 
    if pemain.alive == False:
        Layar.fill((0, 0, 0))
        Layar.blit(restart, (0, 0))
        font_text = pygame.font.Font('freesansbold.ttf', 20)
        text = font_text.render('Kamu Kalah, Tekan R Untuk Merestart Game!', True, (255, 255, 255))
        font_score = pygame.font.Font('freesansbold.ttf', 38)
        score = font.render(f'Skor Kamu : {kills}', True, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (Lebar_layar // 2, 250)
        Layar.blit(text, textRect)
        scoreRect = score.get_rect(center = (Lebar_layar // 2, 190))
        Layar.blit(score, scoreRect)
        if InputanPemain[pygame.K_r]:
            pemain = Pemain(250,290)
            tower_health = 5
            speed = 2
            Musuh.darah_musuh = 30
            data_musuh = []
            kills = 0
    pygame.time.delay(30)
    pygame.display.update()

# Menambahkan Waktu :
limit_waktu = pygame.USEREVENT + 1
pygame.time.set_timer(limit_waktu, 10000)

# Looping Pada Game : 
musuh_diam = False
hit = 5
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            import main_menu2
            #running = False
        if event.type == limit_waktu:
            print(limit_waktu)
            hit += 2
            Musuh.darah_musuh += 10
            if speed <= 10:
               speed += 1
                
    # InputPemain :
    InputanPemain = pygame.key.get_pressed()

    # Menembak :
    pemain.menembak(hit)

    # GerakanPemain :
    pemain.gerakan_pemain(InputanPemain)
    pemain.lompat_pemain(InputanPemain)

    # Nyawa Tower :
    if tower_health <= 0:
        pemain.alive = False

    # Data Musuh : 
    if tower_health > 0 and pemain.alive:
        if len(data_musuh) == 0:
            musuh = Musuh(750, 300, speed)
            data_musuh.append(musuh)
            musuh_diam = False
        for musuh in data_musuh:
            if not musuh_diam:
                musuh.gerak_musuh()
            if musuh.keluar_layar() or musuh.health <= 0:
                data_musuh.remove(musuh)
            if musuh.x <= 30:
                musuh_diam = True
                tower_health -= 0.01
                health_berkurang.play()
                pygame.mixer.Sound.set_volume(health_berkurang,0.1)
            if musuh.health <= 0:
                kills +=1
            
    layar_game()
