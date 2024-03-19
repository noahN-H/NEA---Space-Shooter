    '''    

    spawnTime = random.randint(1000,1001)
    gameTime = pygame.time.get_ticks()
    startTime = 0
    enemySpawnTimer = False
    
    
        #Enemy spawning
        spawnTime = random.randint(5000,7500)            
        if spawnTimer == spawnTime:
            spawnTimer -= spawnTime
            print("work")
            if gameTime < 30000:
                toSpawn = lvl1Enemy
                screen_1.blit(toSpawn)
            elif gameTime < 60000:
                toSpawn = random.choice(lvl1Enemy, lvl2Enemy)
                screen_1.blit(toSpawn)                
            else:
                toSpawn = random.choice(lvl1Enemy, lvl2Enemy, lvl3Enemy)
                screen_1.blit(toSpawn)  
            newEnemy = classes.enemy(toSpawn[0], toSpawn[1], toSpawn[2], toSpawn[3], toSpawn[4], toSpawn[5])
            newEnemy.eSpawn(player.getCoords())
            enemyList.append(newEnemy)
            print(enemyList)
              
        
        #enemy Movement
        for enemy in enemyList:
            enemy.eMove()
            enemy.eDraw(screen_1)
            print("spawn")
        
            
                    
            #event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit

        
        pygame.display.update()    
'''
