import pygame

class Tile:
    def __init__(
        self,
        image:pygame.Surface,
        x,
        y,
        window
        ):
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.x,self.rect.y=x,y
        self.window=window
    def draw(
        self
        ):
        self.window.blit(self.image,(self.rect.x,self.rect.y))