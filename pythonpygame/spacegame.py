import pygame
import random


pygame.init()

screen =pygame.display.set_mode((800,600))
pygame.display.set_caption("Drishya space")
icon = pygame.image.load("head.jpg")
pygame.display.set_icon(icon)
background = pygame.image.load("background.png")

#player
playerimg = pygame.image.load("player.png")
playerx = 110
playery =450
playerxchange = 0

#enemy
enemyimg = pygame.image.load('enemy.png')
enemyx= random.randint(0,800)
enemyy =random.randint(45,150)
enemyxchange= 8
enemyychange = 40
#bullet
bulletimg = pygame.image.load('bullet.png')
bulletx= 0
bullety = 480
bulletxchange= 0
bulletychange = 10
bullet_state = "Fire"


def player(x,y):
    screen.blit(playerimg,(x,y))
def enemy(x,y):
    screen.blit(enemyimg,(x,y))
def  firebullet(x,y):
    global bullet_state
    bullet_state = "ready"
    screen.blit(bulletimg, (x , y ))

white = (255,255,255)
black = (0,0,0)
exit_game = True
quit_game = False

while  exit_game:

    screen.fill(black)
    screen.blit(background,(0,0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerxchange+= 7

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerxchange-= 7

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerxchange = 0
        if event.type == pygame.KEYDOWN:
            if event.key== pygame.K_SPACE:
                firebullet(playerx,bullety)



    #player movement

    playerx+= playerxchange
    if playerx<= 0:
        playerx= 0
    elif playerx >= 736:
        playerx = 736
        #enemey movement

    enemyx+= enemyxchange
    if enemyx <= 0:
        enemyxchange = 8
        enemyy+= enemyychange
    elif enemyx >= 736:
        enemyxchange = -8
        enemyy +=enemyychange
    #bullet movement

    if bullet_state is "fire":
        firebullet(bulletx, bullety)
        bullety -= bulletychange

    player(playerx,playery)
    enemy(enemyx,enemyy)

    pygame.display.update()

pygame.quit()
quit()


