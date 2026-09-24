import random
import pygame
pygame.init()
screen=pygame.display.set_mode((500,500))
done=False
x=225
y=400
bg=pygame.transform.scale(pygame.image.load("BACKG.png"), (500,500))
player=pygame.transform.scale(pygame.image.load("P.png"), (70,70))
al=pygame.transform.scale(pygame.image.load("E.png"), (50,50))
bullet=pygame.transform.scale(pygame.image.load("GUN.png"), (20,20))
gun=False
x2=x
y2=y
clock=pygame.time.Clock()
hit=False
score=pygame.font.SysFont("Arial", 50)
score1=0

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                x-=10
                x2-=10
            if event.key==pygame.K_RIGHT:
                x+=10
                x2+=10
            if event.key==pygame.K_SPACE:
                gun=True
    screen.blit(bg, (0,0))
    a=screen.blit(player, (x,y))
    if gun:
        screen.blit(bullet, (x2, y2))
        y2-=0.2
        if y2<0:
            gun=False
    
    y1=0
    x1=random.randint(0,450)
    x8=random.randint(0,450)
    x3=random.randint(0,450)
    x4=random.randint(0,450)
    x5=random.randint(0,450)
    x6=random.randint(0,450)
    x7=random.randint(0,450)
    xes=[x1,x3,x4,x5,x6,x7,x8]
    enemy=[(xes, y1+0.2) for xes, y1 in enemy]
    
    if a.colliderect():
        score1=1

        hit=True
    if hit==True:
        m=score.render(f"Score: {score1}", True, (250,250,250))
        screen.blit(m, (10,10))
    print(score)
    pygame.display.flip()
pygame.quit()