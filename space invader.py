import random
import pygame
pygame.init()
screen=pygame.display.set_mode((1200,730))
done=False
x=600
y=600
bg=pygame.transform.scale(pygame.image.load("BACKG.png"), (1200,730))
player=pygame.transform.scale(pygame.image.load("P.png"), (100,100))
enemy=pygame.transform.scale(pygame.image.load("E.png"), (70,70))
bullet=pygame.transform.scale(pygame.image.load("GUN.png"), (30,30))
gun=False
x2=x
y2=y
clock=pygame.time.Clock()
hit=False
score=pygame.font.SysFont("Arial", 50)
score1=0
y1=0
clock=pygame.time.Clock()
x1=random.randint(200,1000)
x3=random.randint(200,1000)
y3=0
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                x-=30
                x2-=30
            if event.key==pygame.K_RIGHT:
                x+=30
                x2+=30
            if event.key==pygame.K_SPACE:  
                gun=True
    screen.blit(bg, (0,0))
    d=screen.blit(player, (x,y))
    b=screen.blit(enemy, (x1,y1))
    e=screen.blit(enemy, (x3,y3))
    if y1>=660:
        done=True
    if d.colliderect(b):
        done=True
    if d.colliderect(e):
        done=True
    if gun:
        a=screen.blit(bullet, (x2, y2))
        h=screen.blit(bullet, (x2+70,y2))
        y2-=2
        if y2<0:
            gun=False
        if a.colliderect(b):
            score1+=1
            y1=0
            x1=random.randint(200,1000)
            y2=y
            gun=False
        if a.colliderect(e):
            score1+=1
            y3=0
            x3=random.randint(200,1000)
            y2=y
            gun=False
        if h.colliderect(e):
            score1+=1
            y3=0
            x3=random.randint(200,1000)
            y2=y
            gun=False
        if h.colliderect(b):
            score1+=1
            y1=0
            x1=random.randint(200,1000)
            y2=y
            gun=False

        hit=True
    m=score.render(f"Score: {score1}", True, (250,250,250))
    screen.blit(m, (10,10))
    y1+=1
    y3+=1
    pygame.display.flip()
pygame.quit()
