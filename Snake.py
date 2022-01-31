# I - Import and Initialize
import pygame, mySprites,random,math
pygame.init()
             
def main():
    '''This function defines the 'mainline logic' for our game.'''
    # Display
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Snake")

     
    background = pygame.image.load("grass.png")
    background = background.convert()
    screen.blit(background, (0,0))    
    
    
    #Entities
    Cuckoo=pygame.mixer.Sound("Cuckoo.wav")
    Cuckoo.set_volume(1.0)
    
    Powerup=pygame.mixer.Sound("Powerup.wav")
    Powerup.set_volume(1.0)
    
    Laugh=pygame.mixer.Sound("pacman_eatfruit.wav")
    Laugh.set_volume(1.0)
    
    pygame.mixer.music.load("Chill.mp3")
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(-1)           
    

    EndGroup=pygame.sprite.Group()
    for y in range(4):
        EndGroup.add(mySprites.EndZone(screen,y)) 
    BodyGroup=pygame.sprite.Group()
    while True:
        xBall=random.randrange(20, screen.get_width()-20,20)
        yBall=random.randrange(60, screen.get_height()-20,20)
        if xBall!=screen.get_width()/2 and yBall!=screen.get_height()/2:
            ball=mySprites.Ball(screen)
            ball.setPosition(xBall,yBall)
            break
    player=mySprites.Head(screen)
    Score = mySprites.ScoreKeeper()
    allSprites = pygame.sprite.OrderedUpdates(EndGroup,ball,player,Score,BodyGroup)
    
 
    # ACTION
     
    # Assign 
    clock = pygame.time.Clock()
    keepGoing = True
    up=True
    left=True
    down=True
    right=True       
    play=1
    
    # Loop
    while keepGoing:
     
        # Time
        clock.tick(30)
     
        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and up == True:
                    player.go_up()
                    down=False
                    right=True
                    left=True
                    up=True
                if event.key == pygame.K_DOWN  and down == True:
                    player.go_down()
                    up=False
                    left=True
                    down=True
                    right=True                    
                if event.key == pygame.K_RIGHT and right == True:
                    player.go_right()
                    up=True
                    left=False
                    down=True
                    right=True 
                if event.key == pygame.K_LEFT and left == True:
                    player.go_left()
                    up=True
                    left=True
                    down=True
                    right=False
                if event.key== pygame.K_ESCAPE:
                    keepGoing=False
        
            
        if player.rect.colliderect(ball.rect):
            Segment=mySprites.Body(screen)
            BodyGroup.add(Segment)  
            ball.kill()
            Laugh.play()
            Score.player()
            ball=mySprites.Ball(screen)
            switch=True
            check=0
            while switch == True:
                #My attempt to make sure that the ball doesn't land on the body using distance formula.
                #The way the balls are placed is still alittle buggy and I don't know how to fix it.
                xBall=random.randrange(20, screen.get_width()-20,20 )
                yBall=random.randrange(60, screen.get_height()-20,20)
                for bodies in range(len(BodyGroup.sprites())-1,-1,-1):
                    if math.sqrt((BodyGroup.sprites()[bodies].get_centerx()-xBall)**2+(BodyGroup.sprites()[bodies].get_centery()-yBall)**2) >= 20:
                        check+=1
                        if check==len(BodyGroup.sprites()):
                            ball.setPosition(xBall,yBall)
                            switch=False
                    else:
                        break
            allSprites.add(ball,BodyGroup)

        
        #Collision with the head and the Border
        collision = pygame.sprite.spritecollide(player,EndGroup, False)
        if collision:
            Cuckoo.play()
            #Will reset the game
            for sprites in range(len(BodyGroup.sprites())-1,-1,-1):
                BodyGroup.sprites()[sprites].kill()            
            ball.kill()
            ball=mySprites.Ball(screen)
            player.kill()
            player=mySprites.Head(screen)
            while True:
                xBall=random.randrange(20, screen.get_width()-20,20)
                yBall=random.randrange(60, screen.get_height()-20,20)
                if xBall!=screen.get_width()/2 and yBall!=screen.get_height()/2:
                    ball=mySprites.Ball(screen)
                    ball.setPosition(xBall,yBall)
                    break
            allSprites.add(ball,player)
            Score.reset()
            play=1
            up=True
            left=True
            down=True
            right=True               
            
            
        #Collision with the head and the Bodygroup
        collide = pygame.sprite.spritecollide(player,BodyGroup, False)
        if collide:
            Cuckoo.play()
            #Will reset the game
            for sprites in range(len(BodyGroup.sprites())-1,-1,-1):
                BodyGroup.sprites()[sprites].kill()            
            ball.kill()
            ball=mySprites.Ball(screen)
            player.kill()
            player=mySprites.Head(screen)
            while True:
                xBall=random.randrange(20, screen.get_width()-20,20)
                yBall=random.randrange(60, screen.get_height()-20,20)
                if xBall!=screen.get_width()/2 and yBall!=screen.get_height()/2:
                    ball=mySprites.Ball(screen)
                    ball.setPosition(xBall,yBall)
                    break
            allSprites.add(ball,player)  
            Score.reset()
            play=1
            up=True
            left=True
            down=True
            right=True               
        
        
        #This for-loop controls the position of the body segments
        for index in range(len(BodyGroup.sprites())-1,0,-1):  
            x1=BodyGroup.sprites()[index-1].get_centerx()
            y1=BodyGroup.sprites()[index-1].get_centery()
            BodyGroup.sprites()[index].set_position(x1,y1)               

        #This if-statement controls the first body segment and is used to 
        #update all the other segments  
        if len(BodyGroup.sprites()) > 0:
            x=player.get_x()
            y=player.get_y()
            BodyGroup.sprites()[0].set_position(x,y)                       
        
        #The speed is adjusted by using delay.  Each time the player reaches
        #a certain score, the game gets a bit faster
        if Score.get_score()<=10:
            pygame.time.delay(150)
        elif Score.get_score()>=11 and Score.get_score()<=30:
            if Score.get_score()==11 and play==1:
                Powerup.play()
                play+=1
            pygame.time.delay(120)
        elif Score.get_score()>=31 and Score.get_score()<=50:
            if Score.get_score()==31 and play==2:
                Powerup.play()
                play+=1
            pygame.time.delay(90)
        elif Score.get_score()>=51 and Score.get_score()<=70:
            if Score.get_score()==51 and play==3:
                Powerup.play()
                play+=1
            pygame.time.delay(60)
        elif Score.get_score()>=71 and Score.get_score()<=90:
            if Score.get_score()==71 and play==4:
                Powerup.play()
                play+=1
            pygame.time.delay(30)
        elif Score.get_score()>=91:
            if Score.get_score()==91 and play==5:
                Powerup.play()
                play+=1
            pygame.time.delay(0)
                        
        # Refresh screen
        allSprites.clear(screen, background)
        # The next line calls the update() method for any sprites in the allSprites group.
        allSprites.update()
        allSprites.draw(screen)
     
        pygame.display.flip()
    # Close the game window
    pygame.quit()        
 
# Call the main function
main()