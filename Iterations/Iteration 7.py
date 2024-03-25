import pygame
import classes
import random
import os



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
lifes3 = pygame.transform.scale(threeLifesImage, (int(width * .2), (int(height * .125))))
lifes2 = pygame.transform.scale(twoLifesImage, (int(width * .2), (int(height * .125))))
lifes1 = pygame.transform.scale(oneLifeImage, (int(width * .2), (int(height * .125))))

#Fonts
defultFont4Game = pygame.font.Font("freesansbold.ttf", 16)
defultFont4Leaderboard = pygame.font.Font("freesansbold.ttf", 32)


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

            countOne() 
            
        if instructionsButtonMain.draw(screen_1) == True:

            instructionsScreen() # switches to the instructions screen

        if leaderboardButton.draw(screen_1) == True:

            leaderboard()

            
        if exitButton.draw(screen_1) == True:

            raise SystemExit
                        
    #event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                raise SystemExit

        pygame.display.update() 

def instructionsScreen():
    while True:
        screen_1.blit(instructionsBG,(0,0))
        if backButton.draw(screen_1) == True:

            break# switches to the main menu screen
        
    #event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                raise SystemExit

        pygame.display.update() 

def leaderboardRecord(points, time): 
    lbPFileR = open("LeaderboardPoints.txt","r")
    
    insertionlbP = lbPFileR.readlines(10)
    cleanedUplbP = []
    for score in insertionlbP:
        score = score.strip("\n")
        cleanedUplbP.append(int(score))
    
    orderedpointsScore = []
    if len(cleanedUplbP) == 0:
        orderedpointsScore.append(points)
    else:
        counter = len(cleanedUplbP) - 1
        hasAdded = False
        while len(orderedpointsScore) < 10 and counter > 0:
            print(counter)
        
            orderedpointsScore.append(str(insertionlbP[counter]) + "\n")
            counter -= 1
            if int(insertionlbP[counter]) < int(points) and not hasAdded:
                orderedpointsScore.append(str(points) + "\n")
                hasAdded = True
    lbPFileR.close()
    lbPFileR = open("LeaderboardPoints.txt","w")
    for point in orderedpointsScore:
        print(point)
        lbPFileR.write(str(point))
    lbPFileR.close()
     
    
    lbTFileR = open("LeaderboardTime.txt","r")    
    insertionlbT = lbTFileR.readlines(10)
    cleanedUplbT = []
    for score in insertionlbT:
        score = score.strip("\n")
        print(score)
        cleanedUplbT.append(int(score))
    
    orderedTimeScore = []
    if len(cleanedUplbP) == 0:
        orderedTimeScore.append(time)
    else:
        counter = len(cleanedUplbP) - 1
        hasAdded = False
        while len(orderedTimeScore) < 10 and counter > 0:
            
            orderedTimeScore.append(str(insertionlbT[counter]) + "\n")
            counter -= 1
            if int(insertionlbT[counter]) < int(time) and not hasAdded:
                orderedTimeScore.append(str(time) + "\n")
                hasAdded = True

    lbTFileR.close()
    lbTFileR = open("LeaderboardPoints.txt","w")
    for point in orderedTimeScore:
        lbTFileR.write(str(time))
    lbTFileR.close()
         

    
    lbPFileA = open("LeaderboardPoints.txt","a")
    lbTFileA = open("LeaderboardTime.txt","a")

    lbTFileA.write(str(time) +  "\n")
    lbPFileA.write(str(points) + "\n")
    
def leaderboard():
    running = True    
    lbPFileA = open("LeaderboardPoints.txt","r")
    lbTFileA = open("LeaderboardTime.txt","r")

    # Seperates the lines in thhe text file
    pointsScore1 = lbPFileA.readline(1)
    pointsScore2 = lbPFileA.readline(2)
    pointsScore3 = lbPFileA.readline(3)
    pointsScore4 = lbPFileA.readline(4)
    pointsScore5 = lbPFileA.readline(5)
    pointsScore6 = lbPFileA.readline(6)
    pointsScore7 = lbPFileA.readline(7)
    pointsScore8 = lbPFileA.readline(8)
    pointsScore9 = lbPFileA.readline(9)
    pointsScore10 = lbPFileA.readline(10)
    
    pointsTime1 = lbTFileA.readline(1)
    pointsTime2 = lbTFileA.readline(2)
    pointsTime3 = lbTFileA.readline(3)
    pointsTime4 = lbTFileA.readline(4)
    pointsTime5 = lbTFileA.readline(5)
    pointsTime6 = lbTFileA.readline(6)
    pointsTime7 = lbTFileA.readline(7)
    pointsTime8 = lbTFileA.readline(8)
    pointsTime9 = lbTFileA.readline(9)
    pointsTime10 = lbTFileA.readline(10)
    
    
    # puts each line into a array to be easily accessed
    pointsScoreList = [pointsScore1, pointsScore2, pointsScore3, pointsScore4, pointsScore5, pointsScore6, pointsScore7, pointsScore8, pointsScore9, pointsScore10]
    pointsTimeList = [pointsTime1, pointsTime2, pointsTime3, pointsTime4, pointsTime5, pointsTime6, pointsTime7, pointsTime8, pointsTime9, pointsTime10]
    cleanedPointsScoreList = pointsScoreList
    cleanedTimeScoreList = pointsTimeList
    while running == True:
        screen_1.blit(spaceBG,(0,0))
        
        if backButton.draw(screen_1) == True:
            running = False
    
        showStat(250, 50, "", "|--|SCORE HIGHSCORE|--|", "" )
        showStat(250, 100, cleanedPointsScoreList[0], "", "" )
        showStat(250, 150, cleanedPointsScoreList[1], "", "" )
        showStat(250, 200, cleanedPointsScoreList[2], "", "" )
        showStat(250, 250, cleanedPointsScoreList[3], "", "" )
        showStat(250, 300, cleanedPointsScoreList[4], "", "" )
        showStat(250, 350, cleanedPointsScoreList[5], "", "" )
        showStat(250, 400, cleanedPointsScoreList[6], "", "" )
        showStat(250, 450, cleanedPointsScoreList[7], "", "" )
        showStat(250, 500, cleanedPointsScoreList[8], "", "" )
        showStat(250, 550, cleanedPointsScoreList[9], "", "" )
        
        showStat(750, 50, "", ".__.TIME HIGHSCORE.__.", "" )
        showStat(750, 100 ,cleanedTimeScoreList[0], "", "" )
        showStat(750, 150, cleanedTimeScoreList[1], "", "" )
        showStat(750, 200, cleanedTimeScoreList[2], "", "" )
        showStat(750, 250, cleanedTimeScoreList[3], "", "" )
        showStat(750, 300, cleanedTimeScoreList[4], "", "" )
        showStat(750, 350, cleanedTimeScoreList[5], "", "" )
        showStat(750, 400, cleanedTimeScoreList[6], "", "" )
        showStat(750, 450, cleanedTimeScoreList[7], "", "" )
        showStat(750, 500, cleanedTimeScoreList[8], "", "" )
        showStat(750, 550, cleanedTimeScoreList[9], "", "" )
        
    
        # Event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

        pygame.display.update()        

def countOne():
    start_time = pygame.time.get_ticks() #gets the inital time when the function is run
    running = True 
    while running == True:
        screen_1.blit(spaceBG,(0,0))
        screen_1.blit(number3, (250, 15))

        
            
        current_time = pygame.time.get_ticks() # gets the time of the current time a few milliseconds after the last time
        if current_time - start_time >= 1000: # checks if one second has passed since the function was first run. it does this by taking the current time variable and minusing the time when the function was first run
            running = False
                            
            # Event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

        pygame.display.update()        

    countTwo()  

def countTwo():
    start_time = pygame.time.get_ticks()
    running = True
    while running == True:
        screen_1.blit(spaceBG,(0,0))
        screen_1.blit(number2, (250,15)) 

        
            
        current_time = pygame.time.get_ticks()
        if current_time - start_time >= 1000:  
            running =  False
            # Event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
        pygame.display.update()      

    countThree()
          
def countThree():
    start_time = pygame.time.get_ticks()
    running = True
    while running == True:
        screen_1.blit(spaceBG,(0,0))
        screen_1.blit(number1, (250, 15))
        
        current_time = pygame.time.get_ticks()
        if current_time - start_time >= 1000:  
            running = False
            
            
            # Event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

        pygame.display.update()        
    mainGame() 

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
    
    running = True
    
    points = 0

    
    while running == True:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pauseMenu() 
            
               
        clock.tick(60)
        time = pygame.time.get_ticks() - gameStartTime #resets a time at the time when the mainGame loop is run
        screen_1.blit(spaceBG,(0,0))
        
        
        playerRect = pygame.Rect(player.xPos, player.yPos, player.Pw, player.Pl) # drawing the player onto the screen
        pygame.draw.rect(screen_1, (lBlue), playerRect)

        if difficulty(time) == 1: # for the first 30 seconds this is what is run
            if time%100 == 0 and len(enemyList) < 10: #checks if 5 seconds has passes and there is less than 5 enemies on the screen
                pCoords = player.getCoords() #gets the players coordinates at those 5 seconds
                newlvl1Enemy = classes.enemy(yellow, 3, 5, 1, 45, 45, 1) #instatiates the enemy
                newlvl1Enemy.eSpawn(pCoords[0],pCoords[1]) #spawns in the enemy centred at the players location
                enemyList.append(newlvl1Enemy) #adds the enemy to the enemy list to keep track of how many enemies are on the screem         
        
        if difficulty(time) == 2:
            if time%100 == 0 and len(enemyList) < 12:
                pCoords = player.getCoords()
                newlvl1Enemy = classes.enemy(yellow, 3, 1, 1, 45, 45, 1)
                newlvl1Enemy.eSpawn(pCoords[0],pCoords[1])
                
                newlvl2Enemy = classes.enemy(orange, 5, 1, 1, 45, 45, 3)
                newlvl2Enemy.eSpawn(pCoords[0],pCoords[1])
                
                diff2List = [newlvl1Enemy, newlvl2Enemy] # allows for a choice between either a lvl1 or a lvl2 enemy to be drawn on the screen
                enemyList.append(random.choice(diff2List))
        
        if difficulty(time) == 3:
            if time%100 == 0 and len(enemyList) < 15:
                pCoords = player.getCoords()
                newlvl1Enemy = classes.enemy(yellow, 3, 1, 1, 45, 45, 1)
                newlvl1Enemy.eSpawn(pCoords[0],pCoords[1])
                
                newlvl2Enemy = classes.enemy(orange, 5, 1, 1, 45, 45, 3)
                newlvl2Enemy.eSpawn(pCoords[0],pCoords[1])
                
                newlvl3Enemy = classes.enemy(red, 2, 2, 2, 75, 75, 5)
                newlvl3Enemy.eSpawn(pCoords[0],pCoords[1])
                
                diff3List = [newlvl1Enemy, newlvl2Enemy, newlvl3Enemy]
                enemyList.append(random.choice(diff3List))
                
        if difficulty(time) == 4:
            if time%10 == 0 and len(enemyList) < 30:
                pCoords = player.getCoords()
                newlvl1Enemy = classes.enemy(yellow, 3, 1, 1, 45, 45, 1)
                newlvl1Enemy.eSpawn(pCoords[0],pCoords[1])
                
                newlvl2Enemy = classes.enemy(orange, 5, 1, 1, 45, 45, 3)
                newlvl2Enemy.eSpawn(pCoords[0],pCoords[1])
                
                newlvl3Enemy = classes.enemy(red, 2, 2, 2, 75, 75, 5)
                newlvl3Enemy.eSpawn(pCoords[0],pCoords[1])
                
                diff3List = [newlvl1Enemy, newlvl2Enemy, newlvl3Enemy]
                enemyList.append(random.choice(diff3List))      
        
        for enemy in enemyList:
            enemy.eDraw(screen_1)
            enemy.eMove()
            if pygame.Rect.colliderect(playerRect, enemy):

                playerHP = playerHP - enemy.Edam
                enemyList.remove(enemy)
                pygame.time.wait(2000)
                enemyList.clear()
                player.updateCoords(500, 375)

  
                
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
                        
        for spaceLazer in lazerList:
            lCentre = (spaceLazer.LxPos, spaceLazer.LyPos)
            spaceLazer.lMove()
            lazerRect = pygame.draw.circle(screen_1, green, lCentre, spaceLazer.lRadius)
            
            for enemy in enemyList:
                if pygame.Rect.colliderect(lazerRect, enemy):

                    enemy.eDamage(spaceLazer.lDam)
                    lazerList.remove(spaceLazer)
                    del spaceLazer
                    if enemy.returnEhp() == 0:
                        points = points + enemy.ePoints
                        enemyList.remove(enemy)

                        del enemy
                        print(points)
                        
        # checks if mouse buttons have been pressed    
        for event in pygame.event.get():        
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                spaceLazer = classes.spaceLazer(green, 5, 1, 5, 7.5)
                pCoords = player.getCoords() #gets the players coordinates at those 5 seconds
                spaceLazer.lSpawn(pCoords[0],pCoords[1], mousePos[0], mousePos[1])
                spaceLazer.lDraw(screen_1)
                lazerList.append(spaceLazer)
                
        showStat(750, 25, points, "Score: ", "")
        showStat(750, 50, (time // 1000), "Time Alive: ", " Seconds " )            
        if playerHP == 3:
            screen_1.blit(lifes3, (25,25))

        elif playerHP == 2:

            screen_1.blit(lifes2, (25,25))
            
        elif playerHP == 1:
            screen_1.blit(lifes1, (25,25)) 
            
        elif playerHP <= 0:
            pygame.time.wait(1000)
            running = False
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
                    
        pygame.display.update()
        player.pMovement()


    
    
#    initals = input("Input your initals: ")
#    showStat(500, 100, initals, "", "")
#    if len(initals) == 3:
#        return initals
        
    finalScore = points # creates final score
    timeAlive = time//1000 # shows seconds rather than milliseconnds
    leaderboardRecord(finalScore,timeAlive) # allows types of score to be shown
    
    
    gameover()
   
def lifeLost():
    while True:
        screen_1.blit(spaceBG,(0,0))
        pygame.time.wait(2000)
        break

def showStat(x, y, stat, text1, text2):
    statRenderMG = defultFont4Game.render(text1 + str(stat) + text2 ,True, white)
    screen_1.blit(statRenderMG, (x, y))
    
    statRenderLB = defultFont4Game.render(text1 + str(stat) + text2 ,True, white)
    screen_1.blit(statRenderLB, (x, y))
    
def gameover():
    start_time = pygame.time.get_ticks()
    running = True
    
    while running == True:
        screen_1.blit(spaceBG,(0,0))
        
        screen_1.blit(Gameover, (250, 250)) # blits gameover onto the screen
        
        current_time = pygame.time.get_ticks()
        if current_time - start_time >= 5000:  
            running = False
            
        #event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit
                
        pygame.display.update()
    

    leaderboard()
                  
def pauseMenu():
    while True: 
        
        screen_1.blit(spaceBG,(0,0))
        
        if resumeButton.draw(screen_1) == True:

            break
        
        if instructionsButtonPause.draw(screen_1) == True:
            instructionsScreen()


        if MainMenuButton.draw(screen_1) == True:
            mainMenu()
         
            
        if exitButton.draw(screen_1) == True:

            raise SystemExit
        
    #event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit
            
        pygame.display.update()
                            

run = True
while run:
    mainMenu()
pygame.quit() 