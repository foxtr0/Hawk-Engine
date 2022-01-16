import pygame

class Tile:
    def __init__(
        self,
        image:pygame.Surface,
        type,
        x,
        y,
        window
        ):
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.x,self.rect.y=x,y
        self.window=window
        self.type=type
    def draw(
        self
        ):
        pygame.draw.rect(self.window,(30,30,30),self.rect)
        self.window.blit(self.image,(self.rect.x,self.rect.y))
