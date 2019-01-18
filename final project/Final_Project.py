"""the main interface for final project"""
import pygame
import data_base_fuctions
import high_score_page
import sys
import os
import games.game_snake
import games.Space_invaders



pygame.init()
pygame.mixer.init()


s = pygame.mixer.Sound(sound("file name"))
s.play()


screen = pygame.display.set_mode((800, 600))
color_inactive = pygame.Color('black')
color_active = pygame.Color('white')
FONT = pygame.font.Font(None, 45)
pygame.mouse.set_visible(False)


class Username_Box:

    def __init__(self,x,y,w,h, text =''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = ((0,0,0))
        self.text = ""
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False
        self.has_text = False 
      
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
        
            self.color = color_active if self.active else color_inactive

        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                    if len(self.text)> 12:
                        self.text = self.text[:-1]
                self.txt_surface = FONT.render(self.text, True, self.color)
    

    def return_username(self):
        if self.has_text:
            return self.text
        pass
        
    def update(self):
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(screen, self.color, self.rect, 2)

    @property
    def has_val(self):
        if (len(self.text)) >= 3:
            self.has_text = True
        return self.has_text


class Mouse(pygame.sprite.Sprite):
    def __init__(self):
            super().__init__()
            self.image = pygame.image.load(os.path.join(os.path.dirname(__file__), 'pictures','cursor.png')).convert_alpha()
            self.rect = self.image.get_rect()
        
    def update(self):
        self.rect.center = pygame.mouse.get_pos()


class Enter_Box(pygame.sprite.Sprite):
    def __init__(self,x,y,text):
        super().__init__()    
        self.font = pygame.font.SysFont("monaco",60)
        self.text = text
        self.location = (x,y)
        self.colour = ((0,0,0))
        self.background = (255,255,255)

    def update(self):
        self.image = self.font.render(self.text, 1,(self.colour), (self.background))
        self.rect = self.image.get_rect()
        self.rect.center = self.location


class Label(pygame.sprite.Sprite):
    def __init__(self,x,y,color = (255,255,255),text='',size = int(30)):
        super().__init__()
        self.size = size
        self.font = pygame.font.SysFont("areal",self.size)
        self.text = text
        self.center = (x,y)
        self.color = color
    def update(self):
        self.image = self.font.render(self.text,1,(self.color))
        self.rect = self.image.get_rect()
        self.rect.center = self.center


class Game_slection(pygame.sprite.Sprite):
    
    def __init__(self,x,y, color = (int,int,int),img_dir = '', img_size = (350,250)):
        super().__init__()
        try:
            self.image = pygame.image.load(img_dir)
        except:
            self.image = pygame.Surface(img_size)
            self.image.fill((color))
        
        self.rect = self.image.get_rect()
        self.font =  pygame.font.SysFont("areal",30) 
        self.center = (x,y)
    def update(self):   
        self.rect.center = self.center


def img(img=str):
    return os.path.join(os.path.dirname(__file__), 'pictures','{}'.format(img))

def sound(sound=str):
     return os.path.join(os.path.dirname(__file__), 'sounds', '{}'.format(sound))


def game_slection_screen():
    clock = pygame.time.Clock()

    background = pygame.image.load(img("christmas.jpg"))
    background.get_rect()
    page = Game_slection(175,300,(255,0,0),(img("snake_background.jpg")))
    page2 = Game_slection(625,300,(255,0,255),(img("space_invader_background.jpg")))
   
    page3 = Game_slection(400,75,(255,255,255),(img('title.PNG')),(600,150))
    page4 = Game_slection(400,550,(255,255,255),(img('highscore.png')),(600,150))
    mouse = Mouse()

    game_label = Label(175,350,[0,0,0],"Snake Game", 50)
    game_label2 = Label(625,350,[255,255,255],"Space Invaders",50)
    

    print_to_screen = pygame.sprite.Group(page,page2,page3,page4,mouse,game_label,game_label2)
    cursor = pygame.sprite.Group(mouse)
    
    game1 = pygame.sprite.Group(page)
    game2 = pygame.sprite.Group(page2)
    high_score_pg = pygame.sprite.Group(page4)
   
    

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.sprite.spritecollide(mouse,game1,False):
                    done = True
                    games.game_snake.main()
                    
                
                if pygame.sprite.spritecollide(mouse,game2,False):
                    done = True
                    games.Space_invaders.main()
                   
                
                if pygame.sprite.spritecollide(mouse,high_score_pg,False):
                    done = True
                    high_score_page.main()
                
                


        screen.blit(background,(0,0))
        print_to_screen.clear(screen,background)
        cursor.clear(screen,background)
        print_to_screen.update()
        cursor.update()
        print_to_screen.draw(screen)
        cursor.draw(screen)


        pygame.display.flip()
        clock.tick(30)


if __name__ =="__main__":
    game_slection_screen()
    pygame.quit()
 








