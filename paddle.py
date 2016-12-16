# James Bankole 12/16/16 unit 11
import pygame

class Paddle(pygame.sprite.Sprite):
    """ This class creates the paddle used in breakout. It also moves the paddle in correspondance with the mouse."""
    def __init__(self, color):
        super().__init__()
        self.WIDTH = 40
        self.HEIGHT = 10
        self.color = color
        self.board = pygame.Surface((self.WIDTH, self.HEIGHT))
        self.rect = self.board.get_rect()
        self.board.fill(self.color)

    def move(self):
        xPos = pygame.mouse.get_pos()[0]
        self.rect.x = xPos