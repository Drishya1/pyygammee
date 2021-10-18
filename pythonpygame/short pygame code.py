import pygame


pygame.init()

screen =pygame.display.set_mode((800,600))
pygame.display.set_caption("Drishya space")
icon = pygame.image.load("head.jpg")
pygame.display.set_icon(icon)

playerimg = pygame.image.load("player.png")
playerx = 30
playery =400
playerchange = 0

def player(x,y):
    screen.blit(playerimg,(x,y))

white = (255,255,255)
black = (0,0,0)
exit_game = True
quit_game = False

while  exit_game:

    screen.fill(black)
    playerx += 0.1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = False




    player(playerx,playery)
    pygame.display.update()

pygame.quit()
quit()


