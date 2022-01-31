'''Date:May 28, 2019
   Author:Andrew Lin
   Description: A Snake sprite group that gets called in the snake game.
'''

import pygame
import random
 
class Ball(pygame.sprite.Sprite):
    '''A simple Sprite subclass to represent static ball sprites.'''
    def __init__(self, screen):
        '''This initializer takes a screen surface, and creates the ball sprites'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        # Set the image and rect attributes for the ball
        self.image = pygame.image.load("Ball3.png").convert()
        self.rect = self.image.get_rect()
        self.screen=screen
        self.image.set_colorkey((255,255,255))
    
    def setPosition(self,x,y):
        '''Sets the position of each ball'''
        self.rect.centerx = x
        self.rect.centery = y
        

        
class Body(pygame.sprite.Sprite):
    '''A simple Sprite Subclass to represent a the snakes body Sprite'''
    def __init__(self,screen):
        '''This initializer takes a screen surface, and creates the body of the snake.'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
 
        # Set the image and rect attributes for the bricks
        self.image = pygame.Surface((20,20))
        self.image.fill((162, 82, 3)) 
        self.image=self.image.convert()
        self.rect = self.image.get_rect()      
            
    
    def set_position(self,x,y):
        '''This method is called and sets the position of the body'''
        self.rect.centerx = x
        self.rect.centery = y

    def get_centerx(self):
        '''The method returns a integer and the exact x value of the area of 
        the snake body'''        
        return self.rect.centerx
    
    def get_centery(self):
        '''The method returns a integer and the exact y value of the area of 
        the snake body'''        
        return self.rect.centery
    

        
class Head(pygame.sprite.Sprite):
    '''A simple Sprite Subclass to represent a the snakes head '''
    def __init__(self, screen):
        '''This initializer takes a screen surface, and creates a head sprite'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
 
        # Set the image and rect attributes for the bricks
        self.image = pygame.Surface((20,20))
        self.image.fill((0, 0, 255)) 
        self.image=self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.centerx = screen.get_width()/2 
        self.rect.centery = screen.get_height()/2
        self.dx=0
        self.dy=0
        self.screen=screen
        
    def go_left(self):
        '''This method changes the dx to allow the snake to move left'''
        self.dx = -20
        self.dy = 0    
        
    def go_right(self):
        '''This method changes the dyx to allow the snake to move right'''
        self.dx = 20
        self.dy = 0  
        
    def go_up(self):
        '''This method changes the dy to allow the snake to move up'''
        self.dx = 0
        self.dy = -20
        
    def go_down(self):
        '''This method changes the dy to allow the snake to move down'''
        self.dx = 0
        self.dy = 20
    
    
    def reset(self):
        '''This method resets the snake position to the middle after it dies'''
        self.rect.centerx = self.screen.get_width()/2 
        self.rect.centery = self.screen.get_height()/2
        
        
    def get_x(self):
        '''The method returns a integer and the exact x value of the area of 
        the snake head'''
        return self.rect.centerx
    
    def get_y(self):
        '''The method returns a integer and the exact y value of the area of 
        the snake head'''
        return self.rect.centery

    
    def update(self):
        '''This method will continusely update the snake to allow it to move'''
        self.rect.centerx += self.dx
        self.rect.centery += self.dy        
        


class EndZone(pygame.sprite.Sprite):
    '''This class defines the sprite for our end zones'''
    def __init__(self, screen, number):
        '''This initializer takes a screen surface, and a number to create the border of the game.'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((screen.get_width(),10))
        self.image = self.image.convert()
        self.image.fill((0, 0, 0))           

        if number==0:
            # Set the rect attributes for the endzone
            self.rect = self.image.get_rect()
            self.rect.left = 0
            self.rect.bottom = screen.get_height()            
        elif number==1:
            # Set the rect attributes for the endzone
            self.rect = self.image.get_rect()
            self.rect.left = number
            self.rect.bottom = 50  
            
        elif number==2:
            self.image = pygame.Surface((10,screen.get_height())) 
            # Set the rect attributes for the endzone
            self.rect = self.image.get_rect()
            self.rect.right = 640
            self.rect.bottom = screen.get_height()               
            
        elif number==3:        
            self.image = pygame.Surface((10,screen.get_height()))
            # Set the rect attributes for the endzone
            self.rect = self.image.get_rect()
            self.rect.right = 10
            self.rect.bottom = screen.get_height()               

       
class ScoreKeeper(pygame.sprite.Sprite):
    '''This class defines a label sprite to display the score.'''
    def __init__(self):
        '''This initializer loads the system font "Arial", and
        sets the starting score to 0:0'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        # Load our custom font, and initialize the starting score.
        self.font=pygame.font.Font("walt.ttf", 30)
        self.player1Score = 0
        self.highScore=0
    
    def reset(self):
        '''This method will reset the score and change the high score'''
        if self.player1Score > self.highScore:
            self.highScore=self.player1Score
        self.player1Score = 0
    
    def get_score(self):
        '''Returns the score value'''
        return self.player1Score
      
    def player(self):
        '''This method adds one to the score for player 1'''
        self.player1Score += 1
 
    def update(self):
        '''This method will be called automatically to display 
        the current score at the top of the game window.'''
        message = "Score: " + str(self.player1Score)+"     High Score: " + str(self.highScore)
        self.image = self.font.render(message, 1, (0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (300, 20)
        
