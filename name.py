import pygame
import sys
import subprocess
pygame.font.init()



WIDHT, HEIGHT = 1000, 650
WIN = pygame.display.set_mode((WIDHT, HEIGHT))
pygame.display.set_caption("Player's name ")


BG = pygame.transform.scale(pygame.image.load("bg.jpg"),(WIDHT, HEIGHT))
text_font = pygame.font.SysFont("impact",40)
name_font = pygame.font.SysFont("comicsans",20)

user_text =" "
input_rect = pygame.Rect(440,320,150,32)
color = pygame.Color('lightskyblue3')

RED = (255, 0, 0)
BLUE =(51, 102, 255)
SQUARE_SIZE = 50



def draw_square_red(x, y):
    pygame.draw.rect(WIN, RED,(x, y, SQUARE_SIZE, SQUARE_SIZE))

def draw_square_blue(x, y):
    pygame.draw.rect(WIN, BLUE,(x, y, SQUARE_SIZE, SQUARE_SIZE))



def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    WIN.blit(img, (x,y))



def start_game():
    if user_text.strip():
        subprocess.run(["python", "game.py"])
   
    


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                start_game()
                

            elif event.key == pygame.K_BACKSPACE:
                user_text = user_text[0:-1]
            else:
               user_text += event.unicode

            


    WIN.blit(BG,(0,0))
    draw_text("Enter  your  name :", text_font,(153,51,102),350,250)
    pygame.draw.rect(WIN,color,input_rect)

    text_surface = name_font.render(user_text,True,(153,51,102))
    WIN.blit(text_surface,(input_rect))

    input_rect.w = max(100,text_surface.get_width()+10)
            


 #plane1
    pygame.draw.rect(WIN,RED,(80,140,25,25))
    pygame.draw.rect(WIN,BLUE,(107,140,25,25))
    pygame.draw.rect(WIN,BLUE,(134,140,25,25))
    pygame.draw.rect(WIN,BLUE,(161,140,25,25))
    pygame.draw.rect(WIN,BLUE,(134,167,25,25))
    pygame.draw.rect(WIN,BLUE,(134,113,25,25))


 #plane2
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
    
 


    



