import pygame
from random import uniform as func
from time import sleep

pygame.init()
WIDTH, HEIGHT = 400, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("My Game")

clock = pygame.time.Clock()

bound = 5
c2s = 30
white = (255, 255, 255)
black = (0, 0, 0)

x, y = WIDTH // 2, HEIGHT // 2
radius = 10
color = (0, 255, 0)  # Зелений колір

velocity = 8
vx = velocity * func(-1, 1)
vy = velocity * func(-1, 1)

border_l = bound + radius
border_u = bound + radius
border_d = HEIGHT - bound - radius
border_r = WIDTH - bound - radius

height = 10
width = 80
xp = (WIDTH - width) // 2
yp = HEIGHT - height

vp = 10

num = 1.5

score = 0

def drawScore():
    win.fill(black)
    pygame.font.init()
    path = pygame.font.match_font("arial")
    Font = pygame.font.Font(path, 30)
    text1 = ''.join([chr(int(str(el), 8)) for el in [107, 141, 155, 145, 40, 157, 166, 145, 162]])
    a = Font.render(text1, 1, (255, 255, 255))
    win.blit(a, (WIDTH // 2 - 70, HEIGHT // 3))
    text2 = f"Your score: {score}"
    b = Font.render(text2, 1, (255, 255, 255))
    win.blit(b, (WIDTH // 2 - 70, HEIGHT // 3 + 50))
    pygame.display.update()

def drawWindow():
    win.fill(black)
    pygame.draw.rect(win, white, (0, 0, WIDTH, bound))  # up
    pygame.draw.rect(win, white, (0, 0, bound, HEIGHT))  # left
    pygame.draw.rect(win, white, (WIDTH - bound, 0, bound, HEIGHT))  # right
    #pygame.draw.rect(win, white, (0, HEIGHT - bound, WIDTH, bound))  # down
    pygame.draw.circle(win, color, (x, y), radius)
    pygame.draw.rect(win, white, (xp, yp, width, height))
    pygame.display.update()

run = True

while run:
    clock.tick(c2s)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and xp > bound:
        xp -= vp
    if keys[pygame.K_RIGHT] and xp < WIDTH - bound - width:
        xp += vp
    
    if x + vx < border_l or x + vx > border_r:
        vx = -vx
    if y + vy < border_u:
        vy = -vy
    
    if y + vy > yp:
        if xp <= x + vx <= xp + width:
            vy = -vy
            vx *= num
            vy *= num
            score += 1
        else:
            drawScore()
            sleep(10)
            run = False
    
    x += vx
    y += vy

    drawWindow()

pygame.quit()
