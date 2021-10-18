import  pygame
pygame.init()

screen =pygame.display.set_mode((1200,600))
pygame.display.set_caption("Drishya game")

white = (0,0,0)
playerimg = pygame.image.load('head.jpg')

playerx = 600
playery = 300








exit_game = True
quit_game = False


while not  exit_game:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
            exit_game = True

    screen.fill(white)

    pygame.display.update()
