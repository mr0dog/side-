import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('side-scrolling Game')
clock = pygame.time.Clock()

player = [100, 450, 0, 0] #xpos, ypos, xvel, yvel
platforms = [(500, 400), (700, 300)]
isonground = False
offset = 0
# platform collision

def move_player():
    global isonground #needed to modify a global variable from within a function
    global offset
    isonground = False
    if player[1]+ 50>= 530:
        player[1] = 530 - 50
        isonground = True
    for i in range(len(platforms)):
        if player[0]+50>platforms[i][0]+offset and player[0]<platforms[i][0]+100+offset and player[1]+50>platforms[i][1] and player[1]+50< platforms[i][1]+50:
            isonground = True #stop gravity
            player[1]=platforms[i][1]-50 #reset player feet
            player[3] = 0 #stop downward velocity
            #print("on platform") #for teating
            
    if keys[pygame.K_LEFT]:
        if offset > 260 and player[0]>0: 
            player[2] = -5
            
        elif player[0]>400 and offset < -1500:#check if youve reached the left edge of the map
            player[2] = -5#let player get back to the center of the game screen
        
        elif player[0]>0: #if player is recentered move the offset not the player
            offset += 5
            player[2] = 0
            
        else:
            player[2]=0 #make sure motion is off (stops from going off edge)
            
#         player[2] =- 5 #update velocity
        offset += 5
    elif keys[pygame.K_RIGHT]:
        if offset < -1500 and player[0]<750:
            player[2] = 5
           
        elif offset >260 and player[0]<400:
              player[2] = 5
       
       
        elif player[0]<750:
            offset -= 5
            player[2] = 0
        else:
            player[2]=0
    if isonground == True and keys[pygame.K_UP]:
            player[3] = -15 # player jumps
            isonground = False
               
    if isonground == False:
        player[3] += 1 #Gravity
    
        
        # jump mechanics
       
     
        
    player[0]+=player[2] #add x velocity to x position
    player[1]+=player[3] #add x velocity to y position
   # print(player[0],player[1])
running = True
def draw_clouds():
    for x in range(100, 800, 300): #this loop controls WHERE and HOW MANY clouds are drawn
        for i in range(3): #draw 3 circles
         pygame.draw.circle(screen, (255,255,255), (x + offset, 100), 40)
         pygame.draw.circle(screen, (155,255,255), (x - 50 + offset, 125), 40)
         pygame.draw.circle(screen, (255,255,255), (x + 50 + offset, 125), 40)
    pygame.draw.rect(screen, (244,255,255), (x - 50 + offset, 100, 100, 65)) #flatten bottom edge
        # draw trees
def draw_trees():
    for x in range(100, 800, 300):
         for i in range(3):
          pygame.draw.rect(screen, (165,42,42), (x - 30 + offset, 300, 40, 309))
          pygame.draw.circle(screen, (0,128,0), (x + offset, 300), 50)
          pygame.draw.circle(screen, (0,128,0), (x - 50 + offset, 325), 40)
          pygame.draw.circle(screen, (0,128,0), (x + 50 + offset, 325), 40)
          
def draw_platforms():
    for i in range(len(platforms)):
        pygame.draw.rect(screen, (150, 10, 10), (platforms[i][0] + offset, platforms[i][1], 100, 30))
while running: # main game loop +++++++++++++++++++++++++++++++++++++++++++++++++++++++
    clock.tick(60)
    #input section --------------------------------------------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    keys = pygame.key.get_pressed()
    #pyysics section+++++++++++++++++++++++++++++++++++++++++++++++++++
    move_player()
    #render section++++++++++++++++++++++++++++++++++++++++++++++++++++
    screen.fill((135, 206, 235)) # sky blue backround
    draw_clouds() #function call
    draw_trees() #function call for trees
    draw_platforms() #function call for platforms
    pygame.draw.rect(screen, (40,125,30), (0, 530, 900, 80))
    pygame.draw.rect(screen, (255, 0, 255), (player[0], player[1], 50, 50)) #player
    pygame.display.flip()
    
pygame.quit()
