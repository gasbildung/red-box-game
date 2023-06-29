import pygame, random


WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
GREEN=(0,255,0)
speed=5
pygame.init()
height=400
width=400
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("Red box game")
clock=pygame.time.Clock()
blocksize=20
direction=(0,0)
red_box_x=100
red_box_y=100
barrier_xs=[]
barrier_ys=[]
score=0
difficulty=5

def generate_random_coordinates(extent,limit):
    """Generates random coordinates for food and barrier"""
    return (random.randint(2,(extent-2*limit)//limit))*limit
    


food_x=generate_random_coordinates(width,blocksize)
food_y=generate_random_coordinates(height,blocksize)



def drawGrid():
    """Draws grid on the screen"""
    blockSize=20
    for x in range(0,width,blockSize):
        for y in range(0,height,blockSize):
            rect=pygame.Rect(x,y,blockSize,blockSize)
            pygame.draw.rect(screen,WHITE,rect)

def drawRedBox(x,y,blockSize):
    """Draws red box on the screen"""
    rect=pygame.Rect(x,y,blockSize,blockSize)
    pygame.draw.rect(screen,RED,rect)
    
def drawFood(x,y,blockSize):
    """Draws food on the screen"""
    rect=pygame.Rect(x,y,blockSize,blockSize)
    pygame.draw.rect(screen,GREEN,rect)

def drawBarrier(x,y,blockSize):
    """Draws barrier on the screen"""
    rect=pygame.Rect(x,y,blockSize,blockSize)
    pygame.draw.rect(screen,BLACK,rect)

def generateBarrier(barrier_xs,barrier_ys):
    """Generates barrier coordinates"""
    barrier_xs.append(generate_random_coordinates(width,blocksize))
    barrier_ys.append(generate_random_coordinates(height,blocksize))

def checkCollision(x1,y1,x2,y2):
    """Checks collision between two objects"""
    if x1==x2 and y1==y2:
        return True
    else:
        return False

def restart():
    """Restarts the game"""
    global direction,red_box_x,red_box_y,food_x,food_y,barrier_xs,barrier_ys,speed,score
    direction=(0,0)
    red_box_x=100
    red_box_y=100
    barrier_xs=[]
    barrier_ys=[]
    score=0
    speed=5
    food_x=generate_random_coordinates(width,blocksize)
    food_y=generate_random_coordinates(height,blocksize)
    main()

def gameOver():
    """Displays game over screen"""
    global score
    screen.fill(WHITE)
    font=pygame.font.SysFont(None,100)
    text=font.render("Score: "+str(score),True,BLACK)
    screen.blit(text,[width/8,height/2])    
    pygame.display.update()
    pygame.time.wait(5000)
    restart()



def main():
    """Main function"""
    global direction,red_box_x,red_box_y,food_x,food_y,barrier_xs,barrier_ys,speed,score
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    direction=(-1,0)
                elif event.key==pygame.K_RIGHT:
                    direction=(1,0)
                elif event.key==pygame.K_UP:
                    direction=(0,-1)
                elif event.key==pygame.K_DOWN:
                    direction=(0,1)
        screen.fill(BLACK)
        drawGrid()
        red_box_x+=direction[0]*blocksize
        red_box_y+=direction[1]*blocksize
        drawRedBox(red_box_x,red_box_y,blocksize)
        drawFood(food_x,food_y,blocksize)
        
        if checkCollision(red_box_x,red_box_y,food_x,food_y):
            
            food_x=generate_random_coordinates(width,blocksize)
            food_y=generate_random_coordinates(height,blocksize)
            break_num=0
            while food_x in barrier_xs and food_y in barrier_ys:
                print(food_x)
                print(food_y)
                food_x=generate_random_coordinates(width,blocksize)
                food_y=generate_random_coordinates(height,blocksize)
                break_num+=1
                if break_num>100:
                    food_x=generate_random_coordinates(width,blocksize)
                    food_y=generate_random_coordinates(height,blocksize)
                    break
            speed+=1
            score+=1
            for i in range(difficulty):
                generateBarrier(barrier_xs,barrier_ys)

        for i in range(len(barrier_xs)):
            drawBarrier(barrier_xs[i],barrier_ys[i],20)
            if checkCollision(red_box_x,red_box_y,barrier_xs[i],barrier_ys[i]):
                direction=(0,0)
                gameOver()
        
        if red_box_x<10 or red_box_x>width-10 or red_box_y<10 or red_box_y>height-10:
            direction=(0,0)
            speed=5



        pygame.display.update()
        clock.tick(speed)
        


if __name__=="__main__":
    main()
