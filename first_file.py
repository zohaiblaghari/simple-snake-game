import pygame
from pygame.locals import*
import time
import random

pygame.init()

red = (255,0,0)
red1 = (153,0,0)
blue = (0,0,255)
orange = (255,204,153)
green = (0,120,0)


SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game Madeby ZohaibLaghari")

snake = 10
snake_speed = 10

clock = pygame.time.Clock()

font_style = pygame.font.SysFont("cambria",26)
score_font = pygame.font.SysFont("verdana",30)

def user_score(score):
    number = score_font.render("Score :"+str(score),True,blue)
    screen.blit(number,[0,0])

def game_snake(snake, snake_length_list):
    for x in snake_length_list:
        pygame.draw.rect(screen,green,[x[0], x[1],snake,snake])

def message(msg):
    msg = font_style.render(msg,True,red1)
    screen.blit(msg,[SCREEN_WIDTH/9, SCREEN_HEIGHT/3]) 

def game_loop():
    gameOver = False
    gameclose = False

    X1 = SCREEN_WIDTH/2 
    Y1 = SCREEN_HEIGHT/2

    X1_change = 0
    Y1_change = 0

    snake_length_list = []
    snake_length = 1

    foodx = round(random.randrange(0, SCREEN_WIDTH - snake)/10.0)*10.0
    foody = round(random.randrange(0, SCREEN_HEIGHT - snake)/10.0)*10.0

    while not gameOver:
        
        while gameclose == True:
            screen.fill(orange)
            message("you lost! Press P to play again and Q to quite the game")
            user_score(snake_length-1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameOver = True
                        gameclose = True
                    if event.key == pygame.K_p:
                        game_loop()
    
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_LEFT:
                    X1_change = -snake
                    Y1_change = 0
                if event.key == K_RIGHT:
                    X1_change = snake
                    Y1_change = 0
                if event.key == K_UP:
                    X1_change = 0
                    Y1_change = -snake
                if event.key == K_DOWN:
                    X1_change = 0
                    Y1_change = snake


        if X1 > SCREEN_WIDTH or X1< 0 or Y1 > SCREEN_HEIGHT or Y1< 0:
            gameclose = True
        X1 += X1_change
        Y1 += Y1_change
        screen.fill(orange)
        pygame.draw.rect(screen,red,[foodx,foody,snake,snake] )
        snake_size = []
        snake_size.append(X1)
        snake_size.append(Y1)
        snake_length_list.append(snake_size)
        if len(snake_length_list) > snake_length:
            del snake_length_list[0]
        
        
        game_snake(snake,snake_length_list)
        user_score(snake_length - 1)
        
        pygame.display.update()
        
        
        if X1 == foodx and Y1 == foody:
            foodx = round(random.randrange(0, SCREEN_WIDTH - snake)/10.0) * 10.0
            foody = round(random.randrange(0, SCREEN_HEIGHT - snake)/10.0) * 10.0
            snake_length +=1
        clock.tick(snake_speed)


    pygame.quit()
    quit()


game_loop()


    
        
    
