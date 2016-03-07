import pygame, sys, pygame.mixer, pygame as pg
import pygbutton
from pygame.locals import *

#initalise pygame
pygame.init()

#Globally Initalise the screen 
screen = pygame.display.set_mode((800,600),0,32)
backgroundcolour = (255, 255, 255)
pygame.display.set_caption("MASTERCHEF VRBH")

#initialise colours
black = (0, 0, 0)
white = (255, 255, 255)

#Import Images
background = pygame.image.load("backgroundimage.jpg") 
firstimage = pygame.image.load("firstimage.jpg")
firstimage = pygame.transform.scale(firstimage, (300,300))
secondimage = pygame.image.load("secondimage.jpg")
secondimage = pygame.transform.scale(secondimage, (300,300))


def mainMenu():
   #initialise the cursor
    pygame.mouse.set_visible(True)

    #Generate font objects as well as initialise and display text
    font = pg.font.SysFont("Calibri", 100, bold = True)
    newfont = pg.font.SysFont("Calibri", 45, bold = True) 
    header = font.render("MASTERCHEF VRBH", 1, black)
    text = font.render("BARGAIN HUNT", 1, black)
    groupnames = newfont.render("BY MAX, MICHAEL, NKOSILATHI, NAMAR AND ISAAC", 1, black)

    #Generate buttons
    play = pygbutton.PygButton((350, 300, 100, 30), "PLAY") 
    exitgame = pygbutton.PygButton((350, 370, 100, 30), "EXIT")
    
    #Responds to events such as pressing the escape key 
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE or event.key == K_q:
                    sys.exit()
            if 'click' in exitgame.handleEvent(event):
                pygame.quit()
                sys.exit()
            if 'click' in play.handleEvent(event):
                townMap()
                    
        #display stuff on the screen and update it
        screen.blit(background, (0, 0))
        pygame.draw.rect(screen, white, (60, 50, 690, 55)) #Generate a rectangle and display it on the screen
        pygame.draw.rect(screen, white, (130, 120, 530, 55))
        pygame.draw.rect(screen, white, (15, 530, 775, 35))
        screen.blit(header, (60, 40))
        screen.blit(text, (130, 110))
        screen.blit(firstimage, (5,200))
        screen.blit(secondimage, (495,200))
        screen.blit(groupnames, (15, 530))
        play.draw(screen)
        exitgame.draw(screen)
        pygame.display.update()

def townMap():
    TREES = 0
    ROADS = 1
    GRASS = 2
    HOUSE = 3
    ENDNODE = 5
    STARTNODE = 5
    for x in range(1, 10):
        globals()['store%s' % x] = 4
    tiles = {
                TREES : pygame.image.load('trees.png'),
                ROADS : pygame.image.load('roads.png'),
                GRASS : pygame.image.load('grass.png'),
                HOUSE : pygame.image.load('house.png'),
                STARTNODE : pygame.image.load('startnode.png'),
                ENDNODE : pygame.image.load('endnode.png'),
                store1 : pygame.image.load('shops.png'),
                store2 : pygame.image.load('shops.png'),
                store3 : pygame.image.load('shops.png'),
                store4 : pygame.image.load('shops.png'),
                store5 : pygame.image.load('shops.png'),
                store6 : pygame.image.load('shops.png'),
                store7 : pygame.image.load('shops.png'),
                store8 : pygame.image.load('shops.png'),
                store9 : pygame.image.load('shops.png') 
            }

    tileMap = [
                [ TREES, TREES, TREES, TREES, TREES, TREES, TREES, TREES, TREES, TREES, TREES, TREES, TREES, TREES, TREES, TREES, TREES, TREES, TREES, TREES ],
                [ TREES, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, TREES ],
                [ TREES, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, TREES, TREES, ENDNODE, GRASS, GRASS, GRASS, GRASS, TREES ],
                [ TREES, GRASS, GRASS, store7, GRASS, HOUSE, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, TREES, TREES, ROADS, ROADS, ROADS, store1, GRASS, TREES ],
                [ TREES, GRASS, TREES, ROADS, ROADS, ROADS, ROADS, ROADS, ROADS, store2, GRASS, GRASS, TREES, TREES, ROADS, GRASS, TREES, TREES, GRASS, TREES ],
                [ TREES, GRASS, TREES, ROADS, TREES, GRASS, GRASS, TREES, ROADS, TREES, TREES, store8, TREES, TREES, ROADS, HOUSE, TREES, TREES, GRASS, TREES ],
                [ TREES, GRASS, TREES, ROADS, TREES, GRASS, GRASS, TREES, ROADS, TREES, TREES, ROADS, ROADS, ROADS, ROADS, GRASS, TREES, TREES, GRASS, TREES ],
                [ TREES, GRASS, HOUSE, ROADS, TREES, GRASS, GRASS, HOUSE, ROADS, TREES, TREES, HOUSE, GRASS, GRASS, ROADS, GRASS, store3, GRASS, GRASS, TREES ],
                [ TREES, GRASS, TREES, ROADS, TREES, GRASS, GRASS, TREES, ROADS, GRASS, GRASS, GRASS, GRASS, GRASS, ROADS, GRASS, ROADS, GRASS, GRASS, TREES ],
                [ TREES, GRASS, TREES, ROADS, HOUSE, GRASS, GRASS, TREES, ROADS, GRASS, GRASS, GRASS, GRASS, GRASS, ROADS, GRASS, ROADS, GRASS, GRASS, TREES ],
                [ TREES, GRASS, TREES, ROADS, TREES, TREES, store9, ROADS, ROADS, ROADS, ROADS, ROADS, ROADS, ROADS, ROADS, ROADS, ROADS, HOUSE, GRASS, TREES ],
                [ TREES, GRASS, HOUSE, ROADS, TREES, TREES, TREES, ROADS, GRASS, HOUSE, GRASS, ROADS, GRASS, HOUSE, ROADS, GRASS, GRASS, GRASS, GRASS, TREES ],
                [ TREES, GRASS, TREES, ROADS, TREES, TREES, TREES, ROADS, TREES, TREES, TREES, ROADS, GRASS, TREES, ROADS, GRASS, GRASS, GRASS, GRASS, TREES ],
                [ TREES, GRASS, TREES, ROADS, TREES, TREES, TREES, ROADS, TREES, TREES, TREES, ROADS, GRASS, TREES, ROADS, HOUSE, GRASS, GRASS, GRASS, TREES ],
                [ TREES, GRASS, TREES, ROADS, TREES, TREES, TREES, ROADS, TREES, TREES, TREES, ROADS, GRASS, TREES, ROADS, TREES, TREES, GRASS, GRASS, TREES ],
                [ TREES, GRASS, store4, ROADS, ROADS, ROADS, ROADS, ROADS, TREES, TREES, TREES, store5, GRASS, HOUSE, ROADS, TREES, TREES, GRASS, GRASS, TREES ],
                [ TREES, GRASS, GRASS, STARTNODE, HOUSE, GRASS, HOUSE, GRASS, TREES, TREES, TREES, GRASS, GRASS, GRASS, ROADS, ROADS, ROADS, store6, GRASS, TREES ],
                [ TREES, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, TREES ],
                [ TREES, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, TREES ],
                [ TREES, TREES, TREES, TREES, TREES, TREES, TREES, TREES, TREES, TREES, TREES, TREES, TREES, TREES, TREES, TREES, TREES, TREES, TREES, TREES ]
              ]

    tileSize = 30
    mapWidth = 20
    mapHeight = 20

    pygame.init()
    displayMap = pygame.display.set_mode((mapWidth*tileSize, mapHeight*tileSize))

    while True:
        for row in range(mapHeight):
            for column in range(mapWidth):
                displayMap.blit(tiles[tileMap[row][column]], (column*tileSize,row*tileSize))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.display.update()

mainMenu()
