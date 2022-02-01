import pygame

class Tile:
    def __init__(
        self,
        image:pygame.Surface,
        type,
        x,
        y,
        window,
        camera
        ):
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.x,self.rect.y=x,y
        self.window=window
        self.type=type
        self.camera=camera
    def draw(
        self
        ):
        if self.camera is None:
            self.window.blit(self.image,(self.rect.x,self.rect.y))
        if self.camera is not None:
            self.window.blit(self.image, (self.rect.x-self.camera.scroll[0],self.rect.y-self.camera.scroll[1]))
