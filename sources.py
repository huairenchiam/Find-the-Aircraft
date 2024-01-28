#BUTTON at start.py
#https://youtu.be/G8MYGDf_9ho?si=mJoxtZJy4amhQZzD
start_img = pygame.image.load("start_btn.png").convert_alpha()
exit_img = pygame.image.load("exit_btn.png").convert_alpha()

class Button():
    def _init_(self, x, y, image, scale):
        width= image.get_size()
        height = image.get_size()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)


def draw(self):
        action = False
        pos = pygame.mouse.get_pos()
       
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and  self.clicked == False :
                self.clicked = True
                action = True
        
        if pygame.mouse.get_pressed()[0] ==0:
            self.clicked = False
  
        WIN.blit(self.image, (self.rect.x, self.rect.y))
        return action


start_button = Button(430, 350, start_img, 0.5)
exit_button = Button(440, 430, exit_img, 0.5)



#TEXT INPUT at name.py
#https://youtu.be/Rvcyf4HsWiw?si=prVz7CMeenWEslek
name_font = pygame.font.SysFont("comicsans",20)
user_text =" "

for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
               active = True

        if event.type == pygame.KEYDOWN:
            if active == True:
                if event.key == pygame.K_BACKSPACE:
                   user_text = user_text[:-1]
                else:
 
                    user_text += event.unicode

text_surface = name_font.render(user_text,True,(153,51,102))
input_rect.w = max(100,text_surface.get_width()+10)
            

#text display
#https://youtu.be/ndtFoWWBAoE?si=W6R4cqamS54C65wk
text_font = pygame.font.SysFont("impact",70)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    WIN.blit(img, (x,y))
