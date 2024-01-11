
import pygame
import subprocess
pygame.font.init()


WIDHT, HEIGHT = 1000, 650
WIN = pygame.display.set_mode((WIDHT, HEIGHT))
pygame.display.set_caption("Find the Aircraft")


BG = pygame.transform.scale(pygame.image.load("bg.jpg"),(WIDHT, HEIGHT))
text_font = pygame.font.SysFont("impact",70)
RED = (255, 0, 0)
BLUE =(51, 102, 255)
SQUARE_SIZE = 50

start_img = pygame.image.load("start_btn.png").convert_alpha()
exit_img = pygame.image.load("exit_btn.png").convert_alpha()



def draw_square_red(x, y):
    pygame.draw.rect(WIN, RED,(x, y, SQUARE_SIZE, SQUARE_SIZE))


def draw_square_blue(x, y):
    pygame.draw.rect(WIN, BLUE,(x, y, SQUARE_SIZE, SQUARE_SIZE))



def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    WIN.blit(img, (x,y))

    

def draw():
    WIN.blit(BG,(0,0))
    draw_text("Find  the  Aircraft", text_font,(128,0,0),265,220)



#button class
class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image,(int(width*scale),int(height*scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        action = False

        #get mouse position
        pos = pygame.mouse.get_pos()
        #check mouseover and clicked condition
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
               
            

        if pygame.mouse.get_pressed()[0] ==0:
            self.clicked = False

        #draw button on screen
        WIN.blit(self.image, (self.rect.x, self.rect.y))

        return action

#create button instance
start_button = Button(430, 350, start_img, 0.5)
exit_button = Button(440, 430, exit_img, 0.5)


def start_game():
    subprocess.run(["python", "name.py"])


run = True
while run:

    if start_button.draw():
        start_game()
        
    if exit_button.draw():
        run = False
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False


    
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
    draw()

pygame.quit()
