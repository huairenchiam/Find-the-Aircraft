#Leong Wing Yan

import pygame
import sys
import subprocess

pygame.font.init()

#Chan Jia Hui
pygame.mixer.init()

#Leong Wing Yan
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
SQUARE_SIZE = 25


def draw_square_red(x, y):
    pygame.draw.rect(WIN, RED,(x, y, SQUARE_SIZE, SQUARE_SIZE))

def draw_square_blue(x, y):
    pygame.draw.rect(WIN, BLUE,(x, y, SQUARE_SIZE, SQUARE_SIZE))

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    WIN.blit(img, (x,y))


def start_game():
    #Chan Jia Hui
    global user_text
    if user_text.strip():
        # https://www.geeksforgeeks.org/how-to-open-a-file-using-the-with-statement/
        with open("name.txt", "r+", encoding="utf-8") as f: 
            lines = f.readlines()
            user_exists = False

            # https://www.geeksforgeeks.org/enumerate-in-python/
            for i, line in enumerate(lines):
                if line.strip():
                    user, score = line.strip().split()
                    if user_text.strip() == user.strip():
                        user_exists = True
                        newline = f"{user} {score}\n"
                        del lines[i]
                        break
            if not user_exists:
                newline = f"{user_text.strip()} 0\n"

            lines.append(newline)
            # https://www.w3schools.com/python/python_ref_file.asp
            f.seek(0)
            f.truncate()
            f.writelines(lines)

        #Leong Wing Yan
        subprocess.run(["python", "game.py"])
   

run = True

#chan Jia Hui
sound_effect = pygame.mixer.Sound("namese.mp3")
sound_effect.play()

#Leong Wing Yan
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

    draw_square_red(80, 140)
    draw_square_blue(107, 140)
    draw_square_blue(134, 140)
    draw_square_blue(161, 140)
    draw_square_blue(134, 167)
    draw_square_blue(134, 113)

    # Plane 2
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
    
    
 


 


    



