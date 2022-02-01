import pygame

class Camera:
    def __init__(
        self,
        position,
        lerp
        ):
        self.position=position
        self.scroll=[0,0]
        self.shaking=False
        self.lerp=lerp
    def shake(
        self
        ):
        pass   
    
    def follow(
        self,
        entity_rect
        ):
        """Follows an entity/rect"""
        self.scroll[0]+=(entity_rect.x-self.scroll[0]-self.position[0])//self.lerp[0]
        self.scroll[1]+=(entity_rect.y-self.scroll[1]-self.position[1])//self.lerp[1]
