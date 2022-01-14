import pygame

class Camera:
    def __init__(
        self,
        ):
        self.position=[0,0]
        self.scroll=[0,0]
        self.shaking=False
        
    def shake(
        self
        ):
        pass   
    
    def follow(
        self,
        obj_rect
        ):
        """Follows an object/rect"""
        self.scroll[0]+=(obj_rect.x-self.scroll[0]-200)//10
        self.scroll[1]+=(obj_rect.y-self.scroll[1]-100)//10