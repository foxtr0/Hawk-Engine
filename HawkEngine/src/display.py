import pygame

class Display:
    def __init__(
        self,
        screen_size,
        display_size
        ):
        self.screen_size=screen_size
        self.display_size=display_size
        self.window=pygame.display.set_mode(self.screen_size)
        self.display=pygame.Surface(self.display_size)
        self.offset=[0,0]
    def update(
        self
        ):
        self.window.blit(pygame.transform.scale(self.display,self.screen_size),self.offset)
    def get_size(
        self
        ):
        return self.screen_size
    