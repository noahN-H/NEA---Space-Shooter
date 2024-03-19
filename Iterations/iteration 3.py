import pygame
import classes

# variables
white = (255,255,255)

pygame.init()

clock = pygame.time.Clock()
width = 1000
height = 750


screen_1 = pygame.display.set_mode((width,height))
pygame.display.set_caption("Space Shooter")

#buttons Images

#Main Menu Images
startImage = pygame.image.load("Used Images/Strat Button.png").convert_alpha() 
instructionsImage = pygame.image.load("Used Images/Instructions_Button.png").convert_alpha()
exitImage = pygame.image.load("Used Images/Exit_Button.png").convert_alpha()
backImage = pygame.image.load("Used Images/Back_Button.png").convert_alpha()
titleImage = pygame.image.load("Used Images/Title.png").convert_alpha()
leaderboardImage = pygame.image.load("Used Images/Leaderboard_Button.png").convert_alpha()    

#Countdown Images
numberOneImage = pygame.image.load("Used Images/no 1.png").convert_alpha()
numberTwoImage = pygame.image.load("Used Images/no 2.png").convert_alpha()
numberThreeImage = pygame.image.load("Used Images/no 3.png").convert_alpha()


#Backgrounes
spaceBG = pygame.image.load("Used Images/SpaceBG.png").convert_alpha()
instructionsBG = pygame.image.load("Used Images/Instructions Screen.png").convert_alpha()

#loading the the sprites/making them work

#Title Page
bigTitle = pygame.transform.scale(titleImage, (int(width * .75), (int(height * .35))))

#Main Menu Buttons
title = pygame.transform.scale(titleImage, (int(width * .75), (int(height * .35))))
startButton = classes.button(200, 300, startImage,7)
instructionsButton = classes.button(200, 400, instructionsImage,7)    
leaderboardButton = classes.button(200,500, leaderboardImage,7)
exitButton = classes.button(200, 650,exitImage,7)


#Back Button
backButton = classes.button(50,50, backImage, 5)

#Countdown
number1 = pygame.transform.scale(numberOneImage, (int(width * .5), (int(height * .9))))
number2 = pygame.transform.scale(numberTwoImage, (int(width * .5), (int(height * .9))))
number3 = pygame.transform.scale(numberThreeImage, (int(width * .5), (int(height * .9))))   


def titleScreen():
    start_time = pygame.time.get_ticks()
    while True:
        screen_1.blit(spaceBG,(0,0))
        screen_1.blit(bigTitle,(121, 200))
        pygame.display.update()
        
        # Check if 3 seconds have passed
        current_time = pygame.time.get_ticks()
        if current_time - start_time >= 3000:  # 3000 milliseconds = 3 seconds
            mainMenu()  # Switch to the main menu
        
        # Event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

        pygame.display.update()


def mainMenu():
    while True:        
        screen_1.blit(spaceBG,(0,0))
        screen_1.blit(title,(121, 15))
        
        
        if startButton.draw(screen_1) == True:
            print("START")
            countOne()
            
        if instructionsButton.draw(screen_1) == True:
            instructionsScreen4Menu()
            print("Instructions")
        
        if leaderboardButton.draw(screen_1) == True:
            print("Leaderboard")   
            
        if exitButton.draw(screen_1) == True:
            print("EXIT")
            raise SystemExit
                        
    #event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                raise SystemExit

        pygame.display.update() 

def instructionsScreen4Menu():
    while True:
        screen_1.blit(instructionsBG,(0,0))
        if backButton.draw(screen_1) == True:
            print("Back")
            mainMenu()
        
    #event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                raise SystemExit

        pygame.display.update() 

def instructionsScreen4Game():
    while True:
        screen_1.blit(instructionsBG,(0,0))
        if backButton.draw(screen_1) == True:
            print("Back")
            pauseMenu()
        
    #event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                raise SystemExit

        pygame.display.update() 


def countOne():
    start_time = pygame.time.get_ticks()
    while True:
        screen_1.blit(spaceBG,(0,0))
        screen_1.blit(number3, (250, 15))
        pygame.display.update()
        
            
        current_time = pygame.time.get_ticks()
        if current_time - start_time >= 1000: 
            countTwo()
                            
            # Event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

        pygame.display.update()        

def countTwo():
    start_time = pygame.time.get_ticks()
    while True:
        screen_1.blit(spaceBG,(0,0))
        screen_1.blit(number2, (250,15)) 
        pygame.display.update()
        
            # Check if 5 seconds have passed
        current_time = pygame.time.get_ticks()
        if current_time - start_time >= 1000:  # 5000 milliseconds = 5 seconds
            countThree()  # Switch to the main menu
            
            # Event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

def countThree():
    start_time = pygame.time.get_ticks()
    while True:
        screen_1.blit(spaceBG,(0,0))
        screen_1.blit(number1, (250, 15))
        pygame.display.update()
        
        current_time = pygame.time.get_ticks()
        if current_time - start_time >= 1000:  
            mainGame() 
            
            # Event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

        pygame.display.update()        
        pygame.display.update()        


def mainGame():
    while True:
        screen_1.blit(spaceBG,(0,0))

        movement() 
        
    #event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                raise SystemExit
            
            elif event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_ESCAPE:
                    pauseMenu()

            pygame.display.update()     

def movement():

    player = classes.player(100,100,5,1,3,50,50)

    run = True
    while run:
        clock.tick(60)

        screen_1.blit(spaceBG,(0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

        
    
            
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] and player.xPos > player.vel:
            player.xPos -= player.vel

        if keys[pygame.K_d] and player.xPos <= width - player.Pw:
            player.xPos += player.vel

        if keys[pygame.K_w] and player.yPos > player.vel:
            player.yPos -= player.vel

        if keys[pygame.K_s] and player.yPos <= height - player.Pw:
            player.yPos += player.vel

        pygame.draw.rect(screen_1, (2, 20, 200), (player.xPos, player.yPos, player.Pw, player.Pl))
        pygame.display.update()


    
    
    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

def pauseMenu():
    while run:
        
        screen_1.blit(spaceBG,(0,0))

        if instructionsButton.draw(screen_1) == True:
            instructionsScreen4Game()
            print("Instructions")
   
            
        if exitButton.draw(screen_1) == True:
            print("EXIT")
            raise SystemExit
                                
       

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit



run = True
while run:
    titleScreen()
pygame.quit() 