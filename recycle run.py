import pygame
import random
pygame.init()
HEIGHT = 600
WIDTH = 800
TITLE =  "recylcle run"
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(TITLE)
bitn = pygame.image.load("bin.png")
bag = pygame.image.load("plastic bag.png")
pbag = pygame.image.load("item1.png")
crate = pygame.image.load("bag.png")
bg = pygame.image.load("idk.png")
pencil = pygame.image.load("pen.png")
points = 0

items = [pencil,pbag,crate]

class Bin(pygame.sprite.Sprite):
    def __init__(self,i,x,y ):
        super().__init__()
        self.image = pygame.transform.scale(i,(50,70))
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
class Nonrecycable(pygame.sprite.Sprite):
    def __init__(self,i,x,y):
        super().__init__()
        self.image = pygame.transform.scale(i,(50,50))
        self.rect =self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
class Recycable(pygame.sprite.Sprite):
    def __init__(self,i,x,y):
        super().__init__()
        self.image = pygame.transform.scale(i,(50,50))
        self.rect =self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
bin = Bin(bitn,60,50)
bingroup=pygame.sprite.Group()
bingroup.add(bin)

rectems = pygame.sprite.Group()
for i in range(20):
    x = random.randint(50,700)
    y = random.randint(50,500)
    paperbag = Recycable(random.choice(items),x,y)
    rectems.add(paperbag)
    

nontems = pygame.sprite.Group()
for i in range(20):
    
    x = random.randint(50,700)
    y = random.randint(50,500)
    beg = Nonrecycable(bag,x,y)
    nontems.add(beg)
run = True

while run == True:
    screen.blit(bg,(0,0))
    nontems.draw(screen)
    rectems.draw(screen)
    bingroup.draw(screen)
    font = pygame.font.SysFont("Arial",50)
    text = font.render("points:"+str(points),True,"orange")
    screen.blit(text,(50,50))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if pygame.sprite.groupcollide(bingroup,rectems,False,True):
        points = points +1
    if pygame.sprite.groupcollide(bingroup,nontems,False,True):
        points = points -1

    kdown=pygame.key.get_pressed()
    if kdown[pygame.K_DOWN]:
        bin.rect.y = bin.rect.y + 1
    if kdown[pygame.K_UP]:
        bin.rect.y = bin.rect.y - 1
    if kdown[pygame.K_LEFT]:
        bin.rect.x = bin.rect.x - 1
    if kdown[pygame.K_RIGHT]:
        bin.rect.x = bin.rect.x + 1
        
    
    
    
    pygame.display.update()