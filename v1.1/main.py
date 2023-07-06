import pygame
import sys
import random
from math import *

pygame.init()
pygame.mixer.init()

sirina = 854
visina = 480
zaslon = pygame.display.set_mode((sirina, visina))
pygame.display.set_caption("Smirujuća igrica v1.1")
clock = pygame.time.Clock()

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
        color = crvena
        pygame.draw.rect(zaslon, color, (self.x, self.y, self.w, self.h))


def ugasi():    # Glavna petlja igrice
    loop = True     # Kada True -> igrica radi, Kada False -> igrica se gasi

    font = pygame.font.SysFont("Agency FB", 100)                # Vrsta fonta i veličina fonta za prikaz
    tekst = font.render("Izugbio si!", True, (230, 230, 230))   # Odabir teksta i boja teksta za prikaz

    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:       # Kad se stisne crveni X, igrica se gasi
                ugasi_igricu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:     # Kad se stisne "Q" na tipkovnici, igrica se gasi
                    ugasi_igricu()
                if event.key == pygame.K_r:     # Kad se stisne "R" na tipkovnici, igrica se resetira
                    glavni_loop()

        zaslon.fill(pozadina)                   # Prikaz pozadine na zaslon

        zaslon.blit(tekst, (sirina//2 - tekst.get_width()//2, visina * 0.5))   # Prikaz zavrsnog teksta na zaslon
        prikazi_uspjeh()                                                       # Prikaz poena u gornjem desnom kutu
        prikazi_rank()
        prikazi_skalu()

        pygame.display.update()                     # Osvjezavanje zaslona
        clock.tick()                                # Ferkfencija osvjezavanja zaslona


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
    prikaz_uspjeha = font.render("Uspjeh: " + str(uspjeh) + "%", True, (230, 230, 230))
    zaslon.blit(prikaz_uspjeha, (sirina//2 - prikaz_uspjeha.get_width()//2, visina * 0.87))


def prikazi_rezultat():     # Prikaz rezultata na zaslon
    font = pygame.font.SysFont("Forte", 30)                                     # Odabir fonta i velicine fonta
    prikaz_poena = font.render("Score: " + str(poeni), True, (230, 230, 230))   # Prikaz teksta na zaslon u boji(x,x,x)
    zaslon.blit(prikaz_poena, (sirina//2 - prikaz_poena.get_width()//2, visina * 0.87))    # Lokacija prikaza teksta


def prikazi_skalu():    # Prikaz ljestvice u bojama sa lijeve i desne strane
    zaslon.blit(skala, (sirina * 0.1 - skala.get_width() // 2, visina // 2 - skala.get_height() // 2))
    zaslon.blit(skala, (sirina * 0.9 - skala.get_width() // 2, visina // 2 - skala.get_height() // 2))


def prikazi_rank():     # Prikaz ranka u bojama po ljestvici nakon sudara
    font = pygame.font.SysFont("Comicsans", 40)
    font_veci = pygame.font.SysFont("Comicsans", 60)

    if poeni < 1:                        # Do 1 poena -- NE ZNA KO MU GLAVU NOSI
        rank = "ZNAŠ LI DI ĆEŠ?"
        rank_obojen = font_veci.render(rank, True, (10, 100, 10))
        zaslon.blit(rank_obojen, (sirina // 2 - rank_obojen.get_width() // 2, visina * 0.2))

    elif poeni < 20:                      # Do 20 poena -- NIKO I NISTA
        rank = "NIKO I NIŠTA"
        rank_obojen = font_veci.render(rank, True, (79, 186, 29))
        zaslon.blit(rank_obojen, (sirina // 2 - rank_obojen.get_width() // 2, visina * 0.2))

    elif poeni >= 20 and poeni < 40:      # Do 40 poena -- OUTSIDER
        rank = "OUTSIDER"
        rank_obojen = font_veci.render(rank, True, (141, 223, 0))
        zaslon.blit(rank_obojen, (sirina // 2 - rank_obojen.get_width() // 2, visina * 0.2))
    elif poeni >= 40 and poeni < 55:      # Do 55 poena -- AMATER
        rank = "AMATER"
        rank_obojen = font_veci.render(rank, True, (182, 221, 21))
        zaslon.blit(rank_obojen, (sirina // 2 - rank_obojen.get_width() // 2, visina * 0.2))

    elif poeni >= 55 and poeni < 70:      # Do 70 poena -- UVJEZBAN
        rank = "UVJEZBAN"
        rank_obojen = font_veci.render(rank, True, (253, 209, 1))
        zaslon.blit(rank_obojen, (sirina // 2 - rank_obojen.get_width() // 2, visina * 0.2))

    elif poeni >= 70 and poeni < 85:      # Do 85 poena -- PROFI
        rank = "PROFI"
        rank_obojen = font_veci.render(rank, True, (255, 134, 0))
        zaslon.blit(rank_obojen, (sirina // 2 - rank_obojen.get_width() // 2, visina * 0.2))

    elif poeni >= 85 and poeni < 99:      # Do 99 poena -- MASTER
        rank = "MASTER"
        rank_obojen = font_veci.render(rank, True, (238, 38, 1))
        zaslon.blit(rank_obojen, (sirina // 2 - rank_obojen.get_width() // 2, visina * 0.2))

    elif poeni >= 100:                     # 100+ poena -- OP
        rank = "OP"
        rank_obojen = font_veci.render(rank, True, (255, 0, 0))
        zaslon.blit(rank_obojen, (sirina // 2 - rank_obojen.get_width() // 2, visina * 0.2))

    prikaz_ranka = font.render("Tvoj rank:", True, (230, 230, 230))

    zaslon.blit(prikaz_ranka, (sirina // 2 - prikaz_ranka.get_width() // 2, visina * 0.04))


def glavni_loop():  # Glavna petlja igranja
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
                ugasi_igricu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:     # Kad se upre "Q", igrica se gasi
                    ugasi_igricu()
                if event.key == pygame.K_r:     # Kad se upre "R", skor i igrica se resetiraju
                    glavni_loop()

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


glavni_loop()
