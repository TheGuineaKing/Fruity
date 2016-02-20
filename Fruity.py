#Fruity Concept 1
#Initiated: 08-09-15
#Completed: 08-16-15

import pygame                                                            #pygame module
import time
import random

pygame.init()                                                            #initiate pygame

display_width = 800
display_height = 600

black = (0,0,0)                                                          #Red Green Blue(rgb) to define colors
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)

bucket_width = 120
bucket_height = 117

gameDisplay = pygame.display.set_mode((display_width,display_height))    #display box dimensions  
pygame.display.set_caption('Fruity')                                     #display box title
clock = pygame.time.Clock()                                              #clock for fps

collect_sound = pygame.mixer.Sound('sounds\\Collect.wav')                       
medal_sound = pygame.mixer.Sound('sounds\\Medal.wav')
menuscreen = pygame.image.load('misc\\menu.png')
iconImg = pygame.image.load('misc\\icon.png')
backgroundImg = pygame.image.load('misc\\background.png')
pygame.display.set_icon(iconImg)
bronzeImg = pygame.image.load('medals\\bronze.png')
silverImg = pygame.image.load('medals\\silver.png')
goldImg = pygame.image.load('medals\\gold.png')
                            
bucketImg = pygame.image.load('misc\\bucket.png')
strawberryImg = pygame.image.load('fruits\\strawberry.png')
appleImg = pygame.image.load('fruits\\apple.png')
cherryImg = pygame.image.load('fruits\\cherry.png')
watermelonImg = pygame.image.load('fruits\\watermelon.png')
cakeImg = pygame.image.load('unhealthy_foods\\cake.png')
donutImg = pygame.image.load('unhealthy_foods\\donut.png')
sodaImg = pygame.image.load('unhealthy_foods\\soda.png')
chickenImg = pygame.image.load('unhealthy_foods\\chicken.png')
candyImg = pygame.image.load('unhealthy_foods\\candy.png')

pause = False

def fruits_taken(count):
    font = pygame.font.SysFont('comicsansms', 25)
    text = font.render("Score: " + str(count), True, black)
    gameDisplay.blit(text,(0,0))
                                                            
def strawberry(straw_x,straw_y):                                                                      
    gameDisplay.blit(strawberryImg,(straw_x,straw_y))                                                
                                                          
def apple(apple_x,apple_y):                                
    gameDisplay.blit(appleImg,(apple_x,apple_y))          
                                                          
def cherry(cherry_x,cherry_y):                            
    gameDisplay.blit(cherryImg,(cherry_x,cherry_y))       
                                                          
def watermelon(water_x,water_y):                          
    gameDisplay.blit(watermelonImg,(water_x,water_y))        
 
def cake(cake_x,cake_y):                                                                     
    gameDisplay.blit(cakeImg,(cake_x,cake_y))                                             
                                                           
def donut(donut_x,donut_y):                              
    gameDisplay.blit(donutImg,(donut_x,donut_y))         
                                                          
def soda(soda_x,soda_y):                                  
    gameDisplay.blit(sodaImg,(soda_x,soda_y))            
                                                         
def chicken(chick_x,chick_y):                             
    gameDisplay.blit(chickenImg,(chick_x,chick_y))          
                                                          
def candy(candy_x,candy_y):                               
    gameDisplay.blit(candyImg,(candy_x,candy_y))                                                                  
         
def bucket(x,y):
    gameDisplay.blit(bucketImg,(x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
    
def message_display(text):
    largeText = pygame.font.SysFont('comicsansms',50)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()
    time.sleep(2)
    game_loop()
    
def junk():
    pygame.mixer.music.stop()
    message_display('You Picked Up Junk Food!')
    main()

def button(message, x, y, w, h, ic, ac, action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x,y,w,h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x,y,w,h))
            
    smallText = pygame.font.SysFont('comicsansms',20)
    textSurf, textRect = text_objects(message,smallText)
    textRect.center = ((x + (w/2)), (y + (h/2)))
    gameDisplay.blit(textSurf, textRect)
    
def quitgame():
    pygame.quit()
    quit()

def unpause():
    global pause
    pause = False
    pygame.mixer.music.stop()
    pygame.mixer.music.load('sounds\\Ambience.wav')
    pygame.mixer.music.play(-1)
    
    
def paused():
    pygame.mixer.music.stop()
    pygame.mixer.music.load('sounds\\MenuSong.wav')
    pygame.mixer.music.play(-1)
    
    while pause:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()
               
        gameDisplay.blit(menuscreen,(0,0))
        largeText = pygame.font.SysFont('comicsansms',100)
        TextSurf, TextRect = text_objects('Paused', largeText)
        TextRect.center = ((display_width/2),(display_height/2 + 50))
        gameDisplay.blit(TextSurf, TextRect)
        button('CONTINUE',150,450,120,50, green, bright_green,unpause)
        button('QUIT',550,450,120,50, red, bright_red,quitgame)
        
        pygame.display.update()
        clock.tick(15)
        
def game_intro():
    
    intro = True
    
    pygame.mixer.music.load('sounds\\MenuSong.wav')
    pygame.mixer.music.play(-1)
    logo = pygame.image.load("misc\\ChinchillaCreations.png").convert()
    clock = pygame.time.Clock()

    for i in range(255):
        gameDisplay.fill(black)
        logo.set_alpha(i)
        gameDisplay.blit(logo, (0,0))
        pygame.display.flip()
        clock.tick(60)
        
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()
            
        gameDisplay.blit(menuscreen,(0,0))
        largeText = pygame.font.SysFont('comicsansms',100)
        TextSurf, TextRect = text_objects('Fruity', largeText)
        TextRect.center = ((display_width/2),(display_height/2 + 50))
        gameDisplay.blit(TextSurf, TextRect)

        button('START',150,450,100,50, green, bright_green,game_loop)
        button('QUIT',550,450,100,50, red, bright_red,quitgame)
        
        pygame.display.update()
        clock.tick(15)
        
def game_loop():
    global pause

    pygame.mixer.music.stop()
    pygame.mixer.music.load('sounds\\Ambience.wav')
    pygame.mixer.music.play(-1)
    
    score = 0
    
    x = (display_width*0.45) # x = 360
    y = (display_height*0.8) # y = 480 

    x_change = 0
 
    straw_width = 50
    straw_height = 55
    straw_x = random.randrange(0,display_width - straw_width)
    straw_y = -600
    straw_speed = 2

    apple_width = 50
    apple_height = 49
    apple_x = random.randrange(0,display_width - apple_width)
    apple_y = -600
    apple_speed = 2.75
    
    cherry_width = 50
    cherry_height = 52
    cherry_x = random.randrange(0,display_width - cherry_width)
    cherry_y = -600
    cherry_speed = 3.25
    
    water_width = 50
    water_height = 51
    water_x = random.randrange(0,display_width - water_width)
    water_y = -600
    water_speed = 3.75
 
    cake_width = 50
    cake_height = 67
    cake_x = random.randrange(0,display_width - cake_width)
    cake_y = -600
    cake_speed = 2.5
    
    donut_width = 50
    donut_height = 48
    donut_x = random.randrange(0,display_width - donut_width)
    donut_y = -600
    donut_speed = 3

    soda_width = 50
    soda_height = 65
    soda_x = random.randrange(0,display_width - soda_width)
    soda_y = -600
    soda_speed = 3.5

    chick_width = 50
    chick_height = 55
    chick_x = random.randrange(0,display_width - chick_width)
    chick_y = -600
    chick_speed = 4
    
    candy_width = 50
    candy_height = 57  
    candy_x = random.randrange(0,display_width - candy_width)
    candy_y = -600
    candy_speed = 4.5
    
    gameExit = False

    while not gameExit:

        for event in pygame.event.get():                                     #event-handling loop
            if event.type == pygame.QUIT:
                quitgame()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5   
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_p:
                    pause = True
                    paused()
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                                    
        x = x + x_change
 
        gameDisplay.blit(backgroundImg,(0,0))
 
        strawberry(straw_x,straw_y)
        apple(apple_x,apple_y) 
        cherry(cherry_x,cherry_y)
        watermelon(water_x,water_y)
        cake(cake_x,cake_y)
        donut(donut_x,donut_y)
        soda(soda_x,soda_y)
        chicken(chick_x,chick_y)
        candy(candy_x,candy_y)
 
        straw_y = straw_y + straw_speed
        apple_y = apple_y + apple_speed
        cherry_y = cherry_y + cherry_speed
        water_y = water_y + water_speed
        cake_y = cake_y + cake_speed
        donut_y = donut_y + donut_speed
        soda_y = soda_y + soda_speed
        chick_y = chick_y + chick_speed
        candy_y = candy_y + candy_speed
        
        bucket(x,y)
        fruits_taken(score)

        if x  > display_width - bucket_width or x < 0:
            x_change = 0
 
        if straw_y > display_height:
            straw_y = 0 - straw_height
            straw_x = random.randrange(0, display_width - straw_width)
            
        if straw_y > 495:
            straw_y = 1000

        if y < straw_y + straw_height - 40: 
            if x < straw_x and x + bucket_width > straw_x + straw_width:
                score = score + 1
                pygame.mixer.Sound.play(collect_sound)
                
        if apple_y > display_height:
            apple_y = 0 - apple_height
            apple_x = random.randrange(0, display_width - apple_width)

        if apple_y > 495:
            apple_y = 1000
            
        if y < apple_y + apple_height - 40: 
            if x < apple_x and x + bucket_width > apple_x + apple_width:
                score = score + 1
                pygame.mixer.Sound.play(collect_sound)
                
        if cherry_y > display_height:
            cherry_y = 0 - cherry_height
            cherry_x = random.randrange(0, display_width - cherry_width)

        if cherry_y > 495:
            cherry_y = 1000
            
        if y < cherry_y + cherry_height - 40: 
            if x < cherry_x and x + bucket_width > cherry_x + cherry_width:
                score = score + 1
                pygame.mixer.Sound.play(collect_sound)

        if water_y > display_height:
            water_y = 0 - water_height
            water_x = random.randrange(0, display_width - water_width)

        if water_y > 495:
            water_y = 1000
            
        if y < water_y + water_height - 40: 
            if x < water_x and x + bucket_width > water_x + water_width:
                score = score + 1
                pygame.mixer.Sound.play(collect_sound)
                
        if cake_y > display_height:
            cake_y = 0 - cake_height
            cake_x = random.randrange(0, display_width - cake_width)

        if cake_y > 495:
            cake_y = 1000
        
        if y < cake_y + cake_height - 40:
            if x < cake_x and x + bucket_width > cake_x + cake_width:
                junk()
                
        if donut_y > display_height:
            donut_y = 0 - donut_height
            donut_x = random.randrange(0, display_width - donut_width)

        if donut_y > 495:
            donut_y = 1000
        
        if y < donut_y + donut_height - 40: 
            if x < donut_x and x + bucket_width > donut_x + donut_width:
                junk()

        if soda_y > display_height:
            soda_y = 0 - soda_height
            soda_x = random.randrange(0, display_width - soda_width)
            
        if soda_y > 495:
            soda_y = 1000
            
        if y < soda_y + soda_height - 40: 
            if x < soda_x and x + bucket_width > soda_x + soda_width:
                junk()

        if chick_y > display_height:
            chick_y = 0 - chick_height
            chick_x = random.randrange(0, display_width - chick_width)
            
        if chick_y > 495:
            chick_y = 1000
            
        if y < chick_y + chick_height - 40: 
            if x < chick_x and x + bucket_width > chick_x + chick_width:
                junk()

        if candy_y > display_height:
            candy_y = 0 - candy_height
            candy_x = random.randrange(0, display_width - candy_width)
            
        if candy_y > 495:
            candy_y = 1000
            
        if y < candy_y + candy_height - 40: 
            if x < candy_x and x + bucket_width > candy_x + candy_width:
                junk()

        if score >= 100:
            gameDisplay.blit(bronzeImg,(0,30))
            
        if score == 100:
            pygame.mixer.Sound.play(medal_sound)
            
        if score >= 500:
            gameDisplay.blit(silverImg,(30,30))
            
        if score == 500:
            pygame.mixer.Sound.play(medal_sound)
            
        if score >= 1000:
            gameDisplay.blit(goldImg,(60,30))
            
        if score == 1000:
            pygame.mixer.Sound.play(medal_sound)
            
        pygame.display.update()
        clock.tick(60)                                   #fps: increase to speed up game
        
game_intro()
game_loop()
quitgame()
