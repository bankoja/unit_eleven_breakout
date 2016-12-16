# James Bankole 12/16/16 unit 11
import pygame, sys


from pygame.locals import *


import brick

import paddle

import ball

import random


def main():
    #Constants that will be used in the program
    APPLICATION_WIDTH = 400
    APPLICATION_HEIGHT = 600
    PADDLE_Y_OFFSET = 30
    BRICKS_PER_ROW = 10
    BRICK_SEP = 4 #The space between each brick
    BRICK_Y_OFFSET = 70
    BRICK_WIDTH =  (APPLICATION_WIDTH - (BRICKS_PER_ROW +1) * BRICK_SEP) / BRICKS_PER_ROW
    NUM_TURNS = 3
    BRICK_HEIGHT = 8
    pygame.init()



    mainSurface = pygame.display.set_mode((APPLICATION_WIDTH, APPLICATION_HEIGHT), 0, 32)
    pygame.display.set_caption("Awwww BREAKOUT!")


    #Sets up the colors
    RED = (255, 0, 0)
    ORANGE = (255, 165, 0)
    YELLOW = (255, 255, 0)
    GREEN =(0, 255, 0)
    CYAN = (0, 255, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)


    listColors = [RED, RED, ORANGE, ORANGE, YELLOW, YELLOW, GREEN, GREEN, CYAN, CYAN]
    xPos = BRICK_SEP
    yPos = BRICK_Y_OFFSET
    mainSurface.fill(WHITE)


    brickGroup = pygame.sprite.Group()


    for color in listColors:
        for x in range(BRICKS_PER_ROW):
            pie = brick.Brick(BRICK_WIDTH , color)
            pie.rect.x = xPos
            pie.rect.y = yPos
            xPos += BRICK_SEP + BRICK_WIDTH
            brickGroup.add(pie)
        yPos += BRICK_HEIGHT + BRICK_SEP
        xPos = BRICK_SEP


    paddleGroup = pygame.sprite.Group()

    piepaddle = paddle.Paddle(BLACK)
    piepaddle.rect.x = APPLICATION_WIDTH / 2
    piepaddle.rect.y = APPLICATION_HEIGHT - PADDLE_Y_OFFSET
    paddleGroup.add(piepaddle)

    breakBall = ball.Ball(BLACK, APPLICATION_WIDTH, APPLICATION_HEIGHT, mainSurface)
    breakBall.rect.x = APPLICATION_WIDTH / 2
    breakBall.rect.y = APPLICATION_HEIGHT / 2
    myFont = pygame.font.SysFont("Helvetica", 24)
    label = myFont.render("GAME OVER", 1, BLACK)


    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        mainSurface.fill(WHITE)
        for block in brickGroup:
            mainSurface.blit(block.block, block.rect)
        piepaddle.move()
        mainSurface.blit(piepaddle.board, piepaddle.rect)
        breakBall.move()
        if breakBall.rect.bottom > APPLICATION_HEIGHT:
            NUM_TURNS -= 1
            breakBall.rect.x = APPLICATION_WIDTH / 2
            breakBall.rect.y = APPLICATION_HEIGHT / 2
            pygame.time.wait(1000)
        if NUM_TURNS == 0:
            mainSurface.fill(WHITE)

            mainSurface.blit(label, (200,275))
            pygame.display.update()
            pygame.time.wait(2000)
            pygame.quit()
            sys.exit()

        mainSurface.blit(breakBall.orb, breakBall.rect)
        breakBall.padCollide(paddleGroup)
        breakBall.brickCollide(brickGroup)
        pygame.display.update()
main()
