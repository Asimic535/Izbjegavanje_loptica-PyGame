import pygame
import sys
import random
import time
from datetime import datetime
from math import *
pygame.init()
pygame.mixer.init()


def pocetno_log():      # Početna linija log.txt dokumenta, čisto radi estetike
    file = open("Datoteke/log.txt", "a")
    tekst = "\n\n================================================"
    file.write(tekst)
    file.close()


def background_zvuk():
    BACKGROUND_ZVUK.play()


pocetno_log()

sirina = 854
visina = 480
zaslon = pygame.display.set_mode((sirina, visina))
pygame.display.set_caption("Smirujuća igrica v1.5")
clock = pygame.time.Clock()

SOUND_PICKUP = pygame.mixer.Sound("Datoteke/pickupsound.mp3")
BACKGROUND_ZVUK = pygame.mixer.Sound("Datoteke/background_zvuk_madarski_ples.mp3")

SOUND_IZGUBIO1 = pygame.mixer.Sound("Datoteke/Game over soundovi/awwww.mp3")
SOUND_IZGUBIO2 = pygame.mixer.Sound("Datoteke/Game over soundovi/aj_ramo.mp3")
SOUND_IZGUBIO3 = pygame.mixer.Sound("Datoteke/Game over soundovi/badam_bammm.mp3")
SOUND_IZGUBIO4 = pygame.mixer.Sound("Datoteke/Game over soundovi/cricket.mp3")
SOUND_IZGUBIO5 = pygame.mixer.Sound("Datoteke/Game over soundovi/directed_by.mp3")
SOUND_IZGUBIO6 = pygame.mixer.Sound("Datoteke/Game over soundovi/emotional-damage-meme.mp3")
SOUND_IZGUBIO7 = pygame.mixer.Sound("Datoteke/Game over soundovi/gta_wasted.mp3")
SOUND_IZGUBIO8 = pygame.mixer.Sound("Datoteke/Game over soundovi/galaxy-meme.mp3")
SOUND_IZGUBIO9 = pygame.mixer.Sound("Datoteke/Game over soundovi/gta_cj_here_we_go_again.mp3")
SOUND_IZGUBIO10 = pygame.mixer.Sound("Datoteke/Game over soundovi/helicopterr.mp3")
SOUND_IZGUBIO11 = pygame.mixer.Sound("Datoteke/Game over soundovi/hellodarknessmyoldfriend.mp3")
SOUND_IZGUBIO12 = pygame.mixer.Sound("Datoteke/Game over soundovi/it_was_at_this_moment.mp3")
SOUND_IZGUBIO13 = pygame.mixer.Sound("Datoteke/Game over soundovi/look_at_this_dude_smjeh.mp3")
SOUND_IZGUBIO14 = pygame.mixer.Sound("Datoteke/Game over soundovi/mission_failed_well_get_him_next_time.mp3")
SOUND_IZGUBIO15 = pygame.mixer.Sound("Datoteke/Game over soundovi/nema-ovde-zivota.mp3")
SOUND_IZGUBIO16 = pygame.mixer.Sound("Datoteke/Game over soundovi/oh-no-no-no-no-laugh.mp3")
SOUND_IZGUBIO17 = pygame.mixer.Sound("Datoteke/Game over soundovi/phub-x-see-you-again.mp3")
SOUND_IZGUBIO18 = pygame.mixer.Sound("Datoteke/Game over soundovi/reeeeeeeee.mp3")
SOUND_IZGUBIO19 = pygame.mixer.Sound("Datoteke/Game over soundovi/romanceeeeeeeeeeeeee.mp3")
SOUND_IZGUBIO20 = pygame.mixer.Sound("Datoteke/Game over soundovi/sadtrombone.mp3")
SOUND_IZGUBIO21 = pygame.mixer.Sound("Datoteke/Game over soundovi/sad_violin.mp3")
SOUND_IZGUBIO22 = pygame.mixer.Sound("Datoteke/Game over soundovi/sirene-gemidao.mp3")
SOUND_IZGUBIO23 = pygame.mixer.Sound("Datoteke/Game over soundovi/titanic-flute.mp3")
SOUND_IZGUBIO24 = pygame.mixer.Sound("Datoteke/Game over soundovi/the-weeknd-rizzz.mp3")
SOUND_IZGUBIO25 = pygame.mixer.Sound("Datoteke/Game over soundovi/they_ask_you_how_are_you.mp3")
SOUND_IZGUBIO26 = pygame.mixer.Sound("Datoteke/Game over soundovi/user_disconnected.mp3")
SOUND_IZGUBIO27 = pygame.mixer.Sound("Datoteke/Game over soundovi/windows-10-error-sound.mp3")
SOUND_IZGUBIO28 = pygame.mixer.Sound("Datoteke/Game over soundovi/wut.mp3")
SOUND_IZGUBIO29 = pygame.mixer.Sound("Datoteke/Game over soundovi/wah-wah-wah_wahhhhh.mp3")
SOUND_IZGUBIO30 = pygame.mixer.Sound("Datoteke/Game over soundovi/winXP_shutdownmp3.mp3")

SOUNDOVI = [SOUND_IZGUBIO1, SOUND_IZGUBIO2, SOUND_IZGUBIO3, SOUND_IZGUBIO4, SOUND_IZGUBIO5,
            SOUND_IZGUBIO6, SOUND_IZGUBIO7, SOUND_IZGUBIO8, SOUND_IZGUBIO9, SOUND_IZGUBIO10,
            SOUND_IZGUBIO11, SOUND_IZGUBIO12, SOUND_IZGUBIO13, SOUND_IZGUBIO14, SOUND_IZGUBIO15,
            SOUND_IZGUBIO16, SOUND_IZGUBIO17, SOUND_IZGUBIO18, SOUND_IZGUBIO19, SOUND_IZGUBIO20,
            SOUND_IZGUBIO21, SOUND_IZGUBIO22, SOUND_IZGUBIO23, SOUND_IZGUBIO24, SOUND_IZGUBIO25,
            SOUND_IZGUBIO26, SOUND_IZGUBIO27, SOUND_IZGUBIO28, SOUND_IZGUBIO29, SOUND_IZGUBIO30]

pozadina = (51, 51, 51)
SKALA = pygame.transform.scale(pygame.image.load("Datoteke/skala.png"), (50, visina * 0.8))
skala = SKALA
R = random.randint(0, 255)
G = random.randint(0, 255)
B = random.randint(0, 255)
boja_igraca = (R, G, B)

crvena = (203, 67, 53)
zuta = (241, 196, 15)
plava = (46, 134, 193)
zelena = (34, 153, 84)
ljubicasta = (136, 78, 160)
narancasta = (214, 137, 16)

boje = [crvena, zuta, plava, zelena, ljubicasta, narancasta]

poeni = 0


class Lopta:                # --- Klasa koja definira loptice ---
    def __init__(self, radius, brzina):
        self.x = 0
        self.y = 0
        self.r = radius
        self.color = 0
        self.speed = brzina
        self.angle = 0

    def pravljenje_lopti(self):             # Stvaranje loptice, nasumicna boja iz liste "boje", nasumicni kut upada.
        self.x = sirina / 2 - self.r
        self.y = visina / 2 - self.r
        self.color = random.choice(boje)
        self.angle = random.randint(-180, 180)

    def kretanje_lopti(self):               # Definirani kutevi odbijanja loptica od granica
        self.x += self.speed * cos(radians(self.angle))
        self.y += self.speed * sin(radians(self.angle))

        if self.x < self.r or self.x + self.r > sirina:
            self.angle = 180 - self.angle
        if self.y < self.r or self.y + self.r > visina:
            self.angle *= -1

    def draw(self):
        pygame.draw.ellipse(zaslon, self.color, (self.x - self.r, self.y - self.r, self.r * 2, self.r * 2))

    def sudaranja(self, radius):            # Provjerava sudaranja igrača i bilo koje druge loptice
        pozicija_misa = pygame.mouse.get_pos()
        udaljenost = ((pozicija_misa[0] - self.x) ** 2 + (pozicija_misa[1] - self.y) ** 2) ** 0.5
        if udaljenost <= self.r + radius:   # Koordinate miša + radius loptice = granica igrača
            logfile_progres()               # Zapisiva rezultat u "log.txt" datoteku
            BACKGROUND_ZVUK.stop()          # Gasi instrumental u pozadini
            zvuk_za_kraj()                  # Pušta SOUND kada igrač izgubi, čeka dok SOUND završi onda ide dalje
            ugasi()                         # Zatim gasi loop


class Meta:                 # --- Klasa koja definira mete - kvadratici koji daju poene ---
    def __init__(self):
        self.x = 0
        self.y = 0
        self.w = 20
        self.h = self.w

    def generiraj_nove_koordinate_mete(self):   # Definira mjesto stvaranja novog kvadratica/poena
        self.x = random.randint(self.w, sirina - self.w)
        self.y = random.randint(self.h, visina - self.h)

    def draw(self):                             # Definira boju novog kvadratica/poena
        boja = boje[random.randint(0, 5)]
        pygame.draw.rect(zaslon, boja, (self.x, self.y, self.w, self.h))


def ispisi_pocetni_meni():          # Pocetni meni
    zaslon.fill((20, 170, 165))      # Boja pozadine
    font = pygame.font.SysFont("Comicsans", 60, True)
    tekst = font.render("Glavni izbornik", True, (210, 210, 210))
    zaslon.blit(tekst, (sirina//2 - tekst.get_width()//2, visina * 0.07))
    ispisi_pokreni_igru()           # Ispisiva dugme "Pokreni igru"
    ispisi_izlaz()                  # Ispisiva dugme "Izlaz"
    ispisi_autora_i_verziju()       # Ispisiva autora i verziju u kutevima


def ispisi_pokreni_igru():
    font = pygame.font.SysFont("Comicsans", 46, True)
    tekst_pokreni_igru = font.render("Pokreni igru", True, (20, 20, 180))
    zaslon.blit(tekst_pokreni_igru, (sirina // 2 - tekst_pokreni_igru.get_width() // 2, visina * 0.4))


def ispisi_izlaz():
    font = pygame.font.SysFont("Comicsans", 40, True)
    tekst = font.render("Izlaz", True, crvena)
    zaslon.blit(tekst, (sirina // 2 - tekst.get_width() // 2, visina * 0.6))


def ispisi_autora_i_verziju():                                   # Ispisiva autora dole desno i verziju dole lijevo
    font = pygame.font.SysFont("Comicsans", 18, True)
    tekst_autor = font.render("by Ante Šimić", True, (230, 230, 230))
    zaslon.blit(tekst_autor, (sirina * 0.992 - tekst_autor.get_width(), visina * 0.94))
    tekst_verzija = font.render("Verzija: 1.4", True, (230, 230, 230))
    zaslon.blit(tekst_verzija, (sirina * 0.009, visina * 0.94))


def glavni_meni():
    klik = False

    while True:
        ispisi_pocetni_meni()
        mx, my = pygame.mouse.get_pos()

        dugme_pokreni_igru = pygame.Rect(sirina//2 - 150, visina * 0.42, 300, 60)  # Tehnicki Rect koji je preko teksta
        dugme_izlaz = pygame.Rect(sirina//2 - 100, visina * 0.65, 200, 50)  # "Izlaz" i "Pi", ali nije blit-an na ekran
        if dugme_pokreni_igru.collidepoint((mx, my)):
            if klik:
                glavni_loop()
                background_zvuk()
        if dugme_izlaz.collidepoint((mx, my)):
            if klik:
                logfile_close()
                pygame.quit()
                sys.exit()

        klik = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                logfile_close()
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    logfile_close()
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    klik = True

        pygame.display.update()
        clock.tick(60)


def ugasi():    # Glavna petlja igrice
    loop = True     # Kada True -> igrica radi, Kada False -> igrica se gasi

    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:       # Kad se stisne crveni X, igrica se gasi
                logfile_close()                 # Ispisiva u log.txt da je igrica ugasena
                ugasi_igricu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:     # Kad se stisne "Q" na tipkovnici, igrica se gasi
                    logfile_close()             # Ispisiva u log.txt da je igrica ugasena
                    ugasi_igricu()
                if event.key == pygame.K_r:     # Kad se stisne "R" na tipkovnici, igrica se resetira
                    logfile_restart()           # Ispisiva u log.txt da je igrica ponovno pokrenuta
                    background_zvuk()
                    glavni_loop()
                if event.key == pygame.K_g:     # Kad se stisne "G", vraca se na Glavni Meni
                    glavni_meni()

        zaslon.fill(pozadina)                   # Prikaz pozadine na zaslon

        prikazi_uspjeh()                        # Prikaz poena u gornjem desnom kutu
        prikazi_rank()
        prikazi_skalu()
        novi_hiscore()

        pygame.display.update()                 # Osvjezavanje zaslona
        clock.tick()                            # Ferkfencija osvjezavanja zaslona


def logfile_progres():
    file = open("Datoteke/log.txt", "a")
    sada = datetime.now()
    vrime = sada.strftime("%d/%m/%Y %H:%M:%S")
    tekst = "\n" + vrime + " Izgubili ste na: " + str(poeni) + "% igrice!"
    file.write(tekst)
    file.close()


def logfile_restart():
    file = open("Datoteke/log.txt", "a")
    tekst = "\n Igrica ponovno pokrenuta..."
    file.write(tekst)
    file.close()


def logfile_close():
    file = open("Datoteke/log.txt", "a")
    tekst = "\nIgrica je ugašena.==============================\n================================================"
    file.write(tekst)
    file.close()


def provjeri_sudaranja(meta, d, obj_meta):          # Provjerava sudaranja
    pozicija_misa = pygame.mouse.get_pos()
    udaljenost = ((pozicija_misa[0] - meta[0] - obj_meta.w) ** 2 +
                  (pozicija_misa[1] - meta[1] - obj_meta.h) ** 2) ** 0.5

    if udaljenost <= d + obj_meta.w:
        return True
    return False


def prikaz_igraca(pozicija_misa, r):     # Prikaz igracevog kruga na zaslon
    pygame.draw.ellipse(zaslon, boja_igraca, (pozicija_misa[0] - r, pozicija_misa[1] - r, 2 * r, 2 * r))


def ugasi_igricu():     # Prekida sve i izlazi iz igrice
    pygame.quit()
    sys.exit()


def prikazi_upute():    # Prikaz uputa u gornjem lijevom kutu
    font = pygame.font.SysFont("Comicsans", 15)
    prikaz_uputa = font.render("Kretanje : MIŠ", True, (230, 230, 230))
    prikaz_uputa1 = font.render("Restart: R", True, (230, 230, 230))
    prikaz_uputa2 = font.render("Izlaz: Q", True, (230, 230, 230))
    zaslon.blit(prikaz_uputa, (10, 5))
    zaslon.blit(prikaz_uputa1, (10, 25))
    zaslon.blit(prikaz_uputa2, (10, 45))


def prikazi_uspjeh():   # Prikaz postotka uspjeha na dnu na kraju runde
    font = pygame.font.SysFont("Comicsans", 30)
    uspjeh = poeni
    file = open("Datoteke/HiSc.txt", "r")  # Cita HiScore iz datoteke
    hi_score = file.read()  # Sprema u varijablu
    file.close()  # Zatvara file
    prikaz = font.render(f"| Uspjeh: {uspjeh}% |  | HiScore: {hi_score}% |", True, (230, 230, 230))
    zaslon.blit(prikaz, (sirina//2 - prikaz.get_width()//2, visina * 0.87))


def prikazi_rezultat():     # Prikaz rezultata na zaslon
    font = pygame.font.SysFont("Forte", 30)                                     # Odabir fonta i velicine fonta
    prikaz_poena = font.render("Score: " + str(poeni), True, (230, 230, 230))   # Prikaz teksta na zaslon u boji(x,x,x)
    zaslon.blit(prikaz_poena, (sirina//2 - prikaz_poena.get_width()//2, visina * 0.9))    # Lokacija prikaza teksta


def prikazi_skalu():    # Prikaz ljestvice u bojama sa lijeve i desne strane
    zaslon.blit(skala, (sirina * 0.1 - skala.get_width() // 2, visina // 2 - skala.get_height() // 2))
    zaslon.blit(skala, (sirina * 0.9 - skala.get_width() // 2, visina // 2 - skala.get_height() // 2))


def prikazi_rank():     # Prikaz ranka u bojama po ljestvici nakon sudara
    font_manji = pygame.font.SysFont("Comicsans", 25)
    font = pygame.font.SysFont("Comicsans", 40)
    font_veci = pygame.font.SysFont("Comicsans", 60)

    if poeni < 1:                        # Do 1 poena -- NE ZNA KO MU GLAVU NOSI
        rank = "ZNAŠ LI DI ĆEŠ?"
        rank_obojen = font_veci.render(rank, True, (10, 100, 10))
        zaslon.blit(rank_obojen, (sirina // 2 - rank_obojen.get_width() // 2, visina * 0.27))

    elif poeni < 20:                      # Do 20 poena -- NIKO I NISTA
        rank = "NIKO I NIŠTA"
        rank_obojen = font_veci.render(rank, True, (79, 186, 29))
        zaslon.blit(rank_obojen, (sirina // 2 - rank_obojen.get_width() // 2, visina * 0.27))

    elif poeni >= 20 and poeni < 40:      # Do 40 poena -- OUTSIDER
        rank = "OUTSIDER"
        rank_obojen = font_veci.render(rank, True, (141, 223, 0))
        zaslon.blit(rank_obojen, (sirina // 2 - rank_obojen.get_width() // 2, visina * 0.27))
    elif poeni >= 40 and poeni < 55:      # Do 55 poena -- AMATER
        rank = "AMATER"
        rank_obojen = font_veci.render(rank, True, (182, 221, 21))
        zaslon.blit(rank_obojen, (sirina // 2 - rank_obojen.get_width() // 2, visina * 0.27))

    elif poeni >= 55 and poeni < 70:      # Do 70 poena -- UVJEZBAN
        rank = "UVJEZBAN"
        rank_obojen = font_veci.render(rank, True, (253, 209, 1))
        zaslon.blit(rank_obojen, (sirina // 2 - rank_obojen.get_width() // 2, visina * 0.27))

    elif poeni >= 70 and poeni < 85:      # Do 85 poena -- PROFI
        rank = "PROFI"
        rank_obojen = font_veci.render(rank, True, (255, 134, 0))
        zaslon.blit(rank_obojen, (sirina // 2 - rank_obojen.get_width() // 2, visina * 0.27))

    elif poeni >= 85 and poeni < 99:      # Do 99 poena -- MASTER
        rank = "MASTER"
        rank_obojen = font_veci.render(rank, True, (238, 38, 1))
        zaslon.blit(rank_obojen, (sirina // 2 - rank_obojen.get_width() // 2, visina * 0.27))

    elif poeni >= 100:                     # 100+ poena -- OP
        rank = "OP"
        rank_obojen = font_veci.render(rank, True, (255, 0, 0))
        zaslon.blit(rank_obojen, (sirina // 2 - rank_obojen.get_width() // 2, visina * 0.27))

    prikaz_ranka = font.render("Tvoj rank:", True, (230, 230, 230))
    zaslon.blit(prikaz_ranka, (sirina // 2 - prikaz_ranka.get_width() // 2, visina * 0.08))

    glavni_meni_tekst = font_manji.render("Glavni meni: G", True, (230, 230, 230))
    restart_tekst = font_manji.render("Restart: R", True, (230, 230, 230))
    izlaz_tekst = font_manji.render("Izlaz: Q", True, (230, 230, 230))

    zaslon.blit(glavni_meni_tekst, (sirina // 2 - glavni_meni_tekst.get_width() // 2, visina * 0.52))
    zaslon.blit(restart_tekst, (sirina // 2 - restart_tekst.get_width() // 2, visina * 0.6))
    zaslon.blit(izlaz_tekst, (sirina // 2 - izlaz_tekst.get_width() // 2, visina * 0.68))


def novi_hiscore():
    file = open("Datoteke/HiSc.txt", "r")
    hi_score = file.read()
    file.close()
    if poeni > int(hi_score):
        file = open("Datoteke/HiSc.txt", "w")
        file.write(str(poeni))
        file.close()

        file = open("Datoteke/log.txt", "a")
        sada = datetime.now()
        vrime = sada.strftime("%d/%m/%Y %H:%M:%S")
        tekst = "\n" + vrime + " Novi najbolji rezultat: " + str(poeni) + "%!"
        file.write(tekst)
        file.close()
    else:
        pass


def zvuk_za_kraj():             # Pušta zvuk kada igrac izgubi
    broj_sounda = random.randint(0, 29)                         # Redni broj 0-29 -> sprema u varijablu
    sound_za_play = SOUNDOVI[broj_sounda]                       # Iz liste SOUNDOVI uzimamo SOUND pod random indeksom
    duzina_sounda = sound_za_play.get_length()                  # Trazimo duzinu odabranog SOUND-a pomocu .get_length()
    sound_za_play.play()                                        # Pouštamo odabrani SOUND
    time.sleep(duzina_sounda)                                   # Pauziramo igricu za duzinu SOUND-a koji pustamo


def glavni_loop():  # Glavna petlja igranja
    background_zvuk()

    global poeni    # Poeni globalna varijabla
    poeni = 0

    loop = True

    pradius = 10

    loptice = []        # Lista svih aktivnih smetajućih loptica

    for i in range(1):  # Prva smetajuća loptica
        nova_loptica = Lopta(pradius + 2, 5)
        nova_loptica.pravljenje_lopti()
        loptice.append(nova_loptica)

    meta = Meta()
    meta.generiraj_nove_koordinate_mete()

    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:       # Kad se stisne crveni X, igrica se gasi
                logfile_close()
                ugasi_igricu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:     # Kad se upre "Q", igrica se gasi
                    logfile_close()             # Ispisiva u log.txt da je igrica ugasena
                    ugasi_igricu()
                if event.key == pygame.K_r:     # Kad se upre "R", skor i igrica se resetiraju
                    logfile_restart()           # Ispisiva u log.txt da je igrica ponovno pokrenuta
                    background_zvuk()
                    glavni_loop()
                if event.key == pygame.K_g:     # Kad se upre "G", vraca se na Glavni Meni
                    glavni_meni()

        zaslon.fill(pozadina)                   # Prikaz pozadine
        prikazi_upute()

        for i in range(len(loptice)):           # Za svaku lopticu primjenjena funkcija "kretanje_lopti()"
            loptice[i].kretanje_lopti()         # Za detalje funkcije: --linija 44--

        for i in range(len(loptice)):           # Za svaku logicku lopticu zapravo stvara krug na ekranu
            loptice[i].draw()                   # Za detalje funkcije: --linija 53--

        for i in range(len(loptice)):           # Za svaku lopticu provjerava je li se dira s igračevom lopticom
            loptice[i].sudaranja(pradius)       # Za detalje funkcije: --linija 56--

        pozicija_igraca = pygame.mouse.get_pos()                            # U varijablu sprema gdje se nalazi miš
        prikaz_igraca((pozicija_igraca[0], pozicija_igraca[1]), pradius)    # Oko miša crta krug promjera "pradius"

        collide = provjeri_sudaranja((meta.x, meta.y), pradius, meta)       # Provjerava je li igrač naišao na poen

        if collide:                                     # Ako je, dodaj poen, generiraj novu metu
            poeni += 1                                  # Svako 5 poena se povecava polumjer za 1 i brzina za 1
            SOUND_PICKUP.play()                         # Pušta kratku notu kada se pokupi meta
            meta.generiraj_nove_koordinate_mete()
        elif poeni == 2 and len(loptice) == 1:          # Ako ima 2 poena i 1 loptica u terenu:
            nova_loptica = Lopta(pradius + 2, 5)
            nova_loptica.pravljenje_lopti()             # Dodaj jednu lopticu i generiraj novu metu
            loptice.append(nova_loptica)
            meta.generiraj_nove_koordinate_mete()
        elif poeni == 5 and len(loptice) == 2:          # Ako ima 5 poena i 2 loptice u terenu:
            nova_loptica = Lopta(pradius + 3, 6)
            nova_loptica.pravljenje_lopti()             # Dodaj još jednu lopticu i generiraj novu metu
            loptice.append(nova_loptica)
            meta.generiraj_nove_koordinate_mete()
        elif poeni == 10 and len(loptice) == 3:         # Ako ima 10 poena i 3 loptice u terenu:
            nova_loptica = Lopta(pradius + 4, 7)
            nova_loptica.pravljenje_lopti()             # Dodaj još jednu lopticu i generiraj novu metu
            loptice.append(nova_loptica)
            meta.generiraj_nove_koordinate_mete()
        elif poeni == 15 and len(loptice) == 4:         # Ako ima 15 poena i 4 loptice u terenu:
            nova_loptica = Lopta(pradius + 5, 8)
            nova_loptica.pravljenje_lopti()             # Dodaj još jednu lopticu i generiraj novu metu
            loptice.append(nova_loptica)
            meta.generiraj_nove_koordinate_mete()
        elif poeni == 20 and len(loptice) == 5:         # Ako ima 20 poena i 5 loptica u terenu:
            nova_loptica = Lopta(pradius + 6, 9)
            nova_loptica.pravljenje_lopti()             # Dodaj još jednu lopticu i generiraj novu metu
            loptice.append(nova_loptica)
            meta.generiraj_nove_koordinate_mete()
        elif poeni == 25 and len(loptice) == 6:         # Ako ima 25 poena i 6 loptica u terenu:
            nova_loptica = Lopta(pradius + 15, 10)
            nova_loptica.pravljenje_lopti()             # Dodaj još jednu lopticu i generiraj novu metu
            loptice.append(nova_loptica)
            meta.generiraj_nove_koordinate_mete()

        meta.draw()
        prikazi_rezultat()

        pygame.display.update()
        clock.tick(60)


glavni_meni()
