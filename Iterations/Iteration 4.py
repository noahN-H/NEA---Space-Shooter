import pygame
import classes
import random
import math


# variables
white = (255,255,255)
black = (0,0,0)
lBlue = (0,183,239)
red = (237,28,36)
orange = (255, 194, 14)
yellow = (255,242,0)


pygame.init()


clock = pygame.time.Clock()
width = 1000
height = 750


screen_1 = pygame.display.set_mode((width,height))
pygame.display.set_caption("Space Shooter")

#buttons Images

#Menu Images
startImage = pygame.image.load("Used Images/Strat Button.png").convert_alpha() 
instructionsImage = pygame.image.load("Used Images/Instructions_Button.png").convert_alpha()
exitImage = pygame.image.load("Used Images/Exit_Button.png").convert_alpha()
backImage = pygame.image.load("Used Images/Back_Button.png").convert_alpha()
titleImage = pygame.image.load("Used Images/Title.png").convert_alpha()
leaderboardImage = pygame.image.load("Used Images/Leaderboard_Button.png").convert_alpha()    
ResumeImage = pygame.image.load("Used Images/Resume Button .png").convert_alpha() 
MainMenuImage = pygame.image.load("Used Images/Main Menu Button.png").convert_alpha() 
GameoverImage = pygame.image.load("Used Images/Gameover.png").convert_alpha() 


#Countdown Images
numberOneImage = pygame.image.load("Used Images/no 1.png").convert_alpha()
numberTwoImage = pygame.image.load("Used Images/no 2.png").convert_alpha()
numberThreeImage = pygame.image.load("Used Images/no 3.png").convert_alpha()

#lifes Couter Images

threeLifesImage = pygame.image.load("Used Images/Threelifes.png").convert_alpha() 
twoLifesImage  =  pygame.image.load("Used Images/Twolifes.png").convert_alpha() 
oneLifeImage = pygame.image.load("Used Images/Onelife.png").convert_alpha() 
zeroLifesImage = pygame.image.load("Used Images/Zerolifes.png").convert_alpha() 

#Backgrounes
spaceBG = pygame.image.load("Used Images/SpaceBG.png").convert_alpha()
instructionsBG = pygame.image.load("Used Images/Instructions Screen.png").convert_alpha()

#loading the the sprites/making them work

#Title Page
bigTitle = pygame.transform.scale(titleImage, (int(width * .75), (int(height * .35))))

#Main Menu
title = pygame.transform.scale(titleImage, (int(width * .75), (int(height * .35))))
startButton = classes.button(200, 300, startImage,7)
instructionsButtonMain = classes.button(200, 400, instructionsImage,7)
leaderboardButton = classes.button(200,500, leaderboardImage,7)
exitButton = classes.button(200, 650,exitImage,7)

#Pause Menu
resumeButton = classes.button(200,200, ResumeImage, 7)
instructionsButtonPause = classes.button(200, 300, instructionsImage,7)     
MainMenuButton = classes.button(200,500, MainMenuImage, 7)
Gameover = pygame.transform.scale(GameoverImage, (int(width * .5), (int(height * .25))))


#Back Button
backButton = classes.button(50,50, backImage, 5)

#Countdown
number1 = pygame.transform.scale(numberOneImage, (int(width * .5), (int(height * .9))))
number2 = pygame.transform.scale(numberTwoImage, (int(width * .5), (int(height * .9))))
number3 = pygame.transform.scale(numberThreeImage, (int(width * .5), (int(height * .9))))   

#Lifes Counter
lifes3 =pygame.transform.scale(threeLifesImage, (int(width * .2), (int(height * .125))))
lifes2 =pygame.transform.scale(twoLifesImage, (int(width * .2), (int(height * .125))))
lifes1 =pygame.transform.scale(oneLifeImage, (int(width * .2), (int(height * .125))))
lifes0 =pygame.transform.scale(zeroLifesImage, (int(width * .2), (int(height * .125))))


def titleScreen():
    start_time = pygame.time.get_ticks() # used to get the inital time for when it is run
    while True:
        screen_1.blit(spaceBG,(0,0)) # blitting background onto the screen
        screen_1.blit(bigTitle,(121, 200)) # blitting title onto the screen
        pygame.display.update()

        current_time = pygame.time.get_ticks()
        if current_time - start_time >= 3000:  # will switch screen after 3000 milliseconds = 3 seconds
            mainMenu()  
        
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
            countOne() # remember to changgeback to countOne()
            
        if instructionsButtonMain.draw(screen_1) == True:
            print("Instructions") 
            instructionsScreen4Menu() # switches to the instructions screen

        
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
            mainMenu() # switches to the main menu screen

        
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
            break
        
    #event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                raise SystemExit

        pygame.display.update() 

def countOne():
    start_time = pygame.time.get_ticks() #gets the inital time when the function is run
    while True:
        screen_1.blit(spaceBG,(0,0))
        screen_1.blit(number3, (250, 15))
        pygame.display.update()
        
            
        current_time = pygame.time.get_ticks() # gets the time of the current time a few milliseconds after the last time
        if current_time - start_time >= 1000: # checks if one second has passed since the function was first run. it does this by taking the current time variable and minusing the time when the function was first run
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
        
            
        current_time = pygame.time.get_ticks()
        if current_time - start_time >= 1000:  
            countThree()  
            
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

def mainGame():
    playerHP = 3
    player = classes.player(500,375,5,1,3,45,45) #initalises the player

    lvl1EnemyRect = pygame.Rect(random.randint(50,950), random.randint(50,700), 45, 45) #initalises the enemies
    lvl2EnemyRect = pygame.Rect(random.randint(50,950), random.randint(50,700), 45, 45) #initalises the enemies
    lvl3EnemyRect = pygame.Rect(random.randint(50,950), random.randint(50,700), 50, 50) #initalises the enemies
    
    
    while True:
        screen_1.blit(spaceBG,(0,0))
        fullHealth = screen_1.blit(lifes3, (25,25)) # blits the health bar onto the screen
        twoHealth = screen_1.blit(lifes2, (25,25))
        oneHealth = screen_1.blit(lifes3, (25,25))        
        
        playerRect = pygame.Rect(player.xPos, player.yPos, player.Pw, player.Pl) # drawing the player onto the screen
        pygame.draw.rect(screen_1, (lBlue), playerRect)

        pygame.draw.rect(screen_1, (yellow), lvl1EnemyRect) #drawing enemies onto the screen
        pygame.draw.rect(screen_1, (orange), lvl2EnemyRect)
        pygame.draw.rect(screen_1, (red), lvl3EnemyRect)    


        if pygame.Rect.colliderect(lvl1EnemyRect, lvl2EnemyRect) or pygame.Rect.colliderect(lvl1EnemyRect, lvl3EnemyRect):
                del lvl1EnemyRect
                lvl1EnemyRect = pygame.Rect(random.randint(50,950), random.randint(50,700), 45, 45)
                
        if pygame.Rect.colliderect(lvl1EnemyRect, lvl2EnemyRect) or pygame.Rect.colliderect(lvl2EnemyRect, lvl3EnemyRect):
            del lvl2EnemyRect
            lvl2EnemyRect = pygame.Rect(random.randint(50,950), random.randint(50,700), 45, 45)
            
        if pygame.Rect.colliderect(lvl1EnemyRect, lvl3EnemyRect) or pygame.Rect.colliderect(lvl2EnemyRect, lvl3EnemyRect):
                del lvl3EnemyRect
                lvl3EnemyRect = pygame.Rect(random.randint(50,950), random.randint(50,700), 50, 50)
            
        if pygame.Rect.colliderect(playerRect, lvl1EnemyRect): # checks for a collision between player and enemy
            playerHP = playerHP - 1
            print(playerHP)
            del lvl1EnemyRect
            lvl1EnemyRect = pygame.Rect(random.randint(50,950), random.randint(50,700), 45, 45)
            if pygame.Rect.colliderect(lvl1EnemyRect, lvl2EnemyRect) or (lvl1EnemyRect, lvl3EnemyRect):
                del lvl1EnemyRect
                lvl1EnemyRect = pygame.Rect(random.randint(50,950), random.randint(50,700), 45, 45)

        elif pygame.Rect.colliderect(playerRect, lvl2EnemyRect):
            playerHP = playerHP - 1
            print(playerHP)
            del lvl2EnemyRect
            lvl2EnemyRect = pygame.Rect(random.randint(50,950), random.randint(50,700), 45, 45)
            if pygame.Rect.colliderect(lvl1EnemyRect, lvl2EnemyRect) or (lvl2EnemyRect, lvl3EnemyRect):
                del lvl2EnemyRect
                lvl2EnemyRect = pygame.Rect(random.randint(50,950), random.randint(50,700), 45, 45)

        
        elif pygame.Rect.colliderect(playerRect, lvl3EnemyRect):
            playerHP = playerHP - 1
            print(playerHP)
            del lvl3EnemyRect
            lvl3EnemyRect = pygame.Rect(random.randint(50,950), random.randint(50,700), 50, 50)
            if pygame.Rect.colliderect(lvl1EnemyRect, lvl3EnemyRect) or (lvl2EnemyRect, lvl3EnemyRect):
                del lvl3EnemyRect
                lvl3EnemyRect = pygame.Rect(random.randint(50,950), random.randint(50,700), 50, 50)
            
            

        if playerHP  == 3:
            fullHealth = screen_1.blit(lifes3, (25,25))
            
        elif playerHP == 2:
            del fullHealth
            twoHealth = screen_1.blit(lifes2, (25,25))
            
        elif playerHP == 1:
            del twoHealth
            oneHealth = screen_1.blit(lifes1, (25,25)) 
            
        elif playerHP == 0:
            del oneHealth
            screen_1.blit(lifes0, (25,25))
            gameoverTimer = pygame.time.wait(1000)
            if gameoverTimer > 1000:
                gameover()
                
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit
                    
        pygame.display.update()
    
        pMovement(player) 

def pMovement(player):
    clock.tick(60)
    #Player Movement    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and player.xPos > player.vel:
        player.xPos -= player.vel

    if keys[pygame.K_d] and player.xPos <= (width - 10) - player.Pw:
        player.xPos += player.vel

    if keys[pygame.K_w] and player.yPos > player.vel:
        player.yPos -= player.vel

    if keys[pygame.K_s] and player.yPos <= (height - 1) - player.Pw:
        player.yPos += player.vel
        
    if keys[pygame.K_ESCAPE]:
        pauseMenu()

def gameover():
    start_time = pygame.time.get_ticks()
    while True:
        screen_1.blit(spaceBG,(0,0))
        
        screen_1.blit(Gameover, (250, 250))
        
        current_time = pygame.time.get_ticks()
        if current_time - start_time >= 5000:  
            mainMenu() 
            
        #event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit
            
        pygame.display.update()
                                 
def pauseMenu():
    while True: 
        
        screen_1.blit(spaceBG,(0,0))
        
        if resumeButton.draw(screen_1) == True:
            break
            print("Resume")
        
        if instructionsButtonPause.draw(screen_1) == True:
            instructionsScreen4Game()
            print("Instructions")

        if MainMenuButton.draw(screen_1) == True:
            mainMenu()
            print("Main Menu")            
            
        if exitButton.draw(screen_1) == True:
            print("EXIT")
            raise SystemExit
        
    #event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit
            
        pygame.display.update()
                            

run = True
while run:
    mainGame() #change back to title screen when done
pygame.quit() 
