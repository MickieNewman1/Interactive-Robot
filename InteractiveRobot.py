# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 18:42:20 2021

@author: mwnew
"""
#======
# Interactive Robot
#Mickie Newman
#20/02/19
#
import pygame
from random import *

## Pseudocode
# make robot )
# make robot move to the left
# make robot move to the right
# make robot move up 
# make robot move down
# have the robots buttons ocilate size when tab is pressed
# have the robots lights flash colors when space is pressed
# have the robot change colors when backspace is pressed

## got robot from robot script in my toolbox looked at the 2/11 and 2/13 script for help 

#set up colors
BLACK = (0,0,0)
RED = (255,0,0)
PINK = (170,0,50)
GREEN = (0,255,0)
BLUE = (0,0,255)
LT_BLUE = (0, 100, 255)
WHITE = (255,255,255)
GRAY = (127,127,127)
DK_GRAY = (100,100,100)

#create screen and game variables
size = 500
screen = pygame.display.set_mode((size,size)) #create 500 x500 pixel screen

run = True
x = size/2 #center position for all robot parts
y = size/2


scale = 1 #variable to adjust when keys are pressed to change size of robot
vel = 1
eye_r = 2
buttonSize = 3

#Robo features
buttonColor = [BLUE, RED, GREEN]
color = BLACK
colorL = BLACK
colorR = BLACK

bodyColor = [DK_GRAY, PINK, GRAY, BLACK]
colorRB = GRAY



#Game loop
while run:
    # create exit-on click detection:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            
    #Drawing goes from bottom to top. We'll make our screen white first, then
    #add the robo-parts.    
    screen.fill(WHITE)
    
    
    keys = pygame.key.get_pressed()       
  # makes the robot move up down right and left 
    if keys[pygame.K_LEFT]:
        x -= vel  
        
    if keys[pygame.K_RIGHT]:
        x += vel
    
    
    if keys[pygame.K_UP]:
        y -= vel
    
    
    if keys[pygame.K_DOWN]:
        y += vel
        
# changes the button size
    if keys[pygame.K_TAB]:
        
        if buttonSize <=5: 
           buttonSize += 5
           
        elif buttonSize > 5:
            buttonSize -= 5
 # makes the buttons flash colors  
    if keys[pygame.K_SPACE]:
        color = choice(buttonColor)
        colorL = choice(buttonColor)
        colorR = choice(buttonColor)
# makes the robot change colors
    if keys[pygame.K_BACKSPACE]:
        colorRB = choice(bodyColor)

        
        
        
    #Pygame draw docs: https://www.pygame.org/docs/ref/draw.html#pygame.draw.circle
    Head = pygame.draw.rect(screen,colorRB,(x-25,y-90,50,50)) 
    Body = pygame.draw.polygon(screen, colorRB, [(x+35, y-35),(x+45,y+35), (x-45,y+35),(x-35, y-35)])
    L_eye = pygame.draw.circle(screen, GREEN, (int(x-10), int(y-70)),eye_r)
    R_eye = pygame.draw.circle(screen, GREEN, (int(x+10), int(y-70)),eye_r)
    panelLights1 = pygame.draw.circle(screen, colorR, (int(x+20), int(y-5)),buttonSize)
    panelLights2 = pygame.draw.circle(screen, color, (int(x), int(y-5)),buttonSize)
    panelLights3 = pygame.draw.circle(screen, colorL, (int(x-20), int(y-5)),buttonSize)

    L_wheel = pygame.draw.circle(screen, BLACK, (int(x-40), int(y+63)),20)
    R_wheel = pygame.draw.circle(screen, BLACK, (int(x+40), int(y+63)),20)
    L_hub = pygame.draw.circle(screen, DK_GRAY, (int(x-40), int(y+63)),10)
    R_hub = pygame.draw.circle(screen, DK_GRAY, (int(x+40), int(y+63)),10)
    Track = pygame.draw.ellipse(screen, DK_GRAY, (int(x-65), int(y+33),130,60),2)

    pygame.display.update() #update all changes to screen
    