import pygame
import random
import math


        

class player():
    def __init__ (self, xPos, yPos, vel, dam, hp, Pw, Pl):        
        self.xPos = xPos
        self.yPos = yPos
        self.vel = vel
        self.dam = dam
        self.hp = hp        
        self.Pw = Pw
        self.Pl = Pl
    
    def getCoords(self):
        return self.xPos, self.yPos 

class enemy():
    def __init__ (self, colour, Evel, Edam, Ehp, Ew, El):
        self.colour = colour
        self.Exvel = 0
        self.EyVel = 0
        self.ExPos = 0
        self.EyPos = 0
        
        self.Evel = Evel
        self.Edam = Edam
        self.Ehp = Ehp        
        self.Ew = Ew
        self.El = El
        self.rect = None
    
    def eSpawn(self, PxPos, PyPos): 
        radius = random.randint(200,300)
        self.ExPos = random.randint(-50,50)
        self.EyPos = (math.sqrt(radius**2 - self.ExPos**2) * random.choice([1,-1]))
        velRat = self.Evel/radius
        
        self.ExVel = self.ExPos * velRat
        self.EyVel = self.EyPos * velRat
        self.ExPos = self.ExPos + PxPos
        self.EyPos = self.EyPos + PyPos
        
        
        self.rect = pygame.Rect(self.ExPos, self.EyPos,self.Ew,self.El)
 
    def eMove(self):
        self.ExPos = self.ExPos - self.ExVel
        self.EyPos = self.EyPos - self.EyVel
        self.rect = pygame.Rect(self.ExPos, self.EyPos,self.Ew,self.El)
        
        
    def eDraw (self, screen):
        pygame.draw.rect(screen, self.colour, self.rect)

    def getRekt(self):
        return self.rect
    
    def eGetCoords(self):
        return self.ExPos, self.EyPos
        
        
#Button class and functionality

class button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), (int(height * scale))))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False

    #method for drawing buttons on screen
    def draw(self, surface):
        action = False
        #getting mouse position
        position = pygame.mouse.get_pos()
        
        #checking if mouse is over buttons/being clicked
        if self.rect.collidepoint(position):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
            #resets the click
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        
        
        
        
        #Draw button on screen   
        surface.blit(self.image, (self.rect.x, self.rect.y))
        return action

    
        