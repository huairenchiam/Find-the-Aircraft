import pygame
pygame.font.init()

WIDHT, HEIGHT = 1000, 650
WIN = pygame.display.set_mode((WIDHT, HEIGHT))
pygame.display.set_caption("Good Luck & Have Fun! ")

BG = pygame.transform.scale(pygame.image.load("spbg.jpg"),(WIDHT, HEIGHT))
text_font = pygame.font.SysFont("comicsans",20)

WHITE=(255,255,255)
RED = (255, 0, 0)
BLUE =(51, 102, 255)
SQUARE_SIZE = 50
SQUARE_SIZE_DISPLAY = 25
GAP_SIZE = 5
OFFSET_X, OFFSET_Y = 80, 55


def draw_square_white(x, y):
    pygame.draw.rect(WIN, WHITE,(x, y, SQUARE_SIZE, SQUARE_SIZE))
    
def draw_square_red(x, y):
    pygame.draw.rect(WIN, RED,(x, y, SQUARE_SIZE, SQUARE_SIZE))

def draw_square_blue(x, y):
    pygame.draw.rect(WIN, BLUE,(x, y, SQUARE_SIZE, SQUARE_SIZE))

def draw_square_red_display(x, y):
    pygame.draw.rect(WIN, RED,(x, y, SQUARE_SIZE_DISPLAY, SQUARE_SIZE_DISPLAY))

def draw_square_blue_display(x, y):
    pygame.draw.rect(WIN, BLUE,(x, y, SQUARE_SIZE_DISPLAY, SQUARE_SIZE_DISPLAY))

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    WIN.blit(img, (x,y))
    


    for row in range(10):
        for col in range(10):
            square_x = OFFSET_X + col * (SQUARE_SIZE + GAP_SIZE)
            square_y = OFFSET_Y + row * (SQUARE_SIZE + GAP_SIZE)
            
            draw_square_white(square_x, square_y)

            
            if (row == 1 and col == 5) or (row == 6 and col == 7) or (row == 8 and col == 2):
                draw_square_red(square_x, square_y)

            if (row == 0 and col == 3) or (row == 1 and col == 2) or (row == 1 and col == 3) or(row == 1 and col ==4 )or (row == 2 and col ==3 )or(row == 4 and col ==1 )or(row == 4 and col ==2 )or(row == 4 and col ==3 )or(row == 5 and col ==2 )or(row == 6 and col ==0 )or(row == 6 and col == 1)or(row ==6  and col ==2 )or(row == 6 and col == 3)or(row == 6 and col == 4)or(row == 7 and col == 2)or(row == 7 and col ==6 )or(row == 7 and col ==7 )or(row ==7  and col ==8 )or(row == 8 and col ==7 )or(row == 9 and col == 6)or(row == 9 and col ==8) :
                draw_square_blue(square_x, square_y)

#PLANE1
    draw_square_red_display(770, 130)
    draw_square_blue_display(797, 130)
    draw_square_blue_display(824, 130)
    draw_square_blue_display(851, 130)
    draw_square_blue_display(824, 157)
    draw_square_blue_display(824, 103)

#PLANE2
    draw_square_red_display(813, 219)
    draw_square_blue_display(813, 246)
    draw_square_blue_display(813, 273)
    draw_square_blue_display(786, 246)
    draw_square_blue_display(840, 246)
    draw_square_blue_display(840, 300)
    draw_square_blue_display(786, 300)

#PLANE3
    draw_square_red_display(867, 416)
    draw_square_blue_display(813, 362)
    draw_square_blue_display(813, 389)
    draw_square_blue_display(813, 416)
    draw_square_blue_display(813, 443)
    draw_square_blue_display(813, 470)
    draw_square_blue_display(786, 416)
    draw_square_blue_display(759, 416)
    draw_square_blue_display(840, 416)
    draw_square_blue_display(759, 443)
    draw_square_blue_display(759, 389)


run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False


    WIN.blit(BG,(0,0))
    pygame.draw.rect(WIN,(204,255,255),(700,80,250,500),border_radius =50)
    pygame.draw.rect(WIN,(51,103,152),(725,528,200,35),border_radius =50)
    draw_text("Find the Aircraft", text_font,(255,255,153),743,530)
    


    pygame.display.flip()
   
