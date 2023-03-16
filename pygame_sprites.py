import pygame,random,time
pygame.init()

screen=pygame.display.set_mode((500,400))
clock=pygame.time.Clock()
pygame.mixer.music.load('sounds/background.mp3')
gravity=6
allsprites=pygame.sprite.Group()
score=0
speed=10

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.Surface((50,50))
        self.image.fill('yellow')
        self.rect=self.image.get_rect()
        self.rect.x=50
        self.rect.y=250
        self.yvel=0
        self.jumped=False
        self.doublejumped=False
        allsprites.add(self)
    def jump(self):
        self.jumped=True
        self.yvel=-45

    def update(self):
        self.yvel+=gravity
        self.rect.y+=self.yvel
        if self.rect.y>250:
            self.rect.y=250
            self.jumped=False
            self.doublejumped=False

class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        global speed
        self.image=pygame.Surface((50,50))
        self.image.fill('red')
        self.rect=self.image.get_rect()
        self.rect.x=400
        self.rect.y=250
        self.xvel=-speed
        allsprites.add(self)

    def update(self):
        global score
        self.rect.x+=self.xvel
        if self.rect.x<-50:
            self.kill()
            score+=10

player=Player()
player_group=pygame.sprite.Group()
player_group.add(player)

obstacle=Obstacle()
obg=pygame.sprite.Group()
obg.add(obstacle)

count=0
running=True
pygame.mixer.music.play()
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                if player.jumped and not player.doublejumped:
                    player.jump()
                    player.doublejumped=True
                if player.jumped==False:
                    player.jump()
    if random.randint(0,50)==0:
        newobs=Obstacle()
        obg.add(newobs)
    count+=1
    if count==100:
        speed+=1
        pygame.mixer.Sound('sounds/point.ogg').play()
        print(speed)


    if pygame.sprite.spritecollide(player,obg,False):
        pygame.mixer.Sound('sounds/crash.ogg').play()
        time.sleep(0.7)
        pygame.mixer.music.stop()
        pygame.mixer.Sound('sounds/game_over.ogg').play()
        time.sleep(1)
        print('GAME OVER YOUR SCORE IS',score)

        running=False




    screen.fill('green')
    pygame.draw.rect(screen, 'brown', (0,300,500,100))
    allsprites.update()
    allsprites.draw(screen)

    clock.tick(20)
    pygame.display.update()


pygame.quit()












