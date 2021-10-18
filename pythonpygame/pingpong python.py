import pygame,sys
pygame.init()
clock = pygame.time.Clock()

#ballspeed
ball_speed_x = 7
ball_speed_y = 7

#playerspeed

player_speed = 0

#opponent_speed

opponent_speed = 0



screen_width = 1000
screen_height = 600
screen= pygame.display.set_mode((screen_width,screen_height))
#colors

light_grey = (200,200,200)
bg_color = pygame.Color('grey12')
green= (0,255,0)


pygame.display.set_caption("drishya pong")

#game rectangle
ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 30, 30)
player = pygame.Rect(screen_width- 20, screen_height / 2 - 70, 10,140)
opponent = pygame.Rect(10, screen_height / 2 - 70, 10,140)

exit_game = True
while exit_game:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            exit_game = False

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    #ballmovement

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed_x *= -1
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_y*= -1
    #keyboard controlsplayer

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            player_speed -= 1
        if event.key == pygame.K_DOWN:
            player_speed += 1



        # keyboard controlsopponent
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LSHIFT:
            opponent_speed-=1
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LCTRL:
            opponent_speed+=1







    player.y+= player_speed
    if player.top<= 0:
        player.top=0
    if player.bottom >= screen_height:
        player.bottom = screen_height
    opponent.y += opponent_speed
    if opponent.top <=0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom= screen_height




    screen.fill(bg_color)

    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width / 2, 0), (screen_width / 2, screen_height))

    pygame.display.update()
    clock.tick(60)