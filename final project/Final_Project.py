""""will's password generator + storage system"""
import sqlite3 as sq
import pygame
import sys
sys.path.insert(0,'T:/EAS-ICS3U1-1/will7460/Python/unit_3/final project/games')
import game_snake
import nsnake


pygame.init()
screen = pygame.display.set_mode((800, 600))
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
FONT = pygame.font.Font(None, 25)



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
                    dataBase_in()
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
            self.image = pygame.Surface((30,30))
            self.image.fill((255,0,0))
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
    def __init__(self,x,y,text=''):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.SysFont("areal",30)
        self.text = text
        self.center = (x,y)

    def update(self):
        self.image = self.font.render(self.text,1,(255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = self.center


class Game_slection(pygame.sprite.Sprite):
    def __init__(self, text = ""):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.rect.centerx = 255
        self.rect.centery = 255
        self.font =  pygame.font.SysFont("areal",30)    
        self.text = text
    def update(self):
        self.image = self.font.render(self.text,1,(255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = ((255,255))





screen_us = Username_Box()
screen_pw = Password_Box()
 
def game_login():
    global background
    background = pygame.Surface(screen.get_size())
    background = background.convert()

    
    enter = Enter_Box()
    mouse_loc = Mouse()

    
    
    
    label1 = Label(100,110,"your username")
    label2 = Label(100,140,"your password")
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
                    dataBase_in()
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
    background = pygame.image.load('christmas.jpg')
    background.get_rect()

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                #insert game
                #nsnake.main()
            

        screen.blit(background,(0,0))
        pygame.display.flip()
        clock.tick(30)
  
  
    


""" Second part of project"""



def dataBase_in():

    db = sq.connect('Game_Username_and_Password.db')
    c = db.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS player_data(username, password)")
    c.execute("INSERT INTO player_data(username, password)VALUES(:username, :password)",
            {'username':screen_us.return_username(),'password':screen_pw.return_password()})

    db.commit()






if __name__ =="__main__":
    game_login()
 







