# James Bankole 12/16/16 unit 11
import pygame

class Ball(pygame.sprite.Sprite):
    """ This class creates the ball used in breakout. It gives the size, color and speed of the ball. It also makes the
     ball respond to collisions."""
    def __init__(self, color, windowWidth, windowHeight, screen):
        super().__init__()
        self.RADIUS = 10
        self.color = color
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.speedx = 5
        self.speedy = 3
        self.orb = pygame.Surface((7, 7))
        self.rect = self.orb.get_rect()
        self.orb.fill(self.color)
        self.screen = screen

    def move(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right > self.screen.get_width() or self.rect.left < 0:
            self.speedx = -self.speedx
        if self.rect.top < 0:
            self.speedy = -self.speedy

    def padCollide(self, spriteGroup):
        if pygame.sprite.spritecollide(self, spriteGroup, False):
            self.speedy = -self.speedy

    def brickCollide(self, spriteGroup):
        if pygame.sprite.spritecollide(self, spriteGroup, True):
            self.speedy = -self.speedy
