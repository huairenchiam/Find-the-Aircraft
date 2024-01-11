
import pygame
pygame.font.init()

WIDHT, HEIGHT = 1000, 650
WIN = pygame.display.set_mode((WIDHT, HEIGHT))
pygame.display.set_caption("Good Luck & Have Fun! ")

BG = pygame.transform.scale(pygame.image.load("spbg.jpg"),(WIDHT, HEIGHT))

WHITE=(255,255,255)
RED = (255, 0, 0)
BLUE =(51, 102, 255)
SQUARE_SIZE = 50
GAP_SIZE = 5
OFFSET_X, OFFSET_Y = 80, 55
text_font = pygame.font.SysFont("comicsans",20)

def draw_square_white(x, y):
    pygame.draw.rect(WIN, WHITE,(x, y, SQUARE_SIZE, SQUARE_SIZE))
    
def draw_square_red(x, y):
    pygame.draw.rect(WIN, RED,(x, y, SQUARE_SIZE, SQUARE_SIZE))

def draw_square_blue(x, y):
    pygame.draw.rect(WIN, BLUE,(x, y, SQUARE_SIZE, SQUARE_SIZE))

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    WIN.blit(img, (x,y))
    

def draw():
    WIN.blit(BG,(0,0))
    pygame.draw.rect(WIN,(204,255,255),(700,80,250,500),border_radius =50)
    pygame.draw.rect(WIN,(51,103,152),(725,528,200,35),border_radius =50)
    draw_text("Find the Aircraft", text_font,(255,255,153),743,530)
    
    # Draw a 10x10 grid of squares
    for row in range(10):
        for col in range(10):
            square_x = OFFSET_X + col * (SQUARE_SIZE + GAP_SIZE)
            square_y = OFFSET_Y + row * (SQUARE_SIZE + GAP_SIZE)
            
            draw_square_white(square_x, square_y)

            
            if (row == 1 and col == 5) or (row == 6 and col == 7) or (row == 8 and col == 2):
                draw_square_red(square_x, square_y)

            if (row == 0 and col == 3) or (row == 1 and col == 2) or (row == 1 and col == 3) or(row == 1 and col ==4 )or (row == 2 and col ==3 )or(row == 4 and col ==1 )or(row == 4 and col ==2 )or(row == 4 and col ==3 )or(row == 5 and col ==2 )or(row == 6 and col ==0 )or(row == 6 and col == 1)or(row ==6  and col ==2 )or(row == 6 and col == 3)or(row == 6 and col == 4)or(row == 7 and col == 2)or(row == 7 and col ==6 )or(row == 7 and col ==7 )or(row ==7  and col ==8 )or(row == 8 and col ==7 )or(row == 9 and col == 6)or(row == 9 and col ==8) :
                draw_square_blue(square_x, square_y)

#PLANE 1
    pygame.draw.rect(WIN,RED,(770,130,25,25))
    pygame.draw.rect(WIN,BLUE,(797,130,25,25))
    pygame.draw.rect(WIN,BLUE,(824,130,25,25))
    pygame.draw.rect(WIN,BLUE,(851,130,25,25))
    pygame.draw.rect(WIN,BLUE,(824,157,25,25))
    pygame.draw.rect(WIN,BLUE,(824,103,25,25))

#PLANE2
    pygame.draw.rect(WIN,RED,(813,219,25,25))
    pygame.draw.rect(WIN,BLUE,(813,246,25,25))
    pygame.draw.rect(WIN,BLUE,(813,273,25,25))
    pygame.draw.rect(WIN,BLUE,(786,246,25,25))
    pygame.draw.rect(WIN,BLUE,(840,246,25,25))
    pygame.draw.rect(WIN,BLUE,(840,300,25,25))
    pygame.draw.rect(WIN,BLUE,(786,300,25,25))


#PLANE3
    pygame.draw.rect(WIN,RED,(867,416,25,25))
    pygame.draw.rect(WIN,BLUE,(813,362,25,25))
    pygame.draw.rect(WIN,BLUE,(813,389,25,25))
    pygame.draw.rect(WIN,BLUE,(813,416,25,25))
    pygame.draw.rect(WIN,BLUE,(813,443,25,25))
    pygame.draw.rect(WIN,BLUE,(813,470,25,25))
    pygame.draw.rect(WIN,BLUE,(786,416,25,25))
    pygame.draw.rect(WIN,BLUE,(759,416,25,25))
    pygame.draw.rect(WIN,BLUE,(840,416,25,25))
    pygame.draw.rect(WIN,BLUE,(759,443,25,25))
    pygame.draw.rect(WIN,BLUE,(759,389,25,25))


    
    pygame.display.flip()



def main():

    


    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

  

        draw()
        
       

    pygame.quit()
   

if __name__ == "__main__":
    main()
