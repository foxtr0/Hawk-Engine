import pygame

from src.controller import Controller

class Entity:
    def __init__(
        self,
        tag:str=None,
        sprite:pygame.Surface=None,
        window:pygame.Surface=None,
        health:float=100,
        position:list=[0,0],
        controller:Controller=None
        ):
        self.window=window
        self.sprite=sprite
        self._rect=pygame.Rect(0,0,0,0)
        self.tag=tag
        self.health=health
        self.position=position
    def rect(
        self
        )->pygame.Rect:
        if self.sprite is not None:
            w,h=self.sprite.get_size()
            self._rect.width=w
            self._rect.height=h
            self._rect.y=self.position[1]
            self._rect.x=self.position[0]
        return self._rect
    def render(
        self
        )->None:
        self.window.blit(self.sprite,self._rect)
    def debug(
        self
        )->None:
        #self.position[0] += 4
        pygame.draw.rect(self.window,(255,255,255),self._rect,1)
        
            
        
