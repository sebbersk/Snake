import sys, pygame,time,random

pygame.init()

size = width, height = 620, 620
black = 0, 0, 0
gray = 150,150,150
white = 255,255,255
red = 255,0,0
clock = pygame.time.Clock()
w=30
grid= [[n]*20 for n in range(20)]
offset= 10
snake_img = pygame.image.load('snake.jpg')
snake_img = pygame.transform.scale(snake_img,(w,w))
food_img = pygame.image.load('food.jpg')
food_img = pygame.transform.scale(food_img,((w,w)))
sx=offset+w
sy=offset
score=0
ssx=0
ssy=0
snake = [(sx,sy)]
bpos= [n for n in range(20)]
bx=(random.choice(bpos))*w + offset
by=bx
screen = pygame.display.set_mode(size)
pygame.display.set_caption('SNAKE')

while True:
    font = pygame.font.SysFont('Comic Sans MS',16)
    text = font.render(f'Score: {score}', True, white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                ssy=w
                ssx=0
            elif event.key == pygame.K_UP:
                ssy=-w
                ssx=0
            elif event.key == pygame.K_LEFT:
                ssx=-w
                ssy=0
            elif event.key == pygame.K_RIGHT:
                ssx=w
                ssy=0
            elif event.key == pygame.K_SPACE:
                sys.exit()
        else:
            pass
    screen.fill(black)
    x= offset
    y= offset
    for row in grid:
        for col in row:
            rect = pygame.Rect(x,y,w,w)
            pygame.draw.rect(screen,gray,rect,1)
            x+=w
        y+=w
        x=offset
    screen.blit(food_img,(bx,by))
    sx+=ssx
    sy+=ssy
    if (len(snake) > 1):
        if ((sx,sy) in snake):
            break
    snake.insert(0, tuple((sx,sy)))
    if (bx== sx and by ==sy):
        bx=(random.choice(bpos))*w + offset
        by=bx
        score+=1
    else:
        snake.pop()
    
    for point in snake:
        screen.blit(snake_img,(point[0],point[1]))
    if(sx > width-offset-w or sx < 0 or sy >height-offset-w or sy <0):
        break
    screen.blit(text,(190,0))
    pygame.display.flip()
    clock.tick(10)
print(score)
