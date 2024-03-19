import pygame

#classes
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

    