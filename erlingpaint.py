import pygame
import time
import timer

pygame.init()

# COLOUR
BLACK = (0, 0, 0)
WHITE = (250, 250, 250)
RED = (250, 0, 0)
GREEN = (255, 255, 0)
BLUE = (0, 0, 250)


p = 0
i = 0
ii = 0
iii = 255

W = 1200
H = 800
run = True
clock = pygame.time.Clock()
event = pygame.event.get()

# pos = pygame.mouse.get_pos()

nedtrykk = False

colour_pen = WHITE

draw_list = []
colour_list = []
spising = False
spisetid = time.time()
spisetid_1 = time.time()+1
screen = pygame.display.set_mode((W,H))

player_pos = pygame.Vector2((W/2, H/2))
PLAYER_COLOR = pygame.Color(90, 140, 190)

text_font = pygame.font.SysFont("Arial", 30)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x,y))
    
class colour_cord:
    def __init__(self, x, colour):
        self.colour = colour
        self.x = x
    

ball = pygame.image.load("smil.jpg").convert()
ball2 = pygame.image.load("smil2.jpg").convert()

ball_pos = ball.get_rect(topleft=(W/2, H/2))
ball_pos2 = ball2.get_rect(topleft=(W/2, H/2))

player_img = pygame.Surface((40,60))
player_img.fill((90,140,190))
player_rect = player_img.get_rect(center=(200,200))

# class draw_color_box():
#     pygame.draw.rect(screen, GREEN, (0,0,40,40))
#     def draw():
#         if pos[0] in range(0+40):
#             if pos[1] in range(0+40):
#                 # if event.type == pygame.MOUSEBUTTONDOWN:
#                 colour_pen = GREEN
#                 print("Grønn registrert")
            

class tegne:
    def __init__(self, colour, x_y):
        self.colour = colour
        self.x_y = x_y
        self.x = x_y[0] 
        self.y = x_y[1]
    
class Iterator:
    def __init__(self, limit):
        self.limit = limit
        
    def __iter__(self):
        self.RGB = 1
        
    def __next__(self):
        x = self.x
        if x > 255:
            raise StopIteration

while run:

    spisetid = time.time()
    draw_text("VELKOMMEN TIL ERLINGS PAINT", text_font, WHITE, 0, 100)
    

    if spising == True:
        ball = pygame.image.load("smil2.jpg").convert()
    else:
        spising == False
        ball = pygame.image.load("smil.jpg").convert()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        pos = pygame.mouse.get_pos()

        
    if event.type == pygame.MOUSEBUTTONDOWN:
        nedtrykk = True
    if event.type == pygame.MOUSEBUTTONUP:
        nedtrykk = False
        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and ball_pos.y not in range (0,41):
        ball_pos.y -= 2  
    if keys[pygame.K_s] and ball_pos.y != H-ball_pos.height:
        ball_pos.y += 2
    if keys[pygame.K_a] and ball_pos.x != 0:
        ball_pos.x -= 2 
    if keys[pygame.K_d] and ball_pos.x not in range (W-ball_pos.width,W):
        ball_pos.x += 2 
    if keys[pygame.K_z]:
        if len(draw_list) > 0:
            draw_list.pop()
    
    
    # if pos[0] in range(ball_pos.x , ball_pos.x + ball_pos.w) :
    #     if pos[1] in range(ball_pos.y, ball_pos.y + ball_pos.h):
    #         None

    # if nedtrykk == True:   
    #     draw_list.append((pos[0], pos[1]))
    
    # for drawings in draw_list:
    #     pygame.draw.circle(screen, colour_pen, drawings, 1)
        
    if nedtrykk == True and pos[0] in range(0,W) and pos[1] in range (40,H):
        draw_list.append(tegne(colour_pen, (pos[0], pos[1])))
    
    for obj in draw_list:
        if obj.colour == BLACK:
            pygame.draw.circle(screen, obj.colour, (obj.x_y),20)
        else:
            pygame.draw.circle(screen, obj.colour, (obj.x_y),5)
    
#farge valg der man trykker
    pygame.draw.rect(screen, GREEN, (0,0,40,40))   
    if pos[0] in range(0,40):
        if pos[1] in range(0,40):
            if event.type == pygame.MOUSEBUTTONDOWN:
                colour_pen = GREEN
    pygame.draw.rect(screen, BLACK, (40,0,40,40))   
    if pos[0] in range(40,80):
        if pos[1] in range(0,40):
            if event.type == pygame.MOUSEBUTTONDOWN:
                colour_pen = BLACK
    pygame.draw.rect(screen,WHITE, (80,0,40,40))   
    if pos[0] in range(80,120):
        if pos[1] in range(0,40):
            if event.type == pygame.MOUSEBUTTONDOWN:
                colour_pen = WHITE

                
# Fargeindex

    while i < 255 and iii <= 255:
        pygame.draw.rect(screen, (i,ii,iii), (255+p,0,1,40))
        while ii >= 0 and i < 255:
            if p >= 255+255:
                break
            while iii > 0 and i == 0:      
                iii -= 1
                ii += 1
                p += 1
                pygame.draw.rect(screen, (i,ii,iii), (255+p,0,1,40)) 
                colour_list.append(colour_cord(255+p, (i,ii,iii)))
            ii -= 1
            i += 1
            p += 1
            pygame.draw.rect(screen, (i,ii,iii), (255+p,0,1,40))
            colour_list.append(colour_cord(255+p, (i,ii,iii)))
        i -= 1
        iii +=1
        p += 1
        colour_list.append(colour_cord(255+p, (i,ii,iii)))
        
 #farge valg der man trykker
    if pos[0] in range(255,255+p):
        if pos[1] in range (0, 40):
            if event.type == pygame.MOUSEBUTTONDOWN:
                for farge in colour_list:
                    if pos[0] == farge.x:
                        colour_pen = farge.colour
     
     
#  viskelær i form av spising (munn lukket og åpner)
    # for obj in draw_list:
    #     if obj.x in range(ball_pos.x,(ball_pos.x+ball_pos.width)):
    #         if obj.y in range(ball_pos.y, (ball_pos.y+ball_pos.height)):
    #             spising = True
    #             spisetid_1 = time.time()+0.25
    #             draw_list.remove(obj)
    #     if obj.x not in range(ball_pos.x,(ball_pos.x+ball_pos.width)):
    #         if spisetid_1 < spisetid:
    #             spisetid = time.time() 
    #             spising = False
    # if len(draw_list) == 0:
    #     if spisetid_1 < spisetid:
    #         spisetid = time.time() 
    #         spising = False


    screen.blit(ball, ball_pos)
    pygame.display.flip()
    # screen.fill(BLACK)
    pygame.draw.rect(screen, BLACK, (0,40,W,H))

    clock.tick(1000)
    # print(clock.tick(40))a
    # dt = clock.tick(60) / 1000
    
pygame.quit()

