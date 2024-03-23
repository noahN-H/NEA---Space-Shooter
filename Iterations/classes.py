import pygame
import random
import math


clock = pygame.time.Clock()
        

class player():
    def __init__ (self, xPos, yPos, vel, hp, Pw, Pl):        
        self.xPos = xPos
        self.yPos = yPos
        self.vel = vel
        self.hp = hp        
        self.Pw = Pw
        self.Pl = Pl
    
    def getCoords(self):
        return self.xPos, self.yPos 
    
    def updateCoords(self, newPx, newPy):
        self.xPos = newPx
        self.yPos = newPy
        

    def pMovement(self):
        #Player Movement   
        keys = pygame.key.get_pressed()
        clock.tick(60)

        if keys[pygame.K_a] and self.xPos > self.vel:
            self.xPos -= self.vel

        if keys[pygame.K_d] and self.xPos <= (990) - self.Pw: # stops the player from moving 10px away from the edge of the screen
            self.xPos += self.vel

        if keys[pygame.K_w] and self.yPos > self.vel:
            self.yPos -= self.vel

        if keys[pygame.K_s] and self.yPos <= (740) - self.Pw: # stops the player from moving 10px away from the edge of the screen
            self.yPos += self.vel
            
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
        radius = random.randint(250,500)
        self.ExPos = random.randint(-250,250)
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

class spaceLazer():
    def __init__(self, colour, lVel, lDam, lCentre, lRadius):
        self.colour = colour
        self.LxPos = 0
        self.LyPos = 0
        self.LxVel = 0
        self.LyVel = 0

        self.lVel = lVel
        self.lDam = lDam
        self.lCentre = lCentre
        self.lRadius = lRadius
        self.rect = None
        
    def lSpawn(self, PxPos, PyPos, mouseX, mouseY):
        xGrad = mouseX - PxPos
        yGrad = mouseY - PyPos
        self.LxPos = xGrad
        self.LyPos = yGrad
        radius = math.sqrt(self.LxPos**2 + self.LyPos**2) 
        LvelRat = self.lVel/radius
        
        self.LxVel = self.LxPos * LvelRat
        self.LyVel = self.LyPos * LvelRat
        self.LxPos = self.LxPos + PxPos
        self.LyPos = self.LyPos + PyPos
        
    
        self.rect = pygame.Rect(self.LxPos, self.LyPos, self.lCentre, self.lRadius)
 
    def lMove(self):
        self.LxPos = self.LxPos + self.LxVel
        self.LyPos = self.LyPos + self.LyVel
        self.rect = pygame.Rect(self.LxPos, self.LyPos,self.lCentre, self.lRadius)
        
    def lDraw (self, screen):
        pygame.draw.rect(screen, self.colour, self.rect)

    def getRektL(self):
        return self.rect
    
    def lGetmouseCoords(self):
        mouseX = pygame.mouse.get_pos()[0]
        mouseY = pygame.mouse.get_pos()[1]
        return mouseX, mouseY
    
            
        
        
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

    
        