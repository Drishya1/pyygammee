import pygame
import random
pygame.init()
screen = pygame.display.set_mode((800,600))
black = (0,0,0)

pygame.display.set_caption("space invaders")
background=pygame.image.load("background.png")
playerimg = pygame.image.load('player.png')
icon = pygame.image.load('head.jpg')
pygame.display.set_icon(icon)
#enemy
enemyimg=pygame.image.load("enemy.png")
enemy_x = random.randint(0,800)
enemy_y = random.randint(0,90)
enemy_xchange = 4
enemy_ychange = 30

#player
player_x = 370
player_y = 480
player_xchange = 0
#bullet
bulletimg = pygame.image.load("bullet.png")
bullet_x = 30
bullet_y = 480
bullet_xchange = 0
bullet_ychange = 40
bullet_state = "ready"
def enemy():
    screen.blit(enemyimg,(enemy_x,enemy_y))
def player():
    screen.blit(playerimg,(player_x,player_y))
def fire_bullet():
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg,(bullet_x+16 ,bullet_y+10))


exit_game = False
while not exit_game:
    screen.fill(black)
    screen.blit(background,(0, 0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player_xchange += 5

            if event.type == pygame.K_SPACE:
                fire_bullet(player_x,bullet_y)


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_xchange -= 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or pygame.K_LEFT:
                player_xchange = 0

    player_x+= player_xchange
    if player_x<=0:
        player_x = 0
    if player_x >= 636:
        player_x = 636

    enemy_x+= enemy_xchange

    if enemy_x<=0:
        enemy_xchange = 5
        enemy_y+= enemy_ychange
    if enemy_x>= 736:
        enemy_xchange = -5
        enemy_y += enemy_ychange


    # bulletmovement
    if bullet_state == "fire":
        fire_bullet(player_x,bullet_y)
        bullet_y-=bullet_ychange


    player()
    enemy()


    pygame.display.update()