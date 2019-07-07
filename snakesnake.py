import pygame , sys , random , time
pygame.init()

#Display
size = 600,600
win = pygame.display.set_mode(size)
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

#color
black = [0,0,0]
red = [255,0,0]
green = [0,255,0]
white = [255,255,255]

#Snake
snake_X = 300
snake_Y = 300
XSpeed  = 1
YSpeed = 0
scale = 10

# defining my snake
def snake(scale,snake_list,snakelen):
    for i in snake_list:
        pygame.draw.rect(win,white,[i[0],i[1],scale,scale])




#Food
FoodX = round(random.randint(0,600-scale)/10)*10
FoodY = round(random.randint(0,600-scale)/10)*10

snake_list = []
snakelen  = 1

#message
font= pygame.font.SysFont(None,30)
def mesg(msg,mcolor):
    screen_text = font.render(msg,True,mcolor)
    win.blit(screen_text,[300,300])

# Game main Loop
gameExit = False
while not gameExit:
    snake_X += XSpeed* scale
    snake_Y += YSpeed* scale

    # event
    for event in pygame.event.get():
        #print(events)
        if event.type == pygame.QUIT:
            pygame.QUIT()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                XSpeed = 0
                YSpeed = -1 
            elif event.key == pygame.K_s:
                YSpeed = 1
                XSpeed = 0
            elif event.key == pygame.K_a:
                XSpeed = -1
                YSpeed = 0
            elif event.key == pygame.K_d:
                XSpeed = 1
                YSpeed = 0            

    # Game Ending    
    if snake_X <= 0 or snake_X >= 600:
        win.fill(red)
        mesg(" You Lose", white)
        pygame.display.update()
        print("You lose")
        time.sleep(1)
        gameExit = True
    elif snake_Y <= 0 or snake_Y >= 600:
        win.fill(red)
        mesg(" You Lose", white)
        pygame.display.update()
        print("you lose")
        time.sleep(1)
        gameExit = True
    
    for coordinate in snake_list[:-1]:
        if coordinate == snakeCoordinates:
            #print("You ate yourself!")
            win.fill(red)
            mesg(" You ate Your self ", white)
            pygame.display.update()
            time.sleep(1)
            gameExit = True
          
    win.fill(black)
    # sanke food
    win.fill(green,rect=[FoodX,FoodY,scale,scale])
    
    if len(snake_list) > snakelen:
        del snake_list[0]

    # snake Head
    # snake_list = []
    snakeCoordinates = []
    snakeCoordinates.append(snake_X)
    snakeCoordinates.append(snake_Y)
    snake_list.append(snakeCoordinates)
    #pygame.draw.rect(win,red,
    # [snake_X,snake_Y,scale,scale])
    snake(scale,snake_list,snakelen)    

    # check for snake eating food
    if snake_X == FoodX and snake_Y == FoodY:
        #print("Food has been eaten!")
        FoodX = round(random.randint(0,600-scale)/10)*10
        FoodY = round(random.randint(0,600-scale)/10)*10
        snakelen +=1
        
    

    



    # update System
    pygame.display.flip()
    clock.tick(25)  


pygame.quit()
quit()