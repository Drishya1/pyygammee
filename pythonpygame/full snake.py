

import pygame
import random


pygame.mixer.init()


white = (255, 255, 255)
blue = (0, 0, 255)
black = (0, 0, 0)
red = (255,0,0)
gold = (255,215,0)
green = (0,255,0)
lemon = (255,250,205)


screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))


pygame.display.set_caption("drishya snake game")
pygame.display.update()


clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])


def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])



def game_loop():
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_length = 1

    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_height / 2)
    score = 0
    init_velocity = 5
    snake_size = 30
    fps = 60

    while not exit_game:
        if game_over:
            gameWindow.fill(gold)
            text_screen("game siddyo feri khelna lai enter thich ta" ,red ,100 ,245 )
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type== pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game_loop()

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = 7
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = -7
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - 7
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = 7
                        velocity_x = 0

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<8 and abs(snake_y - food_y)<8:
                score +=1
                food_x = random.randint(20, screen_width / 2)
                food_y = random.randint(20, screen_height / 2)
                snk_length +=5

            gameWindow.fill(lemon)
            text_screen("Score: " + str(score*10), blue, 5, 5)
            pygame.draw.rect(gameWindow, blue, [food_x, food_y, snake_size, snake_size])


            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]
            if head in snk_list [:-1]:
                game_over = True
            if snake_x< 0 or snake_x> screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
                print("Game Over!!!")

            # pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])
            plot_snake(gameWindow, green, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
game_loop()


