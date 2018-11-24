"""the main interface for final project"""
import pygame
import data_base_fuctions
import sys
sys.path.insert(0,"/Users/davesmith/Desktop/Python/final school project/School-Projects-master 2/final project/games/")
import game_snake



pygame.init()
screen = pygame.display.set_mode((800, 600))
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
FONT = pygame.font.Font(None, 25)
pygame.mouse.set_visible(False)


def text_objects(text, font):
    textSurface = font.render(text, True, (255,255,255))
    return textSurface, textSurface.get_rect()


class Password_Box:
    def __init__(self, text=''):
        self.rect = pygame.Rect(220, 130, 100, 30)
        self.color = color_inactive
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
                if event.key == pygame.K_RETURN:
                    intro = False
                    data_base_fuctions.dataBase_in()
                    game_slection_screen()
                    
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.txt_surface = FONT.render(self.text, True, self.color)
    
    def return_password(self):
        return self.text

    def update(self):
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(screen, self.color, self.rect, 2)

class Username_Box:

    def __init__(self, text = ''):
        self.rect = pygame.Rect(220, 100, 100, 30)
        self.color = color_inactive
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
            self.image = pygame.image.load("/Users/davesmith/Desktop/Python/final school project/School-Projects-master 2/final project/pictures/cursor.png")
            self.rect = self.image.get_rect()
        
    def update(self):
        self.rect.center = pygame.mouse.get_pos()



class Enter_Box(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.SysFont("arial",30)
        self.text = "Press to continue"
        self.location = (320,240)
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
    
        


screen_us = Username_Box()
screen_pw = Password_Box()
 
def game_login():
    background = pygame.Surface(screen.get_size())
    background = background.convert()

    
    enter = Enter_Box()
    mouse_loc = Mouse()

    
    label1 = Label(100,110, [255,255,255],"username", 30)
    label2 = Label(100,140,[255,255,255],"password", 30)
    print_to_screen = [screen_pw, screen_us]
    all_labels = pygame.sprite.Group(label1, label2, enter,mouse_loc)
    
    continue_box = pygame.sprite.Group(enter)

    global intro
    intro = True
    clock = pygame.time.Clock()
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro = False
            if event.type == pygame.MOUSEBUTTONDOWN:

                if pygame.sprite.spritecollide(mouse_loc,continue_box, False): 
                    data_base_fuctions.dataBase_in()
                    intro = False
                    game_slection_screen()
                                   
            
            for box in print_to_screen:
                box.handle_event(event)

        largeText = pygame.font.Font('freesansbold.ttf',30)
        TextSurf, TextRect = text_objects("Will's Cool game in the process", largeText)
        TextRect.center = ((400),(300))
        

        for box in print_to_screen:
            box.update()
        
        
        for box in print_to_screen:
            box.draw(screen)
        
        screen.blit(TextSurf, TextRect)
        all_labels.clear(screen,background)
        all_labels.update()
        all_labels.draw(screen)   
        
        
        
    
        pygame.display.flip()
        clock.tick(60)



def game_slection_screen():
    clock = pygame.time.Clock()
    background = pygame.image.load("/Users/davesmith/Desktop/Python/final school project/School-Projects-master 2/final project/pictures/christmas.jpg")
    background.get_rect()
    page = Game_slection(175,125,(255,0,0),"/Users/davesmith/Desktop/Python/final school project/School-Projects-master 2/final project/pictures/snake_background.jpg")
    page2 = Game_slection(175,475,(255,0,255))
    page3 = Game_slection(625,125,(0,255,0))
    page4 = Game_slection(625,475,(0,255,255))
    mouse = Mouse()


    game_label = Label(175,125,[0,0,0],"Snake Game", 50)

    print_to_screen = pygame.sprite.Group(page,page2,page3,page4,mouse,game_label)
    
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
                    game_snake.main()
                
                if pygame.sprite.spritecollide(mouse,game2,False):
                    done = True
                    #put game in here
                    #nsnake.main()
                
                if pygame.sprite.spritecollide(mouse,game3,False):
                    done = True
                    # put game in here
                
                if pygame.sprite.spritecollide(mouse,game4,False):
                    done = True



        screen.blit(background,(0,0))
        print_to_screen.clear(screen,background)
        print_to_screen.update()
        print_to_screen.draw(screen)

        pygame.display.flip()
        clock.tick(30)


if __name__ =="__main__":
    game_login()
 








