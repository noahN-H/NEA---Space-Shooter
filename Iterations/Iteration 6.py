import pygame
import classes
import random



# variables
white = (255,255,255)
black = (0,0,0)
lBlue = (0,183,239)
red = (237,28,36)
orange = (255, 194, 14)
yellow = (255,242,0)
green =  (34,177,78)


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
lifes1 = pygame.transform.scale(oneLifeImage, (int(width * .2), (int(height * .125))))



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

def difficulty(time):
    difficulty = 0
    
    if time >=120000:
        difficulty =  4
        
    elif time >= 60000:
        difficulty = 3
    
    elif time >= 30000:
        difficulty = 2
        
    else:
        difficulty = 1
        
    return difficulty
    
def mainGame():

    playerHP = 3
    enemyList = []
    lazerList=[]
    
    gameStartTime = pygame.time.get_ticks()     
    player = classes.player(500,375,5,3,45,45) #initalises the player


    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_ESCAPE]:
        pauseMenu()    
    
    
    while True:
        clock.tick(60)
        time = pygame.time.get_ticks() - gameStartTime #resets a time at the time when the mainGame loop is run
        screen_1.blit(spaceBG,(0,0))
        
        
        playerRect = pygame.Rect(player.xPos, player.yPos, player.Pw, player.Pl) # drawing the player onto the screen
        pygame.draw.rect(screen_1, (lBlue), playerRect)
        

        
        for spaceLazer in lazerList:
            spaceLazer.lMove()
            spaceLazer.shoot(screen_1)
            pCoords = player.getCoords() #gets the players coordinates at those 5 seconds
            spaceLazer = (1, 5, 5, 10)
            if spaceLazer.lDraw ==True:
                print("True")    
                spaceLazer.lSpawn(pCoords[0],pCoords[1])
                spaceLazer.lDraw(screen_1)
                lazerList.append(spaceLazer)
            
            
            if pygame.Rect.collidepoint(spaceLazer, enemy):
                print("lazer collide")
                enemyList.remove(enemy)
                del enemy                
                
            

        if difficulty(time) == 1: # for the first 30 seconds this is what is run
            if time%100 == 0 and len(enemyList) < 10: #checks if 5 seconds has passes and there is less than 5 enemies on the screen
                pCoords = player.getCoords() #gets the players coordinates at those 5 seconds
                newlvl1Enemy = classes.enemy(yellow, 3, 1, 1, 45, 45) #instatiates the enemy
                newlvl1Enemy.eSpawn(pCoords[0],pCoords[1]) #spawns in the enemy centred at the players location
                enemyList.append(newlvl1Enemy) #adds the enemy to the enemy list to keep track of how many enemies are on the screem         
        
        if difficulty(time) == 2:
            if time%100 == 0 and len(enemyList) < 12:
                pCoords = player.getCoords()
                newlvl1Enemy = classes.enemy(yellow, 3, 1, 1, 45, 45)
                newlvl1Enemy.eSpawn(pCoords[0],pCoords[1])
                
                newlvl2Enemy = classes.enemy(orange, 5, 1, 1, 45, 45)
                newlvl2Enemy.eSpawn(pCoords[0],pCoords[1])
                
                diff2List = [newlvl1Enemy, newlvl2Enemy] # allows for a choice between either a lvl1 or a lvl2 enemy to be drawn on the screen
                enemyList.append(random.choice(diff2List))
        
        if difficulty(time) == 3:
            if time%100 == 0 and len(enemyList) < 15:
                pCoords = player.getCoords()
                newlvl1Enemy = classes.enemy(yellow, 3, 1, 1, 45, 45)
                newlvl1Enemy.eSpawn(pCoords[0],pCoords[1])
                
                newlvl2Enemy = classes.enemy(orange, 5, 1, 1, 45, 45)
                newlvl2Enemy.eSpawn(pCoords[0],pCoords[1])
                
                newlvl3Enemy = classes.enemy(red, 2, 2, 2, 75, 75)
                newlvl3Enemy.eSpawn(pCoords[0],pCoords[1])
                
                diff3List = [newlvl1Enemy, newlvl2Enemy, newlvl3Enemy]
                enemyList.append(random.choice(diff3List))
                
        if difficulty(time) == 4:
            if time%10 == 0 and len(enemyList) < 30:
                pCoords = player.getCoords()
                newlvl1Enemy = classes.enemy(yellow, 3, 1, 1, 45, 45)
                newlvl1Enemy.eSpawn(pCoords[0],pCoords[1])
                
                newlvl2Enemy = classes.enemy(orange, 5, 1, 1, 45, 45)
                newlvl2Enemy.eSpawn(pCoords[0],pCoords[1])
                
                newlvl3Enemy = classes.enemy(red, 2, 2, 2, 75, 75)
                newlvl3Enemy.eSpawn(pCoords[0],pCoords[1])
                
                diff3List = [newlvl1Enemy, newlvl2Enemy, newlvl3Enemy]
                enemyList.append(random.choice(diff3List))      
        
        for enemy in enemyList:
            enemy.eDraw(screen_1)
            enemy.eMove()
            if pygame.Rect.colliderect(playerRect, enemy):
                print("Hello 1")
                playerHP = playerHP - enemy.Edam
                enemyList.remove(enemy)
                pygame.time.wait(2000)
                enemyList.clear()
                player.updateCoords(500, 375)
                print("hello 2")
  
                
            if enemy.eGetCoords()[0] >= 1000:
                print("hello right")
                enemyList.remove(enemy)
                del enemy
            elif enemy.eGetCoords()[0] <= 0:
                print("hello left")
                enemyList.remove(enemy)
                del enemy            
            elif enemy.eGetCoords()[1] >= 750:
                print("hello down")     
                enemyList.remove(enemy)            
                del enemy           
            elif enemy.eGetCoords()[1] <= 0:
                print("hello up")                
                enemyList.remove(enemy)
                del enemy
                         
        if playerHP  == 3:
            screen_1.blit(lifes3, (25,25))

        elif playerHP == 2:

            screen_1.blit(lifes2, (25,25))
            
        elif playerHP == 1:

            screen_1.blit(lifes1, (25,25)) 
            
        elif playerHP <= 0:

            gameoverTimer = pygame.time.wait(1000)
            if gameoverTimer > 1000:
                gameover()
                
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit
                    
        pygame.display.update()
        player.pMovement() 

def lifeLost():
    while True:
        screen_1.blit(spaceBG,(0,0))
        pygame.time.wait(2000)
        break


def gameover():
    start_time = pygame.time.get_ticks()
    while True:
        screen_1.blit(spaceBG,(0,0))
        
        screen_1.blit(Gameover, (250, 250)) # blits gameover onto the screen
        
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
            print("Resume")
            break
        
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
    countThree()
pygame.quit() 
