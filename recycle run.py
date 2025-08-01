import pygame
import random

HEIGHT = 600
WIDTH = 800
TITLE =  "recylcle run"
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(TITLE)
bitn = pygame.image.load("bin.pygame projects\\bin.png")
bag = pygame.image.load("plastic bag.png")
pbag = pygame.image.load("item1.png")
crate = pygame.image.load("bag.png")
bg = pygame.image.load("idk.png")
pencil = pygame.image.load("pen.png")
items = [pencil,pbag,crate]

class Bin(pygame.sprite.Sprite):
    def __init__(self,i,x,y ):
        super().__init__()
        self.image = i
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
class Nonrecycable(pygame.sprite.Sprtite):
    def _init_(self,i,x,y):
        super()._init_()
        self.image = i
        self.rect =self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
class Recycable(pygame.sprite.Sprtite):
    def _init_(self,i,x,y):
        super()._init_()
        self.image = i
        self.rect =self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
bin = Bin(bitn,60,50)
bingroup=pygame.sprite.Group()
bingroup.add(bin)
pen = Recycable()
rectems = pygame.sprite.Group()
paperbag = Recycable(pbag,60,50)
rectems.add(pbag)
nontems = pygame.sprite.Group()
beg = Nonrecycable(bag,60,50)
nontems.add(beg)
run = True

while run == True:
    screen.blit(bg,(0,0))
    nontems.draw(screen)
    rectems.draw(screen)
    bin.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()