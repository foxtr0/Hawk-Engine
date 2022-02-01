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
        amount:int=1,
        camera=None
        ):
        self.window=window
        self.sprite=sprite
        self.tag=tag
        self.health=health
        self.position=position
        self.rect=pygame.Rect(self.position[0],self.position[1],self.sprite.get_width(),self.sprite.get_height())
        self.killed=False
        self.alive=True
        self.controller=controller
        self.camera=camera
    def render(
        self
        )->None:
        """Blits the sprite"""
        if self.camera is None:
            self.window.blit(self.sprite,self.rect)
        if self.camera is not None:
            self.window.blit(self.sprite,(self.rect.x-self.camera.scroll[0],self.rect.y-self.camera.scroll[1]))
    def move(
        self
        ):
        """Moves the entity by detecting input"""
        keys=pygame.key.get_pressed()
        self.position=self.controller.movement()
        self.controller.friction()
        if keys[pygame.K_d]or keys[pygame.K_RIGHT]:
            self.controller.moving_right=True
        if keys[pygame.K_a]or keys[pygame.K_LEFT]:
            self.controller.moving_left=True
        if keys[pygame.K_s]or keys[pygame.K_DOWN]:
            self.controller.moving_down=True
        if keys[pygame.K_w]or keys[pygame.K_UP]:
            self.controller.moving_up=True
    def collide(
        self,
        tile_list
        ):
        """Makes the entity collidable with the `Tile` class's rect"""
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
    def get_position(
        self
        ):
        return self.position
    def debug(
        self
        )->None:
        """debugs the entity by drawing the rect"""
        pygame.draw.rect(self.window,(30,25,255),self.rect,1)

