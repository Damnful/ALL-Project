import pygame, sys, pygame.mixer, pygame as pg
import pygbutton
import random
import csv
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
    font = pg.font.SysFont("Calibri", 80, bold = True)
    newfont = pg.font.SysFont("Calibri", 35, bold = True) 
    header = font.render("MASTERCHEF VRBH", 1, black)
    text = font.render("BARGAIN HUNT", 1, black)
    groupnames = newfont.render("BY MAX, MICHAEL, NKOSILATHI, NAMAR AND ISAAC", 1, black)

    #Generate buttons
    play = pygbutton.PygButton((350, 300, 100, 30), "Play") 
    exitgame = pygbutton.PygButton((350, 370, 100, 30), "Exit")
    
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
                optionsScreen()
                    
        #display stuff on the screen and update it
        screen.blit(background, (0, 0))
        screen.blit(header, (60, 40))
        screen.blit(text, (130, 110))
        screen.blit(firstimage, (5,200))
        screen.blit(secondimage, (495,200))
        screen.blit(groupnames, (15, 530))
        play.draw(screen)
        exitgame.draw(screen)
        pygame.display.update()
        
def optionsScreen():
    pygame.display.set_caption("MASTERCHEF VRBH - OPTIONS")
    pygame.mouse.set_visible(True)
    pygame.font.init()

    font = pg.font.SysFont("Calibri", 35, bold = True)
    newfont = pg.font.SysFont("Calibri", 14, bold = True)
    header = font.render("Game Options", 1, black)
    informationLabel1 = newfont.render("Play our Masterchef Virtual Robot Bargain Hunt today! All you have to do",1,black)
    informationLabel2 = newfont.render("is choose a time limit and a wallet amount, then choose your recipe that",1,black)
    informationLabel3 = newfont.render("you would like to gather the ingredients to in record time!",1, black)

    recipe1 = pygbutton.PygButton((40, 200, 160, 30), "Bacon Pasta Bake")
    recipe2 = pygbutton.PygButton((320, 200, 160, 30), "Chicken Korma")
    recipe3 = pygbutton.PygButton((600, 200, 160, 30), "Chilli Con Carne")
    recipe4 = pygbutton.PygButton((40 , 300, 160, 30), "Victoria Sandwich")
    recipe5 = pygbutton.PygButton((320, 300, 160, 30), "Lasagne")
    recipe6 = pygbutton.PygButton((600, 300, 160, 30), "Lemon Drizzle Cake")
    recipe7 = pygbutton.PygButton((40, 400, 160, 30), "Pepperoni Pizza")
    recipe8 = pygbutton.PygButton((320, 400, 160, 30), "Roast Chicken")
    recipe9 = pygbutton.PygButton((600, 400, 160, 30), "Shepherd's Pie")
    randomRecipe = pygbutton.PygButton((320, 500, 160, 30), "Random Recipe!")
    back = pygbutton.PygButton((0, 570, 70, 30), "Back")
    exitgame = pygbutton.PygButton((730, 570, 70, 30), "Exit")

    while True:
        for event in pygame.event.get():
            
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE or event.key == K_q:
                    sys.exit()
            if 'click' in recipe1.handleEvent(event):
                recipe = 'cheesybaconpastabake.csv'
                initTownMap(recipe)
                
            if 'click' in recipe2.handleEvent(event):
                recipe = 'chickenkorma.csv'
                initTownMap(recipe)
                
            if 'click' in recipe3.handleEvent(event):
                recipe = 'chilliconcarne.csv'
                initTownMap(recipe)
                
            if 'click' in recipe4.handleEvent(event):
                recipe = 'classicvictoriasandwich.csv'
                initTownMap(recipe)
                
            if 'click' in recipe5.handleEvent(event):
                recipe = 'lasagne.csv'
                initTownMap(recipe)
                
            if 'click' in recipe6.handleEvent(event):
                recipe = 'lemondrizzlecake.csv'
                initTownMap(recipe)
                
            if 'click' in recipe7.handleEvent(event):
                recipe = 'pepperonipizza.csv'
                initTownMap(recipe)
                
            if 'click' in recipe8.handleEvent(event):
                recipe = 'roastedchickenroastpotatoes.csv'
                initTownMap(recipe)
                
            if 'click' in recipe9.handleEvent(event):
                recipe = 'shepherdspie.csv'
                initTownMap(recipe)
                
            if 'click' in randomRecipe.handleEvent(event):
                recipelist = [
                                'cheesybaconpastabake.csv', 'chickenkorma.csv', 'chilliconcarne.csv', 'classicvictoriasandwich.csv', 'lasagne.csv',
                                'lemondrizzlecake.csv', 'lemondrizzlecake.csv', 'pepperonipizza.csv', 'roastedchickenroastpotatoes.csv', 'shepherdspie.csv'
                             ]
                recipe = str(random.choice(recipelist))
                initTownMap(recipe)
                
            if 'click' in back.handleEvent(event):
                mainMenu()

            if 'click' in exitgame.handleEvent(event):
                pygame.quit()
                sys.exit()
                    
        #display stuff on the screen and update it
        screen.blit(background, (0, 0))
        pygame.draw.rect(screen, white, (38, 28, 215, 50))
        pygame.draw.rect(screen, white, (38, 68, 440, 59))
        screen.blit(header, (40, 30))
        screen.blit(informationLabel1, (40, 70))
        screen.blit(informationLabel2, (40, 90))
        screen.blit(informationLabel3, (40, 110))
        recipe1.draw(screen)
        recipe2.draw(screen)
        recipe3.draw(screen)
        recipe4.draw(screen)
        recipe5.draw(screen)
        recipe6.draw(screen)
        recipe7.draw(screen)
        recipe8.draw(screen)
        recipe9.draw(screen)
        randomRecipe.draw(screen)
        back.draw(screen)
        exitgame.draw(screen)
        
        pygame.display.update()

def initTownMap(recipe):
    for i in range(1,10):
        storeNumber = 'store%d.csv' % i
        with open('items.csv','r') as csvinput:
            with open(storeNumber, 'w') as csvoutput: # this section of code creates random prices for all items in the item database and creates a new file with these values for each store
                writer = csv.writer(csvoutput)
                reader = csv.reader(csvinput)

                all = []
                row = next(reader)
                row.append('price')
                all.append(row)

                for row in reader:
                    row.append((random.randint(50,500)) / 100)
                    all.append(row)

                writer.writerows(all)

    recipeIngredients = {}

    with open(recipe, 'r') as csvinput:  # this section of code pulls data from the recipe documents and converts to a dictionary
        reader = csv.reader(csvinput)
        next(reader)
        
        for row in reader:
            recipeIngredients['%s' % row[0]] = {'weight': row[1], 'quantity': row[2]}

    ingredientsList = []

    for key in recipeIngredients:
        ingredientsList.append(key)  # makes a list of JUST the ingredients needed for each recipe

    shopPrices = {}
    whereToGetItem = {} # declaring dictionaries and a list
    shopsToVisit = []

    for ingredients in ingredientsList:
        for i in range(1,10):
            storeNumber = 'store%d.csv' % i
            with open(storeNumber, 'r') as csvinput:
                reader = csv.reader(csvinput)
                next(reader)
                                                # this section of code finds where each ingredient is cheapest and store these values in a dictionary
                for row in reader:
                    if ingredients in row:
                        pricePerQuantity = float(row[3]) / float(row[2])
                        shopPrices.update({'store%d' % i: pricePerQuantity})
                        
        cheapestStore = min(shopPrices, key=shopPrices.get)
        whereToGetItem.update({ingredients: cheapestStore})
        
        if cheapestStore not in shopsToVisit:
            shopsToVisit.append(cheapestStore) # this list tells the program which stores it needs to visit, hence ignoring unneeded stores

    townMap(shopsToVisit, whereToGetItem, recipe)


def townMap(recipe, shopsToVisit, whereToGetItem):

    pygame.display.set_caption("MASTERCHEF VRBH - SIMULATION")
    
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
    displayMap = pygame.display.set_mode((800, 600))
    back = pygbutton.PygButton((0, 570, 70, 30), "Back")
    exitgame = pygbutton.PygButton((530, 570, 70, 30), "Exit")
    
    while True:
        for row in range(mapHeight):
            for column in range(mapWidth):
                displayMap.blit(tiles[tileMap[row][column]], (column*tileSize,row*tileSize))
                
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE or event.key == K_q:
                    sys.exit()
                    
            if 'click' in back.handleEvent(event):
                optionsScreen()

            if 'click' in exitgame.handleEvent(event):
                pygame.quit()
                sys.exit()
                
        back.draw(screen)
        exitgame.draw(screen)
        pygame.display.update()

mainMenu()
