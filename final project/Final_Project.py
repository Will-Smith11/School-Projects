"""the main interface for final project"""
import pygame
import data_base_fuctions
import sys
import os
import games.game_snake
import games.Space_invaders


pygame.init()
screen = pygame.display.set_mode((800, 600))
color_inactive = pygame.Color('black')
color_active = pygame.Color('white')
FONT = pygame.font.Font(None, 45)
pygame.mouse.set_visible(False)


class Username_Box:

    def __init__(self,x,y,w,h, text = ''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = ((0,0,0))
        self.text = ""
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False
      
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
        return self.text

    def update(self):
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(screen, self.color, self.rect, 2)
        

class Mouse(pygame.sprite.Sprite):
    def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load(os.path.join(os.path.dirname(__file__), 'pictures','cursor.png')).convert_alpha()
            self.rect = self.image.get_rect()
        
    def update(self):
        self.rect.center = pygame.mouse.get_pos()


class Enter_Box(pygame.sprite.Sprite):
    def __init__(self,x,y,text):
        pygame.sprite.Sprite.__init__(self)    
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
        pygame.sprite.Sprite.__init__(self)
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
    def __init__(self,x,y, color = (int,int,int),img_dir = ''):
        pygame.sprite.Sprite.__init__(self)
        try:
            self.image = pygame.image.load(img_dir)
        except:
            self.image = pygame.Surface((350,250))
            self.image.fill((color))
        
        self.rect = self.image.get_rect()
        self.font =  pygame.font.SysFont("areal",30) 
        self.center = (x,y)
    def update(self):   
        self.rect.center = self.center

class Ranking_display(pygame.sprite.Sprite):
    def __init__(self,x,y,color,game):
        pygame.sprite.Sprite.__init__(self)
        grab_info = data_base_fuctions.Give_Highscores(game)
        
        self.font = pygame.font.SysFont('monaco', 30)
        try:
            self.text = ("User '%s' Score of '%d' Is the top score for this game " % (grab_info.give_name(game),grab_info.give_score(game)))
        except:
            self.text = "error getting data"
        self.center = (x,y)
        self.color = color
    def update(self):
        self.image = self.font.render(self.text,1,(self.color))
        self.rect = self.image.get_rect()
        self.rect.center = self.center   

def img(img=str):
    return os.path.join(os.path.dirname(__file__), 'pictures','{}'.format(img))


def game_slection_screen():
    clock = pygame.time.Clock()

    background = pygame.image.load(img("christmas.jpg"))
    background.get_rect()
    page = Game_slection(175,125,(255,0,0),(img("snake_background.jpg")))
    page2 = Game_slection(175,475,(255,0,255),(img("space_invader_background.jpg")))
    page3 = Game_slection(625,125,(0,255,0))
    page4 = Game_slection(625,475,(0,255,255))
    mouse = Mouse()

    game_label = Label(175,125,[0,0,0],"Snake Game", 50)
    snake_leader = Ranking_display(175,300,(0,0,0),"Snake")

    game_label2 = Label(175,475,[255,255,255],"Space Invaders",50)
    space_leader = Ranking_display(175,340,(0,0,0),"Aliens")

    print_to_screen = pygame.sprite.Group(page,page2,page3,page4,game_label,game_label2,snake_leader,space_leader)
    cursor = pygame.sprite.Group(mouse)
    
    game1 = pygame.sprite.Group(page)
    game2 = pygame.sprite.Group(page2)
    game3 = pygame.sprite.Group(page3)
    game4 = pygame.sprite.Group(page4)
    

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
                   
                
                if pygame.sprite.spritecollide(mouse,game3,False):
                    done = True
                    # put game in here
                
                if pygame.sprite.spritecollide(mouse,game4,False):
                    done = True



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
 








