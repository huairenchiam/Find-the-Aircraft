import pygame
import random
import subprocess

pygame.font.init()

WIDTH, HEIGHT = 1000, 650
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Good Luck & Have Fun! ")

BG = pygame.transform.scale(pygame.image.load("spbg.jpg"),(WIDTH, HEIGHT))
text_font = pygame.font.SysFont("comicsans",17)
score_font = pygame.font.SysFont("comicsans",50)

clicked_block = []
bottom_block = []
block_empty = 0
aircraft_body = 1
aircraft_head = 2
head_up = 1
head_down = 2
head_left = 3
head_right = 4

WHITE=(255,255,255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE =(51, 102, 255)
SQUARE_SIZE = 35
SQUARE_SIZE_DISPLAY = 25
GAP_SIZE = 3
OFFSET_X, OFFSET_Y = 15, 40

size = 15

def square_green(size):
    global bottom_block, clicked_block
    bottom_block = [[block_empty]*size for _ in range(size)]
    clicked_block = [[False] * size for _ in range(size)]


#check aircraft 1 validity 
def aircraft_1_valid(head_direction, centre_i, centre_j):
    size = len(bottom_block)

    if head_direction == head_up:
        return(
        0 <= centre_i + 1 < size
        and 0 <= centre_i - 1 < size
        and 0 <= centre_j + 2 < size
        and 0 <= centre_j - 1 < size
        and bottom_block[centre_i][centre_j] == block_empty
        and bottom_block[centre_i][centre_j + 1] == block_empty
        and bottom_block[centre_i][centre_j + 2] == block_empty
        and bottom_block[centre_i][centre_j - 1] == block_empty
        and bottom_block[centre_i - 1][centre_j] == block_empty
        and bottom_block[centre_i + 1][centre_j] == block_empty
        )
    
    elif head_direction == head_down:
        return (
        0 <= centre_i + 1 < size
        and 0 <= centre_i - 1 < size
        and 0 <= centre_j + 1 < size
        and 0 <= centre_j - 2 < size
        and bottom_block[centre_i][centre_j] == block_empty
        and bottom_block[centre_i][centre_j + 1] == block_empty
        and bottom_block[centre_i][centre_j - 1] == block_empty
        and bottom_block[centre_i][centre_j - 2] == block_empty
        and bottom_block[centre_i - 1][centre_j] == block_empty
        and bottom_block[centre_i + 1][centre_j] == block_empty
        )

    elif head_direction == head_left:
        return (
        0 <= centre_i + 1 < size
        and 0 <= centre_i - 2 < size
        and 0 <= centre_j + 1 < size
        and 0 <= centre_j - 1 < size
        and bottom_block[centre_i][centre_j] == block_empty
        and bottom_block[centre_i][centre_j + 1] == block_empty
        and bottom_block[centre_i][centre_j - 1] == block_empty
        and bottom_block[centre_i - 1][centre_j] == block_empty
        and bottom_block[centre_i - 2][centre_j] == block_empty
        and bottom_block[centre_i + 1][centre_j] == block_empty
        )

    elif head_direction == head_right:
        return (
        0 <= centre_i + 2 < size
        and 0 <= centre_i - 1 < size
        and 0 <= centre_j + 1 < size
        and 0 <= centre_j - 1 < size
        and bottom_block[centre_i][centre_j] == block_empty
        and bottom_block[centre_i][centre_j + 1] == block_empty
        and bottom_block[centre_i][centre_j - 1] == block_empty
        and bottom_block[centre_i - 1][centre_j] == block_empty
        and bottom_block[centre_i + 1][centre_j] == block_empty
        and bottom_block[centre_i + 2][centre_j] == block_empty
    )
    return False

#check aircraft 2 validity 
def aircraft_2_valid(head_direction, centre_i, centre_j):
    size = len(bottom_block)

    if head_direction == head_up:
        return(
        0 <= centre_i + 1 < size
        and 0 <= centre_i - 1 < size
        and 0 <= centre_j + 2 < size
        and 0 <= centre_j - 1 < size
        and bottom_block[centre_i][centre_j] == block_empty
        and bottom_block[centre_i][centre_j + 1] == block_empty
        and bottom_block[centre_i][centre_j + 2] == block_empty
        and bottom_block[centre_i - 1][centre_j + 1] == block_empty
        and bottom_block[centre_i + 1][centre_j + 1] == block_empty
        and bottom_block[centre_i - 1][centre_j - 1] == block_empty
        and bottom_block[centre_i + 1][centre_j - 1] == block_empty
        )
    
    elif head_direction == head_down:
        return(
        0 <= centre_i + 1 < size
        and 0 <= centre_i - 1 < size
        and 0 <= centre_j + 1 < size
        and 0 <= centre_j - 2 < size
        and bottom_block[centre_i][centre_j] == block_empty
        and bottom_block[centre_i - 1][centre_j + 1] == block_empty
        and bottom_block[centre_i + 1][centre_j + 1] == block_empty
        and bottom_block[centre_i][centre_j - 1] == block_empty
        and bottom_block[centre_i - 1][centre_j - 1] == block_empty
        and bottom_block[centre_i + 1][centre_j - 1] == block_empty
        and bottom_block[centre_i][centre_j - 2] == block_empty
        )

    elif head_direction == head_left:
        return (
        0 <= centre_i + 1 < size
        and 0 <= centre_i - 2 < size
        and 0 <= centre_j + 1 < size
        and 0 <= centre_j - 1 < size
        and bottom_block[centre_i][centre_j] == block_empty
        and bottom_block[centre_i - 1][centre_j + 1] == block_empty
        and bottom_block[centre_i + 1][centre_j + 1] == block_empty
        and bottom_block[centre_i - 1][centre_j] == block_empty
        and bottom_block[centre_i - 2][centre_j] == block_empty
        and bottom_block[centre_i - 1][centre_j - 1] == block_empty
        and bottom_block[centre_i + 1][centre_j - 1] == block_empty
        )

    elif head_direction == head_right:
        return (
        0 <= centre_i + 2 < size
        and 0 <= centre_i - 1 < size
        and 0 <= centre_j + 1 < size
        and 0 <= centre_j - 1 < size
        and bottom_block[centre_i][centre_j] == block_empty
        and bottom_block[centre_i - 1][centre_j + 1] == block_empty
        and bottom_block[centre_i + 1][centre_j + 1] == block_empty
        and bottom_block[centre_i + 1][centre_j] == block_empty
        and bottom_block[centre_i + 2][centre_j] == block_empty
        and bottom_block[centre_i - 1][centre_j - 1] == block_empty
        and bottom_block[centre_i + 1][centre_j - 1] == block_empty
    )
    return False

#check aircraft 3 validity 
def aircraft_3_valid(head_direction, centre_i, centre_j):
    size = len(bottom_block)

    if head_direction == head_up:
        return (
            0 <= centre_i + 2 < size
            and 0 <= centre_i - 2 < size
            and 0 <= centre_j + 2 < size
            and 0 <= centre_j - 2 < size
            and bottom_block[centre_i][centre_j] == block_empty
            and bottom_block[centre_i][centre_j + 1] == block_empty
            and bottom_block[centre_i - 1][centre_j] == block_empty
            and bottom_block[centre_i - 2][centre_j] == block_empty
            and bottom_block[centre_i + 1][centre_j] == block_empty
            and bottom_block[centre_i + 2][centre_j] == block_empty
            and bottom_block[centre_i][centre_j - 1] == block_empty
            and bottom_block[centre_i][centre_j - 2] == block_empty
            and bottom_block[centre_i - 1][centre_j - 2] == block_empty
            and bottom_block[centre_i + 1][centre_j - 2] == block_empty
        )

    elif head_direction == head_down:
        return (
            0 <= centre_i + 2 < size
            and 0 <= centre_i - 2 < size
            and 0 <= centre_j + 2 < size
            and 0 <= centre_j - 2 < size
            and bottom_block[centre_i][centre_j] == block_empty
            and bottom_block[centre_i][centre_j - 1] == block_empty
            and bottom_block[centre_i - 1][centre_j] == block_empty
            and bottom_block[centre_i - 2][centre_j] == block_empty
            and bottom_block[centre_i + 1][centre_j] == block_empty
            and bottom_block[centre_i + 2][centre_j] == block_empty
            and bottom_block[centre_i][centre_j + 1] == block_empty
            and bottom_block[centre_i][centre_j + 2] == block_empty
            and bottom_block[centre_i - 1][centre_j + 2] == block_empty
            and bottom_block[centre_i - 2][centre_j + 2] == block_empty
        )

    elif head_direction == head_left:
        return (
            0 <= centre_i + 2 < size
            and 0 <= centre_i - 2 < size
            and 0 <= centre_j + 2 < size
            and 0 <= centre_j - 2 < size
            and bottom_block[centre_i][centre_j] == block_empty
            and bottom_block[centre_i - 1][centre_j] == block_empty
            and bottom_block[centre_i][centre_j + 1] == block_empty
            and bottom_block[centre_i][centre_j + 2] == block_empty
            and bottom_block[centre_i][centre_j - 1] == block_empty
            and bottom_block[centre_i][centre_j - 2] == block_empty
            and bottom_block[centre_i + 1][centre_j] == block_empty
            and bottom_block[centre_i + 2][centre_j] == block_empty
            and bottom_block[centre_i + 2][centre_j + 1] == block_empty
            and bottom_block[centre_i + 2][centre_j - 1] == block_empty
        )

    elif head_direction == head_right:
        return (
            0 <= centre_i + 2 < size
            and 0 <= centre_i - 2 < size
            and 0 <= centre_j + 2 < size
            and 0 <= centre_j - 2 < size
            and bottom_block[centre_i][centre_j] == block_empty
            and bottom_block[centre_i + 1][centre_j] == block_empty
            and bottom_block[centre_i][centre_j + 1] == block_empty
            and bottom_block[centre_i][centre_j + 2] == block_empty
            and bottom_block[centre_i][centre_j - 1] == block_empty
            and bottom_block[centre_i][centre_j - 2] == block_empty
            and bottom_block[centre_i - 1][centre_j] == block_empty
            and bottom_block[centre_i - 2][centre_j] == block_empty
            and bottom_block[centre_i - 2][centre_j + 1] == block_empty
            and bottom_block[centre_i - 2][centre_j - 1] == block_empty
        )

    return False


aircraft_heads = []

#Create aircraft 1
def create_aircraft_1(size):
    head_direction = random.randint(1, 4)
    i_start = 3 if head_direction == head_left else 2
    i_end = size - 2 if head_direction == head_right else size - 1
    j_start = 3 if head_direction == head_up else 2
    j_end = size - 2 if head_direction == head_down else size - 1
    centre_i = random.randint(i_start, i_end)
    centre_j = random.randint(j_start, j_end)

    if not aircraft_1_valid(head_direction, centre_i, centre_j):
        return False
    
    if head_direction == head_up:
        bottom_block[centre_i][centre_j] = aircraft_body
        bottom_block[centre_i][centre_j + 2] = aircraft_head
        aircraft_heads.append((centre_i, centre_j + 2))
        bottom_block[centre_i][centre_j + 1] = aircraft_body
        bottom_block[centre_i][centre_j - 1] = aircraft_body
        bottom_block[centre_i - 1][centre_j] = aircraft_body
        bottom_block[centre_i + 1][centre_j] = aircraft_body
    
    elif head_direction == head_down:
        bottom_block[centre_i][centre_j] = aircraft_body
        bottom_block[centre_i][centre_j - 2] = aircraft_head
        aircraft_heads.append((centre_i, centre_j - 2))
        bottom_block[centre_i][centre_j + 1] = aircraft_body
        bottom_block[centre_i][centre_j - 1] = aircraft_body
        bottom_block[centre_i - 1][centre_j] = aircraft_body
        bottom_block[centre_i + 1][centre_j] = aircraft_body

    elif head_direction == head_left:
        bottom_block[centre_i][centre_j] = aircraft_body
        bottom_block[centre_i - 2][centre_j] = aircraft_head
        aircraft_heads.append((centre_i - 2, centre_j))
        bottom_block[centre_i][centre_j + 1] = aircraft_body
        bottom_block[centre_i][centre_j - 1] = aircraft_body
        bottom_block[centre_i - 1][centre_j] = aircraft_body
        bottom_block[centre_i + 1][centre_j] = aircraft_body

    elif head_direction == head_right:
        bottom_block[centre_i][centre_j] = aircraft_body
        bottom_block[centre_i + 2][centre_j] = aircraft_head
        aircraft_heads.append((centre_i + 2, centre_j))
        bottom_block[centre_i][centre_j + 1] = aircraft_body
        bottom_block[centre_i][centre_j - 1] = aircraft_body
        bottom_block[centre_i - 1][centre_j] = aircraft_body
        bottom_block[centre_i + 1][centre_j] = aircraft_body

    return True

#Create aircraft 2
def create_aircraft_2(size):
    head_direction = random.randint(1, 4)
    i_start = 3 if head_direction == head_left else 2
    i_end = size - 2 if head_direction == head_right else size - 1
    j_start = 3 if head_direction == head_up else 2
    j_end = size - 2 if head_direction == head_down else size - 1
    centre_i = random.randint(i_start, i_end)
    centre_j = random.randint(j_start, j_end)

    if not aircraft_2_valid(head_direction, centre_i, centre_j):
        return False
    
    if head_direction == head_up:
        bottom_block[centre_i][centre_j] = aircraft_body
        bottom_block[centre_i][centre_j + 2] = aircraft_head
        aircraft_heads.append((centre_i, centre_j + 2))
        bottom_block[centre_i][centre_j + 1] = aircraft_body
        bottom_block[centre_i - 1][centre_j + 1] = aircraft_body
        bottom_block[centre_i + 1][centre_j + 1] = aircraft_body
        bottom_block[centre_i - 1][centre_j - 1] = aircraft_body
        bottom_block[centre_i + 1][centre_j - 1] = aircraft_body
    
    elif head_direction == head_down:
        bottom_block[centre_i][centre_j] = aircraft_body
        bottom_block[centre_i][centre_j - 2] = aircraft_head
        aircraft_heads.append((centre_i, centre_j - 2))
        bottom_block[centre_i - 1][centre_j + 1] = aircraft_body
        bottom_block[centre_i + 1][centre_j + 1] = aircraft_body
        bottom_block[centre_i][centre_j - 1] = aircraft_body
        bottom_block[centre_i - 1][centre_j - 1] = aircraft_body
        bottom_block[centre_i + 1][centre_j - 1] = aircraft_body

    elif head_direction == head_left:
        bottom_block[centre_i][centre_j] = aircraft_body
        bottom_block[centre_i - 2][centre_j] = aircraft_head
        aircraft_heads.append((centre_i - 2, centre_j))
        bottom_block[centre_i - 1][centre_j + 1] = aircraft_body
        bottom_block[centre_i + 1][centre_j + 1] = aircraft_body
        bottom_block[centre_i - 1][centre_j] = aircraft_body
        bottom_block[centre_i - 1][centre_j - 1] = aircraft_body
        bottom_block[centre_i + 1][centre_j - 1] = aircraft_body

    elif head_direction == head_right:
        bottom_block[centre_i][centre_j] = aircraft_body
        bottom_block[centre_i + 2][centre_j] = aircraft_head
        aircraft_heads.append((centre_i + 2, centre_j))
        bottom_block[centre_i - 1][centre_j + 1] = aircraft_body
        bottom_block[centre_i + 1][centre_j + 1] = aircraft_body
        bottom_block[centre_i + 1][centre_j] = aircraft_body
        bottom_block[centre_i - 1][centre_j - 1] = aircraft_body
        bottom_block[centre_i + 1][centre_j - 1] = aircraft_body

    return True

#Create aircraft 3
def create_aircraft_3(size):
    head_direction = random.randint(1, 4)
    i_start = 3
    i_end = size - 3
    j_start = 3
    j_end = size - 3
    centre_i = random.randint(i_start, i_end)
    centre_j = random.randint(j_start, j_end)

    if not aircraft_3_valid(head_direction, centre_i, centre_j):
        return False

    if head_direction == head_up:
        bottom_block[centre_i][centre_j] = aircraft_body
        bottom_block[centre_i][centre_j + 1] = aircraft_head
        aircraft_heads.append((centre_i, centre_j + 2))
        bottom_block[centre_i - 1][centre_j] = aircraft_body
        bottom_block[centre_i - 2][centre_j] = aircraft_body
        bottom_block[centre_i + 1][centre_j] = aircraft_body
        bottom_block[centre_i + 2][centre_j] = aircraft_body
        bottom_block[centre_i][centre_j - 1] = aircraft_body
        bottom_block[centre_i][centre_j - 2] = aircraft_body
        bottom_block[centre_i - 1][centre_j - 2] = aircraft_body
        bottom_block[centre_i + 1][centre_j - 2] = aircraft_body

    elif head_direction == head_down:
        bottom_block[centre_i][centre_j] = aircraft_body
        bottom_block[centre_i][centre_j - 1] = aircraft_head
        aircraft_heads.append((centre_i, centre_j - 2))
        bottom_block[centre_i - 1][centre_j] = aircraft_body
        bottom_block[centre_i - 2][centre_j] = aircraft_body
        bottom_block[centre_i + 1][centre_j] = aircraft_body
        bottom_block[centre_i + 2][centre_j] = aircraft_body
        bottom_block[centre_i][centre_j + 1] = aircraft_body
        bottom_block[centre_i][centre_j + 2] = aircraft_body
        bottom_block[centre_i - 1][centre_j + 2] = aircraft_body
        bottom_block[centre_i - 2][centre_j + 2] = aircraft_body

    elif head_direction == head_left:
        bottom_block[centre_i][centre_j] = aircraft_body
        bottom_block[centre_i - 1][centre_j] = aircraft_head
        aircraft_heads.append((centre_i - 1, centre_j))
        bottom_block[centre_i][centre_j + 1] = aircraft_body
        bottom_block[centre_i][centre_j + 2] = aircraft_body
        bottom_block[centre_i][centre_j - 1] = aircraft_body
        bottom_block[centre_i][centre_j - 2] = aircraft_body
        bottom_block[centre_i + 1][centre_j] = aircraft_body
        bottom_block[centre_i + 2][centre_j] = aircraft_body
        bottom_block[centre_i + 2][centre_j + 1] = aircraft_body
        bottom_block[centre_i + 2][centre_j - 1] = aircraft_body

    elif head_direction == head_right:
        bottom_block[centre_i][centre_j] = aircraft_body
        bottom_block[centre_i + 1][centre_j] = aircraft_head
        aircraft_heads.append((centre_i, centre_j + 1))
        bottom_block[centre_i][centre_j + 1] = aircraft_body
        bottom_block[centre_i][centre_j + 2] = aircraft_body
        bottom_block[centre_i][centre_j - 1] = aircraft_body
        bottom_block[centre_i][centre_j - 2] = aircraft_body
        bottom_block[centre_i - 1][centre_j] = aircraft_body
        bottom_block[centre_i - 2][centre_j] = aircraft_body
        bottom_block[centre_i - 2][centre_j + 1] = aircraft_body
        bottom_block[centre_i - 2][centre_j - 1] = aircraft_body

    return True

def block(size):
    global SQUARE_SIZE, OFFSET_X, OFFSET_Y
    for i in range(size):
        for j in range(size):
            color = WHITE
            if 0 <= i < len(clicked_block) and 0 <= j < len(clicked_block[i]):
                if clicked_block[i][j]:
                    color = [GREEN, BLUE, RED][bottom_block[i][j]]

            rect_x = j * (SQUARE_SIZE + GAP_SIZE) + OFFSET_X
            rect_y = i * (SQUARE_SIZE + GAP_SIZE) + OFFSET_Y
            # https://youtu.be/YDP1Hk7uZFA?si=_Xg5COW1n0p35uGk
            # pygame.draw.rect(screen, (255, 0, 0), (200, 100, 150, 150))
            pygame.draw.rect(WIN, color, (rect_x, rect_y, SQUARE_SIZE, SQUARE_SIZE))

block(size)


def draw_square_red_display(x, y):
    pygame.draw.rect(WIN, RED,(x, y, SQUARE_SIZE_DISPLAY, SQUARE_SIZE_DISPLAY))

def draw_square_blue_display(x, y):
    pygame.draw.rect(WIN, BLUE,(x, y, SQUARE_SIZE_DISPLAY, SQUARE_SIZE_DISPLAY))

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    WIN.blit(img, (x,y))

#DISPLAY_PLANE1
    draw_square_red_display(645, 105)
    draw_square_blue_display(672, 105)
    draw_square_blue_display(699, 105)
    draw_square_blue_display(726, 105)
    draw_square_blue_display(699, 132)
    draw_square_blue_display(699, 78)

#DISPLAY_PLANE2
    draw_square_red_display(688, 194)
    draw_square_blue_display(688, 221)
    draw_square_blue_display(688, 248)
    draw_square_blue_display(661, 221)
    draw_square_blue_display(715, 221)
    draw_square_blue_display(715, 275)
    draw_square_blue_display(661, 275)

#DISPLAY_PLANE3
    draw_square_red_display(732, 391)
    draw_square_blue_display(705, 337)
    draw_square_blue_display(705, 364)
    draw_square_blue_display(705, 391)
    draw_square_blue_display(705, 418)
    draw_square_blue_display(705, 445)
    draw_square_blue_display(678, 391)
    draw_square_blue_display(651, 391)
    draw_square_blue_display(651, 418)
    draw_square_blue_display(651, 364)



def game_start():
    square_green(size)
    max_running_times = 500
# https://www.w3schools.com/python/python_sets.asp
# thisset = {"apple", "banana", "cherry"}
#    thisset.add("orange")
#    print(thisset)
    aircraft_types_created = set()

    while len(aircraft_types_created) < 3 and max_running_times > 0:
        aircraft_type = random.choice(["Aircraft1", "Aircraft2", "Aircraft3"])

        if aircraft_type in aircraft_types_created:
            continue

        if aircraft_type == "Aircraft1":
            aircraft_1_success = create_aircraft_1(size)
            if aircraft_1_success:
                aircraft_types_created.add(aircraft_type)

        elif aircraft_type == "Aircraft2":
            aircraft_2_success = create_aircraft_2(size)
            if aircraft_2_success:
                aircraft_types_created.add(aircraft_type)

        elif aircraft_type == "Aircraft3":
            aircraft_3_success = create_aircraft_3(size)
            if aircraft_3_success:
                aircraft_types_created.add(aircraft_type)

        max_running_times -= 1

    block(size)

airplane_heads_clicked = 0
CurrentScore = 0
HighScore = 0

with open("name.txt","r") as f:
    lines = f.readlines()
    last_line = lines[-1].strip()
    user, score = last_line.rsplit(" ", 1)
    HighScore = int(score)


def block_event(event):
    global airplane_heads_clicked, CurrentScore
#https://www.tutorialspoint.com/pygame/pygame_mouse_events.htm
# if event.type == pygame.MOUSEMOTION:
#        pos=event.pos 
#        print ("x = {}, y = {}".format(pos[0], pos[1]))
    if event.type == pygame.MOUSEBUTTONDOWN:
        x, y = event.pos
        i = int((y - OFFSET_Y) // (SQUARE_SIZE + GAP_SIZE))
        j = int((x - OFFSET_X) // (SQUARE_SIZE + GAP_SIZE))

        if 0 <= i < size and 0 <= j < size and not clicked_block[i][j]:
            clicked_block[i][j] = True
            CurrentScore += 1
            block(size)
    
            if (i, j) in aircraft_heads:
                airplane_heads_clicked += 1

                if airplane_heads_clicked == 3:
                    with open("name.txt","r+") as f:
                        lines = f.readlines()
                        last_line = lines[-1].strip()
                        # https://www.w3schools.com/python/python_ref_string.asp
                        user, score = last_line.rsplit(" ", 1)
                        score = int(score)
                        if CurrentScore < score: 
                            NewScore = CurrentScore
                        else:
                            NewScore = score
                        newline = f"{user} {NewScore}" 
                        f.seek(f.tell() - len(last_line)) 
                        f.write(newline)            
                        pygame.mixer_music.pause()  
                    subprocess.run(["python", "win.py"]) 
                    
  
run = True
game_start()

pygame.mixer_music.load("gamebgm.mp3")
pygame.mixer_music.play(-1)
pygame.mixer.music.set_volume(0.5)

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
        block_event(event)


    WIN.blit(BG,(0,0))
    pygame.draw.rect(WIN,(204,255,255),(600,50,200,500),border_radius =50)
    pygame.draw.rect(WIN,(51,103,152),(622.5,498,155,35),border_radius =50)
    draw_text("Find the Aircraft", text_font,(255,255,153),630,503)

    pygame.draw.rect(WIN,(51,153,204),(810,50,180,100),border_radius =50)
    draw_text("HighScore", text_font,(255,255,153),855,60)
    draw_text(str(HighScore), score_font,(00,00,255),870,80)
    pygame.draw.rect(WIN,(51,153,204),(810,200,180,100),border_radius =50)
    draw_text("CurrentScore", text_font,(255,255,153),845,210)
    draw_text(str(CurrentScore), score_font,(00,00,255),870,230)

    block(size)

    pygame.display.flip()

pygame.quit()
   
