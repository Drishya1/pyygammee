import pygame
import random
pygame.init()
black = (0,0,0)
white = (255,255,255)

screen = pygame.display.set_mode((500,650))
clock = pygame.time.Clock()
pygame.display.set_caption("flappy bird drishya")
backimg = pygame.image.load("background-night.png")
backimg1 = pygame.transform.scale2x(backimg)
flappyimg = pygame.image.load("bluebird-downflap.png")
rect = flappyimg.get_rect()


floor = pygame.image.load("base.png")
floor1 = pygame.transform.scale2x(floor)

bird_x = 100
bird_y= 500
bird_ychange = -1.40

#floor
floor_x = 1
floor_y = 560
floor_xchange = 0

#obstacle1
obstacle_width = 70
obstacle_height = random.randint(150,400)
obstacle_colour = (188,90,230)
obstacle_change = -1
obsctacle_x = 290
obstacle_y = -2.50
#obstalce2
obstacle2_x = 370
obstacle2_y = 400
obstacle2_change = -1





def floor2():
    screen.blit(floor1,(floor_x,floor_y))
    screen.blit(floor1, (floor_x + 500, floor_y))

def obstacle():
    pygame.draw.rect(screen,obstacle_colour,(obsctacle_x,obstacle_y,obstacle_width,obstacle_height))
    pygame.draw.rect(screen,obstacle_colour,(obstacle2_x,obstacle2_y,70,obstacle_height))



run_game = True
while run_game:
    screen.blit(backimg1, (0, 0))
    screen.blit(flappyimg, (bird_x, bird_y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_y-=100
        if event.type == pygame.KEYUP:
            if event.type == pygame.K_SPACE:
                bird_ychange=0

    bird_y-= bird_ychange

    floor_x -= 1
    if floor_x <=-576:
        floor_x = 0
    #bird
    if bird_y<= 0:
        bird_y = 0
    if bird_y >= 535:
        bird_y = 535
    #obstacle
    obsctacle_x+= obstacle_change
    if obsctacle_x<= 10:
        obsctacle_x= 500

    #obstacle2
    obstacle2_x+= obstacle2_change
    if obstacle2_x<= 10:
        obstacle2_x = 600





    floor2()
    obstacle()


    pygame.display.update()
    clock.tick(120)




