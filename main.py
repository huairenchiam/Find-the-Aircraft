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
SQUARE_SIZE = 25

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



class Button():
    def __init__(self, x, y, image, scale):
        width, height = image.get_size()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.clicked = False


    def draw(self):
        action = False
        mouse_pos = pygame.mouse.get_pos()
       
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked :
                self.clicked = True
                action = True
               
            

        if pygame.mouse.get_pressed()[0] ==0:
            self.clicked = False

        
        WIN.blit(self.image, (self.rect.x, self.rect.y))
        return action


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
    draw_square_red(80, 140)
    draw_square_blue(107, 140)
    draw_square_blue(134, 140)
    draw_square_blue(161, 140)
    draw_square_blue(134, 167)
    draw_square_blue(134, 113)

#plane2
    draw_square_red(867, 416)
    draw_square_blue(813, 362)
    draw_square_blue(813, 389)
    draw_square_blue(813, 416)
    draw_square_blue(813, 443)
    draw_square_blue(813, 470)
    draw_square_blue(786, 416)
    draw_square_blue(759, 416)
    draw_square_blue(840, 416)
    draw_square_blue(759, 443)
    draw_square_blue(759, 389)

    



    pygame.display.flip()
    draw()
