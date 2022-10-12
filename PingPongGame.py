
import pygame,sys,math

winHeight = 600
winWidth = 700
window = pygame.display.set_mode((winWidth,winHeight))

clock = pygame.time.Clock()
fps = 40

img = pygame.image.load("Background.jpg")
img = pygame.transform.scale(img, (winWidth,winHeight))

paddle1_x = winWidth/2
paddle2_x = winWidth/2
paddle1_y = 50
paddle2_y = 490

ball_x = winWidth/2
ball_y = winHeight/2

# paddle1 = pygame.draw.rect(window, pygame.Color(255,0,0), (60,50,15,15))
# paddle2 = pygame.draw.rect(window, pygame.Color(0,255,0),(60,50,15,15))
one = 0
two = 0

speedX = 1
speedY = 1

def isCollison(ballX,ballY, paddleX,paddleY):
    distance = math.sqrt(math.pow(ballX-paddleX,2) + math.pow(ballY-paddleY,2))
    if distance < 70:
        return True
    else:
        return False


while True:
    window.blit(img, (0,0))
    # window.blit(paddle1, (paddle1_x,paddle1_y))
    # window.blit(paddle2, (paddle2_x,paddle2_y))

    paddle1 = pygame.draw.rect(window, pygame.Color(255,0,0), (paddle1_x,paddle1_y,100,50))  # type: ignore
    paddle2 = pygame.draw.rect(window, pygame.Color(0,255,0),(paddle2_x,paddle2_y,100,50))  # type: ignore


    ball_x += speedX
    ball_y += speedY

    ball = pygame.draw.circle(window, pygame.Color("#E1ED1C"),(ball_x,ball_y),20)

    
    if paddle1_x <= 10:
        paddle1_x += 5
    elif paddle1_x >= (winWidth - 150):
        paddle1_x -= 5
    elif paddle2_x <= 10:
        paddle2_x += 5
    elif paddle2_x >= (winWidth - 150):
        paddle2_x -= 5

    paddle1_x += one
    paddle2_x += two
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                one = 5
            elif event.key == pygame.K_LEFT:
                one= -5
            elif event.key == pygame.K_a:
                two = -5
            elif event.key == pygame.K_d:
                two = 5
        
        if event.type == pygame.KEYUP:
            one = 0
            two = 0
    
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    
    if ball_x >= winWidth-40:
        speedX *= -1
    elif ball_x < 10:
        speedX *= -1

    
    # if isCollison(ball_x,ball_y,paddle1_x,paddle1_y+36):
    #     print("Collided 1")
    #     speedY *= -1
        

    # elif isCollison(ball_x,ball_y,paddle2_x,paddle2_y+55):
    #     print("Collided 2")
    #     speedY *= -1

    if paddle1.collidepoint(ball_x-20,ball_y-20):
        print("Collided 1")
        speedY *= -1

    elif paddle2.collidepoint(ball_x+20,ball_y+20):
        print("Collided 2")
        speedY *= -1


    clock.tick(fps)
    pygame.display.update()