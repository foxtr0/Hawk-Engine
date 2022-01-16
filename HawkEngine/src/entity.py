import pygame
from controller import Controller

class Entity:
    def __init__(
        self,
        tag:str=None,
        sprite:pygame.Surface=None,
        window:pygame.Surface=None,
        health:float=100,
        position:list=[0,0],
        controller:Controller=None,
        amount:int=1
        ):
        self.window=window
        self.sprite=sprite
        self.tag=tag
        self.health=health
        self.position=position
        self.rect=pygame.Rect(self.position[0],self.position[1],self.sprite.get_width(),self.sprite.get_height())
        self.killed=False
        self.controller=controller
    def render(
        self
        )->None:
        self.window.blit(self.sprite,self.rect)
    def collide(
        self,
        tile_list
        ):
        collision_types={"right":False,"left":False,"top":False,"bottom":False}
        self.rect.x+=self.position[0]
        hit=[]
        for tile in tile_list:
            if self.rect.colliderect(tile.rect):
                hit.append(tile)
        for tile in hit:
            if self.position[0]>0:
                self.rect.right=tile.rect.left
                collision_types["right"]=True
            if self.position[0]<0:
                self.rect.left=tile.rect.right
                collision_types["left"]=True
        self.rect.y+=self.position[1]
        hit=[]
        for tile in tile_list:
            if self.rect.colliderect(tile.rect):
                hit.append(tile)
        for tile in hit:
            if self.position[1]>0:
                self.rect.bottom=tile.rect.top
                collision_types["bottom"]=True
            if self.position[1]<0:
                self.rect.top=tile.rect.bottom
                collision_types["top"]=True
        return collision_types
        
    def debug(
        self
        )->None:
        pygame.draw.rect(self.window,(30,25,255),self.rect,1)
        
            
        
