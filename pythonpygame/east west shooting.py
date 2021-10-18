import pygame
pygame.init()

width = 900
height = 500

screen =pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
background = pygame.image.load("space.png")

ywidth,yheight = 55,40
yellowspaceshipimg = pygame.image.load("spaceship_yellow.png")
yellow = pygame.transform.rotate(pygame.transform.scale(yellowspaceshipimg,(ywidth,yheight)),90)



rwidth,rheight = 55,40
redspacesipimg = pygame.image.load("spaceship_red.png")
red= pygame.transform.rotate(pygame.transform.scale(redspacesipimg,(rwidth,rheight)),-90)


white = (255,255,255)
black = (0,0,0)
redcolor = (255,0,0)
yellowcolor = (255,255,0)


#yellow
yellow_x =200
yellow_y =300
yellow_xchange = 0
yellow_ychange = 0
#red
red_x =600
red_y =300
red_xchange = 0
red_ychange = 0

#border
border_x = 450
border_y = 0
border_width = 10
border_height = 500

#bulet
bullet_velocity = 7
MAX_BULLETS = 3
YELLOW_HIT = pygame.USEREVENT +1
RED_HIT = pygame.USEREVENT +2
exit_game = True







while exit_game:

    red_bullets = []
    yellow_bullets = []

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = False
        #yellow movements

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                yellow_xchange += 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                yellow_xchange -= 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                yellow_ychange -= 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                yellow_ychange += 1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                yellow_xchange = 0
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                yellow_xchange = 0
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                yellow_ychange = 0
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                yellow_ychange = 0

        #red movements

        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                red_xchange-= 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                red_xchange += 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                red_ychange -= 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                red_ychange += 1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                red_xchange = 0
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                red_xchange = 0
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                red_ychange = 0
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                red_ychange = 0
        #bulletshooting
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                bullet = pygame.Rect(
                    yellow_x + ywidth, yellow_y + yheight // 2 - 2, 10, 5)
                yellow_bullets.append(bullet)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                bullet = pygame.Rect(
                    red_x, red_y + rheight // 2 - 2, 10, 5)
                red_bullets.append(bullet)
        #handle_bullets
        for bullet in yellow_bullets:
            bullet.x += bullet_velocity
            if red.colliderect(bullet):
                pygame.event.post(pygame.event.Event(RED_HIT))
                yellow_bullets.remove(bullet)
            elif bullet.x > width:
                yellow_bullets.remove(bullet)

        for bullet in red_bullets:
            bullet.x -= bullet_velocity
            if yellow.colliderect(bullet):
                pygame.event.post(pygame.event.Event(YELLOW_HIT))
                red_bullets.remove(bullet)
            elif bullet.x < 0:
                red_bullets.remove(bullet)






    yellow_x+= yellow_xchange
    yellow_y+= yellow_ychange
    if yellow_x<= 0:
        yellow_x = 0
    if yellow_y>= 450:
        yellow_y = 450


    red_x+=red_xchange
    red_y +=red_ychange
    if red_x>= 855:
        red_x = 855
    if red_y>= 450:
        red_y = 450



    screen.fill(white)
    screen.blit(background, (0, 0))
    screen.blit(yellow, (yellow_x, yellow_y))
    screen.blit(red, (red_x, red_y))
    pygame.draw.rect(screen, black, (border_x, border_y, border_width, border_height))
    print(red_bullets,yellow_bullets)










    pygame.display.update()
    clock.tick(70)







