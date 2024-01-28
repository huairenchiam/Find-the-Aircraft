import pygame
import sys
from prettytable import PrettyTable
# https://pypi.org/project/prettytable/

pygame.init()
pygame.mixer.init()
# https://www.pygame.org/docs/ref/mixer.html

WIDTH, HEIGHT = 1460,850
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Congratulations! You're win!!! ")

winbg = pygame.image.load("winbg.png")
WIN.blit(winbg,(0,0))

pygame.draw.rect(WIN,(00,00,17),(0,0,800,600),border_radius =50)

data = []
with open("name.txt","r") as f:
    for lines in f:
        line = lines.strip().split()
        if len(line) == 2 and line[1].isdigit():
            user, score = line
            data.append((user, int(score)))

data_sorted = sorted(data, key=lambda x: x[1])    
table = PrettyTable()
table.field_names = ["Rank", "Username", "Score"]

font = pygame.font.SysFont("Arial", 30)


field_names_rendered = []
for field in table.field_names:
    field_rendered = font.render(field, True, (255, 255, 255))
    field_names_rendered.append(field_rendered)

text_height = font.get_height()
x_offset = 50
y_offset = 50

for i, (user, score) in enumerate(data_sorted, start=1):
    rank_text = font.render(str(i), True, (255, 255, 255))
    user_text = font.render(user, True, (255, 255, 255))
    score_text = font.render(str(score), True, (255, 255, 255))


    for j, field_rendered in enumerate(field_names_rendered):
        WIN.blit(field_rendered, (x_offset + j * 200, y_offset))


    WIN.blit(rank_text, (x_offset, y_offset + i * text_height))
    WIN.blit(user_text, (x_offset + 200, y_offset + i * text_height))
    WIN.blit(score_text, (x_offset + 400, y_offset + i * text_height))



sound_effect = pygame.mixer.Sound("winse.mp3")
sound_effect.play()

         
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
