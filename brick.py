# James Bankole 12/16/16 unit 11
import pygame

class Brick(pygame.sprite.Sprite):
    """ This class creates the bricks used in breakout."""
    def __init__(self, width, color):
        super().__init__()
        self.BRICK_HEIGHT = 8
        self.width = width
        self.color = color
        self.block = pygame.Surface((self.width, self.BRICK_HEIGHT))
        self.rect = self.block.get_rect()
        self.block.fill(self.color)
